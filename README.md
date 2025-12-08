# XAE-Frame: Explainable, Adaptive & Ethical AI Framework for Cross-Domain Personalization

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![NIST Compliant](https://img.shields.io/badge/NIST-Compliant-green.svg)](https://www.nist.gov/publications/four-principles-explainable-artificial-intelligence)
[![EU AI Act Ready](https://img.shields.io/badge/EU%20AI%20Act-Ready-blue.svg)](https://artificialintelligenceact.eu/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)


**A production-ready AI framework that combines cross-domain personalization, explainable AI, adaptive learning, and ethical oversight for trustworthy recommendation systems.**

> **M.Sc. Thesis Project** | Istanbul University - Management Information Systems  
> **Author:** Nazlı Özgür | **Industry Partner:** MindTech

---

## Problem Statement

Modern recommendation systems face a critical challenge: they optimize for accuracy but fail to address transparency, adaptability, and fairness. This creates three major issues:

1. **Black-box decisions** - Users and regulators cannot understand why recommendations are made
2. **Static models** - Systems fail to adapt to changing user behavior and data patterns
3. **Domain isolation** - Organizations cannot transfer AI knowledge across business units

With the EU AI Act enforcement beginning in 2025, organizations need AI systems that are not only accurate but also explainable, adaptive, and verifiably fair. Current solutions like Clerk.io provide recommendations but lack the transparency, ethical oversight, and cross-domain flexibility required by modern regulations and business needs.

**XAE-Frame addresses these challenges** by integrating explainability, cross-domain transfer learning, adaptive retraining, and ethical monitoring into a unified framework designed for enterprise deployment.

---

## Key Capabilities

### Cross-Domain Personalization
Transfer user preferences and behavioral patterns across different business domains (e-commerce, finance, insurance). The framework goes beyond simple preference transfer by preserving the reasoning behind recommendations, enabling meaningful knowledge transfer even between semantically different domains. Transfer is achieved through deep learning-based embedding mapping (utilizing neural collaborative filtering and matrix factorization techniques), effectively solving cold-start problems in target domains by leveraging rich knowledge from source domains.

### Explainable AI Integration (NIST-Compliant)
Built on SHAP (SHapley Additive exPlanations) with full compliance to NIST's Four Principles of Explainable AI:

1. **Explanation**: Every prediction comes with evidence-based reasoning
2. **Meaningful**: Context-aware explanations adapted to user expertise (technical deep-dive vs. business summary)
3. **Explanation Accuracy**: Fidelity metrics ensure explanations truly reflect model behavior
4. **Knowledge Limits**: Confidence thresholds and out-of-distribution detection prevent unreliable predictions

The system generates five types of explanations aligned with NIST standards: user benefit (simple "why"), societal acceptance (trust-building), regulatory compliance (audit trails), system development (debugging), and owner benefit (business value). Technical users receive detailed feature importance with statistical measures, while business users get simplified, actionable insights.

### Adaptive Learning Engine
Real-time concept drift detection using Alibi Detect monitors changes in user behavior and triggers automated retraining strategies. The system tracks behavioral patterns including click timing, session duration, purchase patterns, and preference evolution. When significant drift is detected (using statistical tests such as ADWIN), the framework automatically initiates retraining with optimized data selection strategies while maintaining explanation consistency.

**Key innovations:**
- **Automated retraining triggers**: Performance threshold monitoring + time-based scheduling
- **Feedback loop integration**: User interactions (clicks, purchases, returns) continuously improve model accuracy
- **A/B testing**: New models are validated against control groups before full deployment

### Ethical AI & Compliance
Continuous bias monitoring across demographic groups using Fairlearn and AIF360, with automated fairness metrics including Demographic Parity and Equal Opportunity. The system performs regular audits to detect bias amplification during cross-domain transfers, ensuring that knowledge transfer does not introduce or propagate unfair patterns.

**EU AI Act compliance features:**
- Transparency requirements: Full decision traceability and explainability
- Accountability: Automated audit logs and compliance reports (PDF)
- Fairness: Real-time bias detection with mitigation strategies
- Robustness: Adversarial testing and drift monitoring

### Business Impact Measurement
Quantifies AI value through metrics that matter to stakeholders. The framework includes a **metric mapping layer** that connects technical AI performance to business outcomes:

| XAI Metric | Business KPI |
|-----------|--------------|
| Explanation Quality | Customer Trust (surveys) |
| Model Confidence | Conversion Rate |
| Fairness Score | Brand Reputation (NPS) |
| Drift Detection | Revenue Stability |

Real-time tracking through an interactive dashboard shows: revenue lift, conversion rate improvement, churn reduction, and customer lifetime value increase.

---

## Technical Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                    LAYER 1: USER INTERFACE                           │
├─────────────────────────────────────────────────────────────────────┤
│  ┌──────────────┬──────────────┬──────────────┬─────────────────┐  │
│  │  Executive   │ Data Science │  Compliance  │   End User      │  │
│  │  Dashboard   │  Dashboard   │   Dashboard  │   Interface     │  │
│  │  (ROI/KPI)   │  (Technical) │  (Audit)     │  (Simple Why)   │  │
│  └──────────────┴──────────────┴──────────────┴─────────────────┘  │
│  • Streamlit/React-based multi-view interface                       │
│  • Role-based access control (RBAC)                                 │
└────────────────────────────┬────────────────────────────────────────┘
                             │
┌────────────────────────────▼────────────────────────────────────────┐
│          LAYER 2: EXPLANATION PERSONALIZATION ENGINE                 │
├─────────────────────────────────────────────────────────────────────┤
│  • Role Detection & Authorization                                    │
│  • Explanation Complexity Adjustment (5 NIST Categories)             │
│  • Language Simplification (Technical → Business)                    │
│  • Metric Mapping (XAI Metrics → Business KPIs)                      │
└────────────────────────────┬────────────────────────────────────────┘
                             │
┌────────────────────────────▼────────────────────────────────────────┐
│                 LAYER 3: CORE XAE-FRAME ENGINES                      │
├─────────────────────────────────────────────────────────────────────┤
│                                                                       │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │              3A. EXPLAINABILITY (XAI) ENGINE                  │  │
│  ├──────────────────────────────────────────────────────────────┤  │
│  │  • SHAP Value Computation (Feature Importance)                │  │
│  │  • Multi-Level Explanations (NIST 5 Categories)               │  │
│  │  • Explanation Accuracy Tracker (Fidelity Metrics)            │  │
│  │  • Knowledge Limits Module                                    │  │
│  │     - Confidence thresholds                                   │  │
│  │     - Out-of-distribution detection (Alibi Detect)            │  │
│  │     - Uncertainty quantification                              │  │
│  └──────────────────────────────────────────────────────────────┘  │
│                                                                       │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │              3B. ADAPTIVE LEARNING ENGINE                     │  │
│  ├──────────────────────────────────────────────────────────────┤  │
│  │  • Drift Detection (Alibi Detect)                             │  │
│  │     - Concept drift (user behavior changes)                   │  │
│  │     - Data drift (feature distribution shifts)                │  │
│  │  • Automated Retraining Strategy                              │  │
│  │     - Trigger conditions (performance drop, time-based)       │  │
│  │     - Retraining data selection (sliding window)              │  │
│  │     - A/B testing for new model rollout                       │  │
│  │  • Feedback Loop Integration                                  │  │
│  │     - User interaction tracking (clicks, purchases, returns)  │  │
│  │     - Implicit feedback signals (dwell time, bounce rate)     │  │
│  │     - Incremental model updates                               │  │
│  └──────────────────────────────────────────────────────────────┘  │
│                                                                       │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │              3C. ETHICAL AI MONITOR                           │  │
│  ├──────────────────────────────────────────────────────────────┤  │
│  │  • Bias Detection (Fairlearn / AIF360)                        │  │
│  │  • Fairness Metrics:                                          │  │
│  │     - Demographic Parity                                      │  │
│  │     - Equal Opportunity                                       │  │
│  │     - Disparate Impact                                        │  │
│  │  • Bias Mitigation (pre/in/post-processing)                   │  │
│  │  • EU AI Act Compliance Mapper                                │  │
│  │     - Transparency requirements checklist                     │  │
│  │     - Accountability trail (decision logs)                    │  │
│  │     - Auto-generated compliance report (PDF)                  │  │
│  └──────────────────────────────────────────────────────────────┘  │
│                                                                       │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │          3D. BUSINESS IMPACT MEASUREMENT ENGINE               │  │
│  ├──────────────────────────────────────────────────────────────┤  │
│  │  • Real-Time Data Collection:                                 │  │
│  │     - Event streaming (FastAPI webhooks)                      │  │
│  │     - User interaction logging (PostgreSQL)                   │  │
│  │     - A/B test result tracking                                │  │
│  │  • XAI → Business KPI Mapping                                 │  │
│  │  • Business Metrics Dashboard:                                │  │
│  │     - ROI (Return on Investment)                              │  │
│  │     - Churn Reduction Rate                                    │  │
│  │     - Revenue Impact (uplift vs. baseline)                    │  │
│  │     - Customer Satisfaction (CSAT / NPS)                      │  │
│  └──────────────────────────────────────────────────────────────┘  │
│                                                                       │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │        3E. CROSS-DOMAIN TRANSFER ENGINE                       │  │
│  ├──────────────────────────────────────────────────────────────┤  │
│  │  • Transfer Learning Models (Neural Collaborative Filtering)  │  │
│  │  • Explanation Knowledge Mapping                              │  │
│  │  • Multi-Domain Knowledge Graphs                              │  │
│  │  • Cross-Domain Fairness Validation                           │  │
│  └──────────────────────────────────────────────────────────────┘  │
└────────────────────────────┬────────────────────────────────────────┘
                             │
┌────────────────────────────▼────────────────────────────────────────┐
│              LAYER 4: MODEL & DATA INFRASTRUCTURE                    │
├─────────────────────────────────────────────────────────────────────┤
│  • ML Models: LightGBM / XGBoost (production-grade)                  │
│  • Experiment Tracking: MLflow (versioning, registry)                │
│  • Database: PostgreSQL (metadata, logs, interactions)               │
│  • API: FastAPI (RESTful endpoints)                                  │
│  • Deployment: Docker + Docker Compose                               │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Comparison with Existing Solutions

| Capability | CDARS (2025) | Clerk.io | Traditional RecSys | XAE-Frame |
|-----------|--------------|----------|-------------------|-----------|
| Cross-Domain Transfer | Yes | No | No | Yes |
| Explainability | Yes | Limited | No | **NIST-Compliant** |
| Adaptive Learning | Yes | Basic | No | **Automated Retraining** |
| Bias Detection | No | No | No | Yes |
| Knowledge Limits | No | No | No | **Yes** |
| Explanation Transfer | No | No | No | **Yes** |
| Context-Aware Explanations | No | No | No | **Yes** |
| Fairness Across Domains | No | No | No | **Yes** |
| EU AI Act Compliance | No | Not specified | No | **Full Compliance** |
| Business Impact Tracking | Partial | Basic analytics | No | **Real-time KPI Mapping** |

**Key differentiators**: XAE-Frame is the first framework to:
1. Transfer both user preferences AND explanatory logic across domains
2. Implement full NIST Four Principles compliance
3. Provide automated retraining with feedback loops
4. Map technical XAI metrics directly to business KPIs

---

## Technology Stack

**Machine Learning & AI**
- Python 3.9+, Scikit-learn 1.3+, LightGBM 4.0+, XGBoost 2.0+
- SHAP 0.43+ (explainability), Fairlearn 0.9+ (ethics)
- Alibi-Detect 0.12+ (drift detection)

**Data & Infrastructure**
- Pandas 2.0+, NumPy 1.24+, PyArrow (Parquet support)
- PostgreSQL (database), SQLAlchemy 2.0+ (ORM)
- MLflow 2.8+ (experiment tracking)

**API & Interface**
- FastAPI 0.104+ (REST API), Uvicorn (ASGI server)
- Streamlit 1.28+ (dashboard), Plotly 5.17+ (visualizations)

**Development & Deployment**
- Docker + Docker Compose
- pytest (testing), black/flake8 (code quality)
- Git/GitHub

---

## Dataset

The framework uses the [Amazon Reviews 2023](https://amazon-reviews-2023.github.io/) dataset from McAuley Lab at UC San Diego:

- **571.54 million customer reviews** (245% larger than previous versions)
- **33 product categories** spanning multiple business domains
- **Time range**: May 1996 to September 2023
- **Rich metadata**: product descriptions, prices, images, user behavior patterns
- **Standard splits**: Pre-defined train/validation/test for reproducibility

**Selected domains for development:**
- **E-Commerce (Primary Demo)**: All_Beauty (701K reviews), Electronics (43.9M reviews)
- **Finance (Adaptation)**: Synthetic credit card transactions + Kaggle datasets
- **Insurance (Adaptation)**: Synthetic policy data + Kaggle safe driver prediction

---

## Installation & Setup

**Prerequisites:** Python 3.9+, Git, Docker (optional but recommended)

### Option 1: Quick Start with Docker (Recommended)

```bash
# Clone repository
git clone https://github.com/nazliozgur/xae-frame.git
cd xae-frame

# Copy environment template
cp .env.example .env
# Edit .env with your settings (optional for development)

# Start all services (API, Dashboard, PostgreSQL, MLflow)
docker-compose up --build

# Access services:
# - API: http://localhost:8000
# - Dashboard: http://localhost:8501
# - MLflow UI: http://localhost:5000
```

### Option 2: Manual Installation

```bash
# Clone repository
git clone https://github.com/nazliozgur/xae-frame.git
cd xae-frame

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Download dataset (sample for quick start)
python scripts/download_data.py --dataset amazon_reviews --category All_Beauty --sample-size 10000

# Initialize database
python scripts/init_db.py

# Run preprocessing
python src/data/preprocess.py --config configs/e_commerce.yaml

# Train baseline model
python src/models/train.py --config configs/e_commerce.yaml

# Start API server
uvicorn src.api.main:app --reload --port 8000

# Start dashboard (new terminal)
streamlit run src/dashboard/app.py
```

**Run Jupyter notebooks:**
```bash
jupyter lab
```

---

## Project Structure

```
xae-frame/
├── README.md                          # This file
├── requirements.txt                   # Python dependencies
├── requirements-dev.txt               # Development tools
├── requirements-prod.txt              # Production minimal
├── docker-compose.yml                 # Multi-container setup
├── Dockerfile                         # Container definition
├── .env.example                       # Environment template
├── .gitignore                         # Git ignore patterns
│
├── configs/                           # Configuration files
│   ├── e_commerce.yaml
│   ├── finance.yaml
│   └── insurance.yaml
│
├── data/                              # Data directory (gitignored)
│   ├── raw/                           # Original datasets
│   ├── processed/                     # Cleaned data
│   └── models/                        # Saved model artifacts
│
├── notebooks/                         # Jupyter notebooks
│   ├── 01_eda.ipynb                   # Exploratory analysis
│   ├── 02_baseline.ipynb              # Baseline experiments
│   ├── 03_xai_analysis.ipynb          # SHAP analysis
│   └── 04_fairness.ipynb              # Bias detection
│
├── src/                               # Source code
│   ├── data/                          # Data processing
│   │   ├── download.py
│   │   ├── preprocess.py
│   │   └── feature_engineering.py
│   │
│   ├── models/                        # Model training
│   │   ├── train.py
│   │   ├── predict.py
│   │   └── evaluate.py
│   │
│   ├── explainability/                # XAI engine
│   │   ├── shap_explainer.py
│   │   ├── explanation_accuracy.py
│   │   ├── knowledge_limits.py
│   │   └── multi_level_explanations.py
│   │
│   ├── adaptive/                      # Adaptive learning
│   │   ├── drift_detection.py
│   │   ├── retraining_strategy.py
│   │   └── feedback_loop.py
│   │
│   ├── ethical/                       # Fairness & compliance
│   │   ├── bias_detection.py
│   │   ├── bias_mitigation.py
│   │   └── eu_ai_act_compliance.py
│   │
│   ├── business_impact/               # Business metrics
│   │   ├── metric_mapping.py
│   │   ├── real_time_collector.py
│   │   └── roi_calculator.py
│   │
│   ├── transfer_learning/             # Cross-domain
│   │   ├── transfer_models.py
│   │   └── explanation_transfer.py
│   │
│   ├── api/                           # FastAPI application
│   │   ├── main.py
│   │   ├── routes/
│   │   └── schemas.py
│   │
│   ├── dashboard/                     # Streamlit UI
│   │   ├── app.py
│   │   └── views/
│   │
│   └── utils/                         # Utilities
│
├── scripts/                           # Standalone scripts
│   ├── download_data.py
│   └── init_db.py
│
├── tests/                             # Unit and integration tests
│
└── docs/                              # Documentation
    ├── architecture.md
    ├── nist_compliance.md
    └── deployment.md
```

---

## Novel Contributions

This work introduces three methodological innovations to cross-domain recommendation systems:

**1. Explanation Knowledge Transfer**

Traditional cross-domain systems transfer user-item interaction patterns but lose the semantic reasoning behind preferences. XAE-Frame preserves and transfers explanation patterns across domains.

Example: A user who prefers "award-winning" books (indicating quality focus) receives recommendations for "premium" financial products with explanations tied to the same underlying quality preference, even though the feature spaces are different.

**2. NIST-Compliant Adaptive Explanation Generation**

Rather than providing uniform SHAP-based explanations, the system implements all four NIST principles with adaptive complexity:

- **Explanation**: SHAP values for every prediction
- **Meaningful**: Role-based views (technical deep-dive vs. business summary)
- **Explanation Accuracy**: Fidelity metrics ensure truthfulness
- **Knowledge Limits**: Confidence thresholds prevent unreliable predictions

**3. Cross-Domain Fairness Monitoring with Automated Retraining**

First systematic approach to detect bias propagation in cross-domain transfers while maintaining model accuracy through automated retraining strategies. The system monitors whether explanation quality and recommendation fairness remain consistent across demographic groups when knowledge transfers between domains, and triggers retraining when drift is detected.

---

## Development Roadmap

**Phase 1: Foundation** (Weeks 1-2)
- ✅ Project infrastructure and repository setup
- ✅ Dataset acquisition (Amazon Reviews 2023)
- ✅ Data preprocessing pipeline
- ✅ Baseline recommendation models

**Phase 2: Core Engines** (Weeks 3-4)
- 🔄 XAI engine (SHAP integration)
- 🔄 Drift detection (Alibi Detect)
- 🔄 Fairness monitoring (Fairlearn)
- 🔄 Knowledge Limits module

**Phase 3: Advanced Features** (Week 5)
- ⏳ Automated retraining strategy
- ⏳ Feedback loop integration
- ⏳ Business impact measurement
- ⏳ EU AI Act compliance mapper

**Phase 4: Cross-Domain & Integration** (Weeks 6-7)
- ⏳ Transfer learning implementation
- ⏳ Explanation knowledge transfer
- ⏳ Finance & insurance adaptations
- ⏳ Multi-view dashboard

**Phase 5: Finalization** (Week 8)
- ⏳ REST API development
- ⏳ Docker containerization
- ⏳ Technical documentation
- ⏳ Thesis writing

**Target Completion**: January 15, 2025

---

## Key References

**Standards & Frameworks**
- Phillips, P.J., et al. (2020). *Four Principles of Explainable Artificial Intelligence*. NIST IR 8312. [Link](https://www.nist.gov/publications/four-principles-explainable-artificial-intelligence)
- European Commission (2024). *EU Artificial Intelligence Act*. [Link](https://artificialintelligenceact.eu/)

**Cross-Domain Recommendation**
- Petruzzelli, A., et al. (2024). Instructing and Prompting Large Language Models for Explainable Cross-Domain Recommendations. ACM RecSys '24.
- Hou, Y., et al. (2024). Bridging Language and Items for Retrieval and Recommendation. arXiv:2403.03952.

**Explainable AI**
- Lundberg, S.M., & Lee, S.I. (2017). *A Unified Approach to Interpreting Model Predictions*. NeurIPS.
- McKinsey (2022). *Why Businesses Need Explainable AI—and How to Deliver It*. [Link](https://www.mckinsey.com/capabilities/quantumblack/our-insights/why-businesses-need-explainable-ai-and-how-to-deliver-it)

**Dataset**
- McAuley Lab (2023). *Amazon Reviews 2023*. [Link](https://amazon-reviews-2023.github.io/)

Full bibliography available in `docs/references.md`

---

## Use Cases

**E-Commerce**
Product recommendations with transparent reasoning, real-time adaptation to browsing patterns, and personalized explanation delivery based on user sophistication.

**Financial Services**
Credit product recommendations with regulatory-compliant explanations, bias-free scoring models, and cross-sell opportunities based on behavior patterns from other domains.

**Insurance**
Policy recommendations with risk factor explanations, fair pricing across demographic groups, and coverage suggestions informed by purchasing behavior in adjacent domains.

---

## Contributing

This is a Master's thesis project at Istanbul University. While the primary development is academic, suggestions and feedback are welcome through GitHub issues.

**For partnership or licensing inquiries**, please reach out via email.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## Contact

**Nazlı Özgür**  
🎓 M.Sc. Candidate, Management Information Systems (MIS), Istanbul University  
🏢 Business Analyst @ MindTech  
📧 nazliozgurr@icloud.com  
🔗 [LinkedIn](https://www.linkedin.com/in/nazliozgurr/) | [GitHub](https://github.com/nazliozgur)

---

*This project constitutes the final thesis for the Master of Science program in Management Information Systems at Istanbul University.*

---

## Acknowledgments

- **NIST** for the foundational XAI principles framework
- **McKinsey QuantumBlack** for industry insights on XAI business value
- **McAuley Lab (UC San Diego)** for the Amazon Reviews 2023 dataset
- **MindTech** for real-world problem context from fintech, insurance, and telecom sectors
- **Istanbul University** for academic support

---

**Designed for transparency, built for adaptability, validated for fairness.**
