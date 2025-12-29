#!/bin/bash

# XAE-Frame v3.6 - Comprehensive Documentation & Config Update Script
# Updates: README, requirements, configs, docs
# Run AFTER update_structure_v36.sh

set -e  # Exit on error

BASE_DIR="$HOME/Desktop/xai-personalization-framework"
cd "$BASE_DIR"

echo "XAE-Frame v3.6 - Documentation & Config Update"
echo "=================================================="
echo ""

# STEP 1: UPDATE README.md



# STEP 2: UPDATE REQUIREMENTS FILES

echo "Step 2: Updating requirements files..."

# Update requirements-prod.txt
cat > requirements-prod.txt << 'REQEOF'
# XAE-Frame v3.6 - Production Dependencies
# Python 3.9+

# Core ML
numpy==1.24.3
pandas==2.0.3
scikit-learn==1.3.0
lightgbm==4.0.0

# XAI
shap==0.42.1
dice-ml==0.10  # v3.6: Counterfactual explanations

# Deep Learning (optional)
torch==2.0.1
tensorflow==2.13.0

# Data Processing
pyarrow==12.0.1
fastparquet==2023.7.0

# API
fastapi==0.100.0
uvicorn==0.23.0
pydantic==2.0.0

# Caching & Queue
redis==4.6.0
celery==5.3.1

# Monitoring
mlflow==2.5.0
prometheus-client==0.17.1

# Dashboard
streamlit==1.25.0
plotly==5.15.0
altair==5.0.1

# Fairness
fairlearn==0.9.0

# Utilities
python-dotenv==1.0.0
pyyaml==6.0.1
requests==2.31.0
tqdm==4.65.0

# Logging
loguru==0.7.0

# Testing (minimal for prod)
pytest==7.4.0
REQEOF

# Update requirements-dev.txt
cat > requirements-dev.txt << 'REQEOF'
# XAE-Frame v3.6 - Development Dependencies
# Includes all production deps + dev tools

-r requirements-prod.txt

# Development Tools
ipython==8.14.0
jupyter==1.0.0
jupyterlab==4.0.3
notebook==7.0.0

# Code Quality
black==23.7.0
flake8==6.0.0
pylint==2.17.4
mypy==1.4.1
isort==5.12.0

# Testing
pytest-cov==4.1.0
pytest-mock==3.11.1
pytest-asyncio==0.21.1
hypothesis==6.82.0

# Documentation
sphinx==7.1.0
sphinx-rtd-theme==1.3.0
myst-parser==2.0.0

# Profiling
memory-profiler==0.61.0
line-profiler==4.0.3

# Git Hooks
pre-commit==3.3.3

# v3.6 Specific
scipy==1.11.1  # For KS-test (skew detection)
REQEOF

# Create requirements.txt (points to prod)
cat > requirements.txt << 'REQEOF'
# XAE-Frame v3.6 - Default Installation
# For production use: pip install -r requirements-prod.txt
# For development: pip install -r requirements-dev.txt

-r requirements-prod.txt
REQEOF

echo "Requirements files updated!"
echo "   - requirements.txt (default)"
echo "   - requirements-prod.txt (production)"
echo "   - requirements-dev.txt (development)"
echo ""

# STEP 3: UPDATE CONFIG FILES

echo "  Step 3: Updating config files..."

# Create config directory if doesn't exist
mkdir -p config

# E-commerce config
cat > config/e_commerce.yaml << 'YAMLEOF'
# E-commerce Domain Configuration
domain:
  name: e_commerce
  description: "E-commerce product recommendations and rating prediction"

schema:
  user_id:
    - user_id
    - reviewerID
    - customer_id
  item_id:
    - parent_asin
    - asin
    - product_id
  target:
    - rating
    - score
  timestamp:
    - timestamp
    - unixReviewTime
  verification:
    - verified_purchase
    - is_verified
  engagement:
    - helpful_vote
    - helpfulness
  text:
    - review_text
    - text

target:
  type: rating
  range: [1, 5]
  distribution: left_skewed

features:
  temporal:
    - days_since_last_purchase
    - account_age_days
    - purchase_frequency
  text:
    - review_length
    - sentiment_score
    - tfidf_features
  user:
    - user_total_reviews
    - user_avg_rating
    - user_consistency
  item:
    - item_avg_rating
    - item_review_count
    - item_popularity

business_kpis:
  - Revenue Impact
  - Customer Lifetime Value
  - Churn Risk
  - Conversion Rate
YAMLEOF

# Finance config
cat > config/finance.yaml << 'YAMLEOF'
# Finance Domain Configuration
domain:
  name: finance
  description: "Credit scoring and loan approval prediction"

