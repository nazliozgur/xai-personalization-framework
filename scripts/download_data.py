#!/usr/bin/env python3
"""
XAE-Frame Data Download Script
Downloads datasets for e-commerce, finance, and insurance domains.

Usage:
    python scripts/download_data.py --dataset amazon_reviews --category Electronics
    python scripts/download_data.py --dataset finance --sample-size 10000
    python scripts/download_data.py --all
"""

import argparse
import logging
import os
from pathlib import Path
from typing import Optional

from datasets import load_dataset
import pandas as pd
from tqdm import tqdm

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class DataDownloader:
    """Download and prepare datasets for XAE-Frame."""
    
    def __init__(self, data_dir: str = "data/raw"):
        """Initialize downloader with data directory."""
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(parents=True, exist_ok=True)
        logger.info(f"Data directory: {self.data_dir.absolute()}")
    
    def download_amazon_reviews(
        self, 
        category: str = "All_Beauty",
        sample_size: Optional[int] = None
    ):
        """
        Download Amazon Reviews 2023 dataset.
        
        Args:
            category: Product category (e.g., Electronics, Books, All_Beauty)
            sample_size: Number of samples to download (None = full dataset)
        
        Available categories:
            - All_Beauty, Toys_and_Games, Cell_Phones_and_Accessories
            - Electronics, Movies_and_TV, Clothing_Shoes_and_Jewelry
            - Home_and_Kitchen, Books, Sports_and_Outdoors
            - And many more...
        """
        logger.info(f"Downloading Amazon Reviews 2023 - {category}...")
        
        try:
            # Load dataset from HuggingFace
            dataset = load_dataset(
                "McAuley-Lab/Amazon-Reviews-2023",
                f"raw_review_{category}",
                split="full",
                trust_remote_code=True
            )
            
            # Convert to pandas
            df = dataset.to_pandas()
            
            logger.info(f"Full dataset size: {len(df):,} reviews")
            
            # Sample if requested
            if sample_size and sample_size < len(df):
                df = df.sample(n=sample_size, random_state=42)
                logger.info(f"Sampled to {sample_size:,} reviews")
            
            # Save to parquet (more efficient than CSV)
            output_path = self.data_dir / f"amazon_reviews_{category}.parquet"
            df.to_parquet(output_path, index=False)
            
            logger.info(f"✓ Saved to {output_path}")
            logger.info(f"  Columns: {list(df.columns)}")
            logger.info(f"  Shape: {df.shape}")
            
            # Download metadata separately
            self._download_amazon_metadata(category, sample_size)
            
            return df
            
        except Exception as e:
            logger.error(f"Failed to download Amazon Reviews: {e}")
            raise
    
    def _download_amazon_metadata(
        self, 
        category: str,
        sample_size: Optional[int] = None
    ):
        """Download product metadata for Amazon Reviews."""
        logger.info(f"Downloading product metadata for {category}...")
        
        try:
            dataset = load_dataset(
                "McAuley-Lab/Amazon-Reviews-2023",
                f"raw_meta_{category}",
                split="full",
                trust_remote_code=True
            )
            
            df = dataset.to_pandas()
            
            if sample_size and sample_size < len(df):
                df = df.sample(n=min(sample_size, len(df)), random_state=42)
            
            output_path = self.data_dir / f"amazon_metadata_{category}.parquet"
            df.to_parquet(output_path, index=False)
            
            logger.info(f"✓ Saved metadata to {output_path}")
            
        except Exception as e:
            logger.warning(f"Could not download metadata: {e}")
    
    def download_finance_dataset(self, dataset_name: str = "credit_card_fraud"):
        """
        Download finance-related datasets.
        
        Options:
            - credit_card_fraud: Kaggle Credit Card Fraud Detection
            - home_credit: Home Credit Default Risk
        """
        logger.info(f"Downloading finance dataset: {dataset_name}...")
        
        if dataset_name == "credit_card_fraud":
            self._download_credit_card_fraud()
        elif dataset_name == "home_credit":
            logger.warning("Home Credit requires Kaggle API. Please download manually from:")
            logger.warning("https://www.kaggle.com/c/home-credit-default-risk/data")
        else:
            logger.error(f"Unknown finance dataset: {dataset_name}")
    
    def _download_credit_card_fraud(self):
        """Download Credit Card Fraud dataset from Kaggle."""
        logger.warning("Credit Card Fraud dataset requires Kaggle API.")
        logger.info("To download:")
        logger.info("1. Install kaggle: pip install kaggle")
        logger.info("2. Setup API credentials: https://www.kaggle.com/docs/api")
        logger.info("3. Run: kaggle datasets download -d mlg-ulb/creditcardfraud")
        logger.info("4. Extract to data/raw/")
        
        # Alternative: Use a synthetic dataset for demo
        logger.info("Generating synthetic credit card transaction data for demo...")
        self._generate_synthetic_finance_data()
    
    def _generate_synthetic_finance_data(self, n_samples: int = 10000):
        """Generate synthetic finance data for prototyping."""
        import numpy as np
        
        np.random.seed(42)
        
        df = pd.DataFrame({
            'transaction_id': range(n_samples),
            'customer_id': np.random.randint(1000, 5000, n_samples),
            'transaction_amount': np.random.lognormal(4, 1.5, n_samples),
            'transaction_type': np.random.choice(['purchase', 'withdrawal', 'transfer'], n_samples),
            'merchant_category': np.random.choice(['retail', 'food', 'travel', 'entertainment'], n_samples),
            'is_fraud': np.random.choice([0, 1], n_samples, p=[0.998, 0.002]),
            'customer_age': np.random.randint(18, 80, n_samples),
            'account_balance': np.random.lognormal(8, 2, n_samples),
            'timestamp': pd.date_range('2023-01-01', periods=n_samples, freq='5min')
        })
        
        output_path = self.data_dir / "synthetic_finance_data.parquet"
        df.to_parquet(output_path, index=False)
        
        logger.info(f"✓ Generated synthetic finance data: {output_path}")
        logger.info(f"  Shape: {df.shape}")
        logger.info(f"  Fraud rate: {df['is_fraud'].mean():.2%}")
    
    def download_insurance_dataset(self, dataset_name: str = "safe_driver"):
        """
        Download insurance-related datasets.
        
        Options:
            - safe_driver: Porto Seguro Safe Driver Prediction
            - health_insurance: Health Insurance Cross-Sell
        """
        logger.info(f"Downloading insurance dataset: {dataset_name}...")
        
        if dataset_name == "safe_driver":
            logger.warning("Porto Seguro dataset requires Kaggle API.")
            logger.info("Download from: https://www.kaggle.com/c/porto-seguro-safe-driver-prediction/data")
        elif dataset_name == "health_insurance":
            logger.warning("Health Insurance dataset requires Kaggle API.")
            logger.info("Download from: https://www.kaggle.com/datasets/anmolkumar/health-insurance-cross-sell-prediction")
        
        # Generate synthetic insurance data for demo
        logger.info("Generating synthetic insurance data for demo...")
        self._generate_synthetic_insurance_data()
    
    def _generate_synthetic_insurance_data(self, n_samples: int = 10000):
        """Generate synthetic insurance data for prototyping."""
        import numpy as np
        
        np.random.seed(42)
        
        df = pd.DataFrame({
            'policy_id': range(n_samples),
            'customer_id': np.random.randint(1000, 5000, n_samples),
            'age': np.random.randint(18, 80, n_samples),
            'gender': np.random.choice(['M', 'F'], n_samples),
            'vehicle_age': np.random.choice(['<1 Year', '1-2 Years', '>2 Years'], n_samples),
            'vehicle_damage': np.random.choice(['Yes', 'No'], n_samples, p=[0.3, 0.7]),
            'annual_premium': np.random.lognormal(8, 0.8, n_samples),
            'policy_sales_channel': np.random.randint(1, 160, n_samples),
            'vintage': np.random.randint(10, 300, n_samples),
            'risk_score': np.random.uniform(0, 1, n_samples),
            'claim_amount': np.where(
                np.random.random(n_samples) < 0.1,
                np.random.lognormal(7, 1, n_samples),
                0
            )
        })
        
        output_path = self.data_dir / "synthetic_insurance_data.parquet"
        df.to_parquet(output_path, index=False)
        
        logger.info(f"✓ Generated synthetic insurance data: {output_path}")
        logger.info(f"  Shape: {df.shape}")
        logger.info(f"  Claim rate: {(df['claim_amount'] > 0).mean():.2%}")
    
    def download_all(self, sample_size: Optional[int] = 10000):
        """Download all datasets with sampling for quick start."""
        logger.info("Downloading all datasets (sampled)...")
        
        # E-commerce (primary demo)
        self.download_amazon_reviews(category="All_Beauty", sample_size=sample_size)
        
        # Finance (demo with synthetic data)
        self.download_finance_dataset("credit_card_fraud")
        
        # Insurance (demo with synthetic data)
        self.download_insurance_dataset("safe_driver")
        
        logger.info("✓ All datasets downloaded!")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Download datasets for XAE-Frame",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument(
        "--dataset",
        type=str,
        choices=["amazon_reviews", "finance", "insurance", "all"],
        default="amazon_reviews",
        help="Dataset to download"
    )
    
    parser.add_argument(
        "--category",
        type=str,
        default="All_Beauty",
        help="Category for Amazon Reviews (e.g., Electronics, Books)"
    )
    
    parser.add_argument(
        "--sample-size",
        type=int,
        default=None,
        help="Number of samples to download (None = full dataset)"
    )
    
    parser.add_argument(
        "--data-dir",
        type=str,
        default="data/raw",
        help="Directory to save data"
    )
    
    args = parser.parse_args()
    
    # Create downloader
    downloader = DataDownloader(data_dir=args.data_dir)
    
    # Download requested dataset(s)
    try:
        if args.dataset == "amazon_reviews":
            downloader.download_amazon_reviews(
                category=args.category,
                sample_size=args.sample_size
            )
        elif args.dataset == "finance":
            downloader.download_finance_dataset()
        elif args.dataset == "insurance":
            downloader.download_insurance_dataset()
        elif args.dataset == "all":
            downloader.download_all(sample_size=args.sample_size or 10000)
        
        logger.info("✓ Download complete!")
        
    except Exception as e:
        logger.error(f"Download failed: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
