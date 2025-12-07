#!/usr/bin/env python3
"""
Database Initialization Script for XAE-Frame
Creates PostgreSQL tables for metadata, logs, and user interactions.

Usage:
    python scripts/init_db.py
"""

import os
import sys
from pathlib import Path

# Add src to path
sys.path.append(str(Path(__file__).parent.parent / "src"))

from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Float,
    DateTime,
    Boolean,
    JSON,
    Text,
    text,
)
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Base class for models
Base = declarative_base()


# DATABASE MODELS

class Model(Base):
    """ML Model metadata"""
    __tablename__ = "models"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    version = Column(String(50), nullable=False)
    model_type = Column(String(50))  # lightgbm, xgboost, etc.
    domain = Column(String(50))  # e_commerce, finance, insurance
    
    # Performance metrics
    train_accuracy = Column(Float)
    val_accuracy = Column(Float)
    test_accuracy = Column(Float)
    
    # Metadata
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    is_active = Column(Boolean, default=True)
    mlflow_run_id = Column(String(255))
    
    # Configuration
    config = Column(JSON)  # Store full config as JSON


class Prediction(Base):
    """Prediction logs"""
    __tablename__ = "predictions"
    
    id = Column(Integer, primary_key=True)
    model_id = Column(Integer, nullable=False)
    user_id = Column(String(255))
    item_id = Column(String(255))
    
    # Prediction details
    prediction = Column(Float)
    confidence = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)
    
    # Features used
    features = Column(JSON)
    
    # Explanation (SHAP values)
    explanation = Column(JSON) # Store SHAP values/feature contributions for XAI transparency


class DriftAlert(Base):
    """Drift detection alerts"""
    __tablename__ = "drift_alerts"
    
    id = Column(Integer, primary_key=True)
    model_id = Column(Integer, nullable=False)
    
    # Drift details
    drift_type = Column(String(50)) # Records if drift is concept (user behavior) or data (feature shift)
    drift_score = Column(Float)
    threshold = Column(Float)
    
    # Timing
    detected_at = Column(DateTime, default=datetime.utcnow)
    
    # Affected features
    affected_features = Column(JSON)
    
    # Action taken
    action_taken = Column(String(255))  # retraining_triggered, alert_sent, etc.


class FairnessMetric(Base):
    """Fairness monitoring metrics"""
    __tablename__ = "fairness_metrics"
    
    id = Column(Integer, primary_key=True)
    model_id = Column(Integer, nullable=False)
    
    # Protected attribute
    protected_attribute = Column(String(100))  # Sensitive attribute subject to bias monitoring (e.g., age, gender)
    
    # Metrics
    demographic_parity = Column(Float)
    equal_opportunity = Column(Float)
    disparate_impact = Column(Float)
    
    # Timestamp
    measured_at = Column(DateTime, default=datetime.utcnow)
    
    # Pass/fail
    is_fair = Column(Boolean)


class UserInteraction(Base):
    """User interaction logs for feedback loop"""
    __tablename__ = "user_interactions"
    
    id = Column(Integer, primary_key=True)
    user_id = Column(String(255), nullable=False)
    item_id = Column(String(255), nullable=False)
    
    # Interaction type
    interaction_type = Column(String(50))  # click, purchase, return, rating
    
    # Interaction details
    rating = Column(Float)
    dwell_time = Column(Float)  # seconds
    purchased = Column(Boolean, default=False) # Used as the positive label/signal for the adaptive feedback loop
    returned = Column(Boolean, default=False)
    
    # Timing
    timestamp = Column(DateTime, default=datetime.utcnow)
    
    # Context
    session_id = Column(String(255))
    device_type = Column(String(50))


class BusinessMetric(Base):
    """Business impact metrics"""
    __tablename__ = "business_metrics"
    
    id = Column(Integer, primary_key=True)
    model_id = Column(Integer, nullable=False)
    
    # Metrics
    metric_name = Column(String(100))  # conversion_rate, churn_rate, etc.
    metric_value = Column(Float)
    
    # Comparison with baseline
    baseline_value = Column(Float)
    lift_percentage = Column(Float)
    
    # A/B test group
    is_control_group = Column(Boolean, default=False)
    
    # Timing
    measured_at = Column(DateTime, default=datetime.utcnow)
    period_start = Column(DateTime)
    period_end = Column(DateTime)


class ComplianceReport(Base):
    """EU AI Act compliance reports"""
    __tablename__ = "compliance_reports"
    
    id = Column(Integer, primary_key=True)
    model_id = Column(Integer, nullable=False)
    
    # Report details
    report_date = Column(DateTime, default=datetime.utcnow)
    report_type = Column(String(50))  # weekly, monthly, audit
    
    # Compliance status
    transparency_score = Column(Float)
    accountability_score = Column(Float)
    fairness_score = Column(Float)
    robustness_score = Column(Float)
    
    # Overall
    is_compliant = Column(Boolean)
    
    # Detailed report (JSON)
    detailed_report = Column(JSON)
    
    # PDF path
    pdf_path = Column(String(500))


# DATABASE INITIALIZATION

def init_database(database_url: str = None):
    """
    Initialize database with all tables.
    
    Args:
        database_url: PostgreSQL connection string
                     If None, uses environment variable or SQLite fallback
    """
    if database_url is None:
        # Try environment variable first
        database_url = os.getenv(
            "DATABASE_URL",
            "sqlite:///data/xae_frame.db"  # Fallback to SQLite
        )
    
    logger.info(f"Connecting to database: {database_url.split('@')[-1]}")  # Hide password
    
    try:
        # Create engine
        engine = create_engine(database_url)
        
        # Create all tables
        Base.metadata.create_all(engine)
        
        logger.info("Database tables created successfully!")
        logger.info(f"  Tables: {list(Base.metadata.tables.keys())}")
        
        # Test connection
        Session = sessionmaker(bind=engine)
        session = Session()
        session.execute(text("SELECT 1"))
        session.close()
        
        logger.info("Database connection test passed!")
        
        return engine
        
    except Exception as e:
        logger.error(f"Failed to initialize database: {e}")
        raise


def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Initialize XAE-Frame database")
    parser.add_argument(
        "--database-url",
        type=str,
        default=None,
        help="Database connection string (default: from .env or SQLite)"
    )
    
    args = parser.parse_args()
    
    try:
        engine = init_database(args.database_url)
        logger.info("Database initialization complete!")
        return 0
    except Exception as e:
        logger.error(f"Database initialization failed: {e}")
        return 1


if __name__ == "__main__":
    exit(main())