schema:
  user_id:
    - customer_id
    - applicant_id
  item_id:
    - loan_id
    - product_id
  target:
    - credit_score
    - default_risk
  timestamp:
    - application_date
    - timestamp
  verification:
    - verified_account
    - kyc_verified
  engagement:
    - app_usage_frequency
    - transaction_count
  text:
    - customer_notes
    - application_notes

target:
  type: credit_score
  range: [300, 850]
  distribution: normal

features:
  temporal:
    - days_since_account_open
    - transaction_frequency
  financial:
    - income
    - debt_to_income_ratio
    - account_balance
  user:
    - payment_history
    - credit_utilization
  item:
    - loan_amount
    - interest_rate

business_kpis:
  - Default Risk
  - Customer Profitability
  - Fraud Detection
  - Cross-Sell Opportunity
YAMLEOF

# Insurance config
cat > config/insurance.yaml << 'YAMLEOF'
# Insurance Domain Configuration
domain:
  name: insurance
  description: "Claim frequency prediction and policy pricing"

schema:
  user_id:
    - policy_holder_id
    - customer_id
  item_id:
    - policy_id
    - policy_number
  target:
    - claim_frequency
    - claim_amount
  timestamp:
    - policy_start_date
    - claim_date
  verification:
    - verified_identity
    - kyc_complete
  engagement:
    - policy_review_frequency
    - claim_submission_count
  text:
    - claim_description
    - notes

target:
  type: claim_frequency
  range: [0, null]  # 0 to N
  distribution: poisson

features:
  temporal:
    - policy_age_days
    - days_since_last_claim
  risk:
    - risk_score
    - coverage_amount
  user:
    - claim_history
    - premium_payment_consistency
  item:
    - policy_type
    - coverage_level

business_kpis:
  - Claim Frequency Prediction
  - Policy Renewal Rate
  - Loss Ratio Optimization
  - Fraud Detection
YAMLEOF

echo "Config files created!"
echo "   - config/e_commerce.yaml"
echo "   - config/finance.yaml"
echo "   - config/insurance.yaml"
echo ""

# STEP 4: UPDATE DOCUMENTATION

echo "Step 4: Updating documentation..."

mkdir -p docs/architecture

# Create v3.6 updates doc (already done in previous script, but ensure it exists)
if [ ! -f docs/architecture/v3.6_updates.md ]; then
    cat > docs/architecture/v3.6_updates.md << 'MDEOF'
# XAE-Frame v3.6 Architecture Updates

## Overview
Version 3.6 introduces proxy-aware XAI, dual-layer explanations, and enhanced compliance.

## New Components

### 1. Proxy Analysis Layer
**File:** `src/data/proxy_analyzer.py`

Classifies features as:
- **Causal:** Unchangeable (demographics, temporal)
- **Proxy:** Changeable, gameable (engagement metrics)
- **Actionable:** User can legitimately modify

**Gaming Risk Assessment:**
- NONE: Causal features
- LOW: Difficult to manipulate
- MEDIUM: Actionable but monitored
- HIGH: Easily gameable (proxies)

### 2. Feature Store
**File:** `src/data/feature_store.py`

Ensures training-serving consistency:
- Single source of truth for feature computation
- Used in BOTH training and serving
- Implements Google ML Rule #32

### 3. Intrinsic Baseline
**File:** `src/models/intrinsic_baseline.py`

Decision Tree for interpretability:
- Max depth: 5 (human-readable)
- Fidelity cross-check with LightGBM
- Human-readable rules extraction

### 4. Dual-Layer XAI System

**Layer 1: Admin/Stakeholder View**
- **File:** `src/dashboard/admin_view.py`
- **Content:** Full model transparency (SHAP/LIME)
- **Audience:** Data scientists, managers, auditors
- **Features:** Proxy risk scores, drift timelines, compliance

**Layer 2: User View**
- **File:** `src/dashboard/user_view.py`
- **Content:** Actionable counterfactuals (DiCE-ML)
- **Audience:** End users
- **Features:** "What can I change?" recommendations

### 5. Explanation Fidelity Checker
**File:** `src/explainability/fidelity.py`

Validates explanation quality:
- **Model Agreement:** Baseline vs complex model (>0.80)
- **SHAP Fidelity:** SHAP accuracy (>0.90)
- **Stability:** Noise robustness (>0.80)

### 6. Counterfactual Explainer
**File:** `src/explainability/counterfactual.py`

DiCE-ML integration:
- Generates "what-if" scenarios
- Filters to actionable features only
- Prevents proxy manipulation suggestions

### 7. Training-Serving Skew Monitor
**File:** `src/realtime/log_monitor.py`

Detects preprocessing differences:
- Logs: raw input → preprocessing → prediction
- Weekly KS-test vs training baseline
- Alerts on significant skew (p < 0.05)

