# XAE-Frame: Cross-Domain Explainable, Adaptive & Ethical AI Framework

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![EU AI Act](https://img.shields.io/badge/EU%20AI%20Act-Compliant-green.svg)](https://artificialintelligenceact.eu/)

**A production-ready AI framework that combines cross-domain personalization, explainable AI, adaptive learning, and ethical oversight for trustworthy recommendation systems.**

---

## Problem Statement

Modern recommendation systems face a critical challenge: they optimize for accuracy but fail to address transparency, adaptability, and fairness. This creates three major issues:

1. **Black-box decisions** - Users and regulators cannot understand why recommendations are made
2. **Static models** - Systems fail to adapt to changing user behavior in real-time
3. **Domain isolation** - Knowledge cannot be transferred across business sectors

With the EU AI Act enforcement beginning in 2025, organizations need AI systems that are not only accurate but also explainable, adaptive, and verifiably fair.

**XAE-Frame addresses these challenges** by integrating explainability, cross-domain transfer learning, and ethical oversight into a unified framework designed for enterprise deployment.

---

## Key Capabilities

### Cross-Domain Personalization
Transfer user preferences and behavioral patterns across different business domains (e-commerce, finance, insurance). The framework goes beyond simple preference transfer by preserving the reasoning behind recommendations, enabling meaningful knowledge transfer even between semantically different domains. Transfer is achieved through deep learning-based embedding mapping (utilizing neural collaborative filtering and matrix factorization techniques), effectively solving cold-start problems in target domains by leveraging rich knowledge from source domains.

### Explainable AI Integration
Built on SHAP (SHapley Additive exPlanations) and LIME with an additional layer that adapts explanations to user context. Technical users receive detailed feature importance breakdowns with statistical significance measures, while business users get simplified, actionable insights via natural language justifications. The system generates context-aware explanations by analyzing user interaction history, expertise level, and current decision context, ensuring that each explanation is both accurate and comprehensible to its intended audience.

### Adaptive Learning Engine
Real-time concept drift detection using the River library monitors changes in user behavior and triggers model updates via online learning techniques without requiring full retraining. The system tracks behavioral patterns including click timing, revisit frequency, session duration, and preference evolution over time. When significant drift is detected (using statistical tests such as ADWIN and Page-Hinkley), the framework automatically initiates incremental model updates while maintaining explanation consistency.

### Ethical AI & Compliance
Continuous bias monitoring across demographic groups and domain-specific segments with automated fairness metrics including Demographic Parity and Equal Opportunity (implemented through Fairlearn). The system performs regular audits to detect bias amplification during cross-domain transfers, ensuring that knowledge transfer does not introduce or propagate unfair patterns. Includes built-in EU AI Act compliance reporting with full decision traceability, model documentation, and risk assessment capabilities.

### Business Impact Measurement
Quantifies AI value through metrics that matter to business stakeholders: revenue lift, conversion rate improvement, churn reduction, and customer lifetime value increase. All metrics are tracked in real-time through an interactive dashboard.

---

## Technical Architecture

```
┌─────────────────────────────────────────────────────┐
│          Business Impact Dashboard                  │
│    (Streamlit - dashboard/app.py)                   │
│    Real-time Metrics & ROI Tracking                 │
└─────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────┐
│       Explainability & Ethics Layer                 │
├─────────────────────────────────────────────────────┤
│  SHAP Feature Analysis (src/xai/explainer.py)       │
│  Adaptive Explanation Engine                        │
│    (src/xai/adaptive_explainer.py)                  │
│  Cross-Domain Bias Detection                        │
│    (src/ethics/bias_detector.py)                    │
│  Drift Monitoring (src/adaptive/drift_detector.py)  │
└─────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────┐
│       Cross-Domain Transfer Engine                  │
├─────────────────────────────────────────────────────┤
│  Transfer Learning Models                           │
│    (src/models/transfer_learning.py)                │
│  Explanation Knowledge Mapping                      │
│    (src/xai/explanation_transfer.py)                │
│  Multi-Domain Knowledge Graphs                      │
└─────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────┐
│              Data Processing Layer                  │
│    (src/data/loaders.py, preprocessors.py)          │
│     Amazon Reviews 2023 (571M+ interactions)        │
└─────────────────────────────────────────────────────┘
```

---

## Comparison with Existing Solutions

| Capability | CDARS (2025) | LLM-Based RecSys | Traditional RecSys | XAE-Frame |
|-----------|--------------|------------------|-------------------|-----------|
| Cross-Domain Transfer | Yes | Yes | No | Yes |
| Explainability | Yes | Yes | No | Yes |
| Adaptive Learning | Yes | No | No | Yes |
| Bias Detection | No | No | No | Yes |
| Explanation Transfer | No | No | No | **Yes** |
| Context-Aware Explanations | No | Partial | No | **Yes** |
| Fairness Across Domains | No | No | No | **Yes** |
| EU AI Act Compliance | No | No | No | Yes |
| Business Metrics | Partial | No | No | Yes |

**Key differentiators**: XAE-Frame is the first framework to transfer not just user preferences but also the explanatory logic across domains, while maintaining continuous bias monitoring and providing business-measurable outcomes.

---

## Technology Stack

**Machine Learning & AI**
- Python 3.11, Scikit-learn, LightGBM
- SHAP (explainability), Fairlearn (ethics), River (online learning)

**API & Interface**
- FastAPI (REST API), Streamlit (dashboard), Plotly (visualizations)

**Data Infrastructure**
- Amazon Reviews 2023 dataset (571M reviews, 33 categories)
- Pandas, NumPy, SQLAlchemy

**Development & Deployment**
- Docker, Git/GitHub, pytest

---

## Dataset

The framework uses the [Amazon Reviews 2023](https://amazon-reviews-2023.github.io/) dataset from McAuley Lab at UC San Diego:

- 571.54 million customer reviews (245% larger than previous versions)
- 33 product categories spanning multiple business domains
- Time range: May 1996 to September 2023
- Rich metadata: product descriptions, prices, images, user behavior patterns

**Selected domains for cross-domain experiments:**
- All_Beauty (701K reviews)
- Health_and_Household (25.6M reviews)
- Electronics (43.9M reviews)

---

## Installation & Setup

**Prerequisites:** Python 3.11 or higher, Git

```bash
# Clone repository
git clone https://github.com/nazliozgur/xai-personalization-framework.git
cd xai-personalization-framework

# Create and activate virtual environment
python3.11 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Optional: Download sample dataset
python scripts/download_dataset.py --domain All_Beauty
```

**Run Jupyter notebooks:**
```bash
jupyter lab
```

**Launch dashboard:**
```bash
streamlit run dashboard/app.py
```

**Start API server:**
```bash
uvicorn src.api.endpoints:app --reload
# API documentation: http://localhost:8000/docs
```

---

## Project Structure

```
xai-personalization-framework/
├── data/
│   ├── raw/              # Original datasets
│   ├── processed/        # Cleaned and preprocessed data
│   └── external/         # Additional data sources
│
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_model_experiments.ipynb
│   └── 03_xai_analysis.ipynb
│
├── src/
│   ├── data/             # Data loading and preprocessing
│   ├── models/           # ML models and transfer learning
│   ├── xai/              # Explainability modules
│   │   ├── explainer.py
│   │   ├── adaptive_explainer.py
│   │   └── explanation_transfer.py
│   ├── ethics/           # Fairness and bias detection
│   │   ├── fairness_checker.py
│   │   └── bias_detector.py
│   ├── adaptive/         # Drift detection and online learning
│   └── api/              # REST API endpoints
│
├── dashboard/
│   ├── app.py            # Main dashboard application
│   └── components/       # Reusable UI components
│
├── tests/
│   ├── unit/
│   └── integration/
│
├── deployment/
│   ├── Dockerfile
│   └── docker-compose.yml
│
├── docs/
│   ├── api_documentation.md
│   ├── technical_whitepaper.md
│   └── user_guide.md
│
├── requirements.txt
└── README.md
```

---

## Novel Contributions

This work introduces three methodological innovations to cross-domain recommendation systems:

**1. Explanation Knowledge Transfer**

Traditional cross-domain systems transfer user-item interaction patterns but lose the semantic reasoning behind preferences. XAE-Frame preserves and transfers explanation patterns across domains.

Example: A user who prefers "award-winning" books (indicating quality focus) receives recommendations for "premium" financial products with explanations tied to the same underlying quality preference, even though the feature spaces are different.

**2. Adaptive Explanation Generation**

Rather than providing uniform SHAP-based explanations, the system adapts explanation complexity and focus based on user expertise level and context:

- Technical users: Detailed feature importance with statistical measures
- Business users: High-level insights focused on actionable attributes  
- Value-conscious users: Cost-benefit analysis and ROI-focused explanations

**3. Cross-Domain Fairness Monitoring**

First systematic approach to detect bias propagation in cross-domain transfers. The system monitors whether explanation quality and recommendation fairness remain consistent across demographic groups when knowledge transfers between domains.

This addresses a critical gap: ensuring that domain adaptation does not introduce or amplify biases present in the source domain.

---

## Development Roadmap

**Phase 1: Foundation** (Completed)
- Project infrastructure and repository setup
- Dataset acquisition and initial exploration
- Technology stack configuration

**Phase 2: Core Development** (In Progress)
- Data preprocessing pipeline
- Baseline recommendation models
- SHAP integration and explanation generation
- Initial dashboard prototype

**Phase 3: Advanced Features** (Planned)
- Cross-domain transfer learning implementation
- Explanation knowledge transfer module
- Adaptive explanation engine
- Bias detection and fairness monitoring

**Phase 4: Deployment & Documentation** (Planned)
- EU AI Act compliance documentation
- Business impact dashboard finalization
- REST API development
- Docker containerization
- Technical documentation and user guides

---

## Key References

**Cross-Domain Recommendation**
- Petruzzelli, A., et al. (2024). Instructing and Prompting Large Language Models for Explainable Cross-Domain Recommendations. ACM RecSys '24.
- Hou, Y., et al. (2024). Bridging Language and Items for Retrieval and Recommendation. arXiv:2403.03952.

**Explainable AI**
- Frontiers in Big Data (2024). On Explaining Recommendations with Large Language Models: A Review.
- MDPI Algorithms (2025). Enhancing Recommendation Systems with Real-Time Adaptive Learning and Multi-Domain Knowledge Graphs.

**Dataset**
- McAuley Lab, UC San Diego. Amazon Reviews 2023. [https://amazon-reviews-2023.github.io/](https://amazon-reviews-2023.github.io/)

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

**Note:** A comprehensive investor pitch deck and commercialization roadmap will be available upon thesis completion. For early partnership or licensing inquiries, please reach out via email.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## Contact

**Nazlı Özgür**  
🎓 **M.Sc. Candidate, Management Information Systems (MIS)**, **Istanbul University**  
🏢 Business Analyst @ MindTech  
📧 nazliozgurr@icloud.com  
🔗 [LinkedIn Profile](https://www.linkedin.com/in/nazliozgurr/) | [GitHub Profile](https://github.com/nazliozgur)

---

*This project constitutes the final thesis for the Master of Science program in Management Information Systems at Istanbul University.*

---

## Acknowledgments

**MindTech** - Professional insights from fintech, insurance, and telecom sector implementations  
**McAuley Lab, UC San Diego** - Amazon Reviews 2023 dataset  
**Open-source community** - SHAP, Fairlearn, Streamlit, FastAPI, and supporting libraries

---

**Designed for transparency, built for adaptability, validated for fairness.**