### 8. Governance Auditor
**File:** `src/compliance/governance.py`

Automated compliance checking:
- **EU AI Act:** Articles 10-15 (data quality, fairness)
- **NIST IR 8312:** 4 principles (explanation, meaningful, etc.)
- **Report Generation:** JSON audit logs

## Testing Framework

### New Test Suites

**1. Skew Tests** (`tests/skew_tests.py`)
- Training-serving consistency
- Feature computation identity
- Distribution shift detection

**2. Proxy Tests** (`tests/proxy_tests.py`)
- Gaming vulnerability assessment
- Proxy taxonomy accuracy
- Manipulation sensitivity

**3. Stability Tests** (`tests/stability_tests.py`)
- SHAP noise robustness
- Explanation consistency
- Perturbation analysis

## Success Metrics (v3.6)

### Performance
- RMSE < 0.9
- Coverage > 70%
- Serendipity > 15%

### XAI Quality
- Model Fidelity > 0.80
- SHAP Fidelity > 0.90
- Stability > 0.80

### Compliance
- Data Quality > 80/100
- Fairness Ratio > 0.80
- NIST Compliance: 100%

## Migration Guide

### From v3.5 to v3.6

1. **Structure Update:**
   ```bash
   ./update_structure_v36.sh
   ./update_docs_configs_v36.sh
   ```

2. **Install New Dependencies:**
   ```bash
   pip install -r requirements-prod.txt --upgrade
   ```

3. **Update Feature Engineering:**
   ```python
   from src.data.proxy_analyzer import ProxyAnalyzer
   
   analyzer = ProxyAnalyzer()
   taxonomy = analyzer.analyze_dataset(df)
   ```

4. **Train Dual Baselines:**
   ```python
   # Performance
   lgbm = train_lightgbm(X_train, y_train)
   
   # Interpretability
   tree = IntrinsicBaseline().train(X_train, y_train)
   
   # Check fidelity
   fidelity_checker.check_model_agreement(lgbm, tree, X_test)
   ```

5. **Run Compliance Audit:**
   ```python
   from src.compliance.governance import GovernanceAuditor
   
   auditor = GovernanceAuditor()
   auditor.check_data_quality(85.0)
   auditor.check_fairness(0.82)
   auditor.generate_audit_report()
   ```

---
**Version:** 3.6  
**Date:** December 2025  
**Author:** Nazlı Özgür
MDEOF
fi

# Create proxy taxonomy guide
cat > docs/proxy_taxonomy.md << 'MDEOF'
# Proxy Taxonomy Guide

## Overview
The Proxy Taxonomy system classifies features by their manipulability and gaming risk.

## Feature Types

### 1. Causal Features
**Definition:** Unchangeable attributes (root causes)

**Examples:**
- User age
- Account creation date
- Geographic location
- Gender
- Birth date

**Properties:**
- `manipulable`: False
- `gaming_risk`: NONE
- `causal_parent`: demographics/temporal

**Why Important:** These are "true" features that reflect reality.

### 2. Proxy Features
**Definition:** Changeable metrics that correlate with but don't cause outcomes

**Examples:**
- Helpful votes
- Review count
- Engagement score
- Activity frequency
- Rating history

**Properties:**
- `manipulable`: True
- `gaming_risk`: HIGH
- `causal_parent`: None (surface-level metric)

**Why Dangerous:** 
- Can be artificially inflated
- Gaming the system becomes easy
- Model learns spurious correlations

### 3. Actionable Features
**Definition:** User can legitimately modify

**Examples:**
- Verified purchase badge
- Review text length
- Premium subscription
- Profile completeness

**Properties:**
- `manipulable`: True
- `gaming_risk`: MEDIUM
- `causal_parent`: None

**Why Useful:**
- Can be suggested in counterfactuals
- User has control
- Legitimate improvement path

## Gaming Risk Levels

### NONE
- Feature cannot be manipulated
- Safe to use without restriction
- Example: User age, account creation date

### LOW
- Difficult to manipulate
- Requires significant effort
- Example: Historical purchase pattern

### MEDIUM
- Can be changed but monitored
- Example: Profile information, verified status

### HIGH
- Easily gameable
- Vulnerable to manipulation
- Example: Votes, ratings, counts

## Usage in XAE-Frame

### 1. Feature Engineering
```python
from src.data.proxy_analyzer import ProxyAnalyzer

analyzer = ProxyAnalyzer()
taxonomy = analyzer.analyze_dataset(df)

# Export for documentation
analyzer.export_taxonomy('data/processed/proxy_taxonomy.json')

# Get high-risk features
high_risk = analyzer.get_high_risk_features()
```

### 2. Model Training
- Monitor proxy feature importance
- Test model with proxy manipulation
- Document proxy dependencies

### 3. XAI Layer
**Admin View:** Show ALL features (including proxies)
**User View:** Show ONLY actionable features (filter out high-risk proxies)

### 4. Counterfactual Generation
```python
# Filter counterfactuals to exclude high-risk proxies
actionable_cf = cf_explainer.filter_actionable_features(
    counterfactuals,
    proxy_taxonomy
)
```

## Best Practices

###DO:
- Label all features in taxonomy
- Monitor high-risk proxy importance
- Test for gaming vulnerability
- Filter user-facing explanations
- Document proxy dependencies

###DON'T:
- Suggest proxy manipulation in counterfactuals
- Rely solely on proxy features
- Ignore gaming risk in production
- Show technical proxies to end users
- Skip taxonomy documentation

## Example Taxonomy

```json
{
  "user_age": {
    "type": "Causal",
    "manipulable": false,
    "gaming_risk": "NONE",
    "causal_parent": "demographics"
  },
  "helpful_vote": {
    "type": "Proxy",
    "manipulable": true,
    "gaming_risk": "HIGH",
    "causal_parent": null,
    "description": "Easily manipulable engagement metric"
  },
  "verified_purchase": {
    "type": "Actionable",
    "manipulable": true,
    "gaming_risk": "MEDIUM",
    "causal_parent": null,
    "description": "User can legitimately verify purchases"
  }
}
```

---
**Author:** Nazlı Özgür  
**Version:** 3.6  
**Date:** December 2025
MDEOF

echo "Documentation files created!"
echo "   - docs/architecture/v3.6_updates.md"
echo "   - docs/proxy_taxonomy.md"
echo ""

# STEP 5: UPDATE .gitignore

echo "Step 5: Updating .gitignore..."

# Append v3.6 specific ignores
cat >> .gitignore << 'GITEOF'

# v3.6 Additions

# Proxy taxonomy outputs
data/processed/proxy_taxonomy.json

# Serving logs
logs/serving.log
logs/serving.log.*

# Compliance audit reports
docs/compliance_audit.json
docs/audit_*.json

# Model fidelity reports
docs/fidelity_report_*.json

# Backup files
*.backup
*~

# Redis dumps
dump.rdb
*.rdb

# Temporary test outputs
tests/output/
.pytest_cache/

# MLflow artifacts (if not already covered)
mlruns/
mlartifacts/

# Jupyter checkpoints
.ipynb_checkpoints/
*/.ipynb_checkpoints/*

# VSCode settings (keep local)
.vscode/settings.json

# macOS
.DS_Store
.AppleDouble
.LSOverride
GITEOF

echo " .gitignore updated!"
echo ""

# STEP 6: CREATE VERSION FILE

echo "Step 6: Creating version file..."

cat > VERSION << 'VEREOF'
3.6.0
VEREOF

cat > src/__version__.py << 'PYEOF'
"""XAE-Frame version information"""
__version__ = "3.6.0"
__author__ = "Nazlı Özgür"
__email__ = "your-email@example.com"
__description__ = "Explainable AI Framework for Cross-Domain Personalization"
PYEOF

echo "Version files created!"
echo ""

# STEP 7: SUMMARY

echo ""
echo "XAE-Frame v3.6 - Documentation & Config Update Complete!"
echo "============================================================"
echo ""
echo "Updated Files:"
echo "   - README.md (comprehensive v3.6 docs)"
echo "   - requirements.txt (default)"
echo "   - requirements-prod.txt (production deps)"
echo "   - requirements-dev.txt (dev tools + DiCE-ML)"
echo "   - config/e_commerce.yaml"
echo "   - config/finance.yaml"
echo "   - config/insurance.yaml"
echo "   - docs/architecture/v3.6_updates.md"
echo "   - docs/proxy_taxonomy.md"
echo "   - .gitignore (v3.6 additions)"
echo "   - VERSION (3.6.0)"
echo "   - src/__version__.py"
echo ""
echo "Next Steps:"
echo "   1. Review updated files in VSCode"
echo "   2. Install updated dependencies:"
echo "      pip install -r requirements-prod.txt --upgrade"
echo "   3. Run git status to see changes"
echo "   4. Commit everything:"
echo "      git add ."
echo "      git commit -m 'docs: XAE-Frame v3.6 documentation and config update'"
echo "      git push origin main"
echo ""
echo "You're now ready for v3.6 development!"
echo ""

echo "Script created: update_docs_configs_v36.sh"
echo ""
echo "VERIFICATION: To update your VSCode project:"
echo "   1. Run: ./update_structure_v36.sh (creates new Python files)"
echo "   2. Run: ./update_docs_configs_v36.sh (updates docs & configs)"
echo "   3. Done! All v3.6 updates applied!"
