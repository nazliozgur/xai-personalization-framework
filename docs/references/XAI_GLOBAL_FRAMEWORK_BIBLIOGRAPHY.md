# XAE-FRAME: GLOBAL XAI FRAMEWORK SOURCES
# Comprehensive Bibliography for World-Class EDA & Project

##  PRIMARY FRAMEWORKS & STANDARDS

### 1. **NIST AI Framework** 
- **NIST IR 8312** - Four Principles of Explainable AI (2021)
  * Explanation
  * Meaningful
  * Explanation Accuracy
  * Knowledge Limits
- **Citation:** Phillips, P. J., et al. (2021). Four Principles of Explainable Artificial Intelligence. NIST Interagency Report 8312.
- **URL:** https://www.nist.gov/publications/four-principles-explainable-artificial-intelligence
- **Use in Project:** Foundation for XAI module design

### 2. **DARPA XAI Program** 
- **Gunning & Aha (2019)** - DARPA's Explainable AI Program
- **Key Concepts:**
  * Performance vs. Explainability trade-off
  * User-centric explanation evaluation
  * Psychological model of explanation
  * Trust calibration
- **Citation:** Gunning, D., & Aha, D. (2019). DARPA's explainable artificial intelligence (XAI) program. AI Magazine, 40(2), 44-58.
- **Retrospective:** Gunning & Vorm (2021) - Lessons learned 2017-2021
- **Use in Project:** Explanation interface design, evaluation metrics

### 3. **EU AI Act** 
- **Regulation (EU) 2024/1689** - AI Act (June 2024)
- **Key Requirements:**
  * High-risk AI transparency
  * Documentation obligations
  * Human oversight
  * Bias monitoring
- **Citation:** European Parliament & Council. (2024). Regulation on Artificial Intelligence (AI Act).
- **URL:** https://artificialintelligenceact.eu/
- **Use in Project:** Compliance module, audit trails

### 4. **McKinsey AI Value Framework** 
- **Bughin et al. (2022)** - Notes from the AI frontier
- **Key Metrics:**
  * 20%+ EBIT from AI in leading firms
  * Digital trust → 10%+ revenue growth
  * XAI critical for scaling
- **Citation:** McKinsey Global Institute. (2022). The state of AI in 2022.
- **Use in Project:** Business impact measurement, ROI framework

---

##  ACADEMIC CONFERENCES & PUBLICATIONS

### 5. **World Conference on XAI** (xAI 2024, Malta)
- **Springer CCIS** - 95 papers, 204 submissions
- **Topics:**
  * Counterfactual explanations
  * Fairness, trust, privacy
  * Healthcare applications
  * Human-computer interaction
- **Editors:** Longo, Lapuschkin, Seifert (2024)
- **Use in Project:** Latest XAI techniques, benchmarks

### 6. **EXPLAINS 2024** - Neural & Symbolic Methods
- **Special Focus:** Online behavior, radicalization detection
- **Indexed:** SCOPUS, Web of Science, DBLP
- **Use in Project:** Text bias detection methods

### 7. **ACM RecSys** - Recommendation Systems
- **Top Conference:** Explainable recommendations
- **Key Papers:**
  * User-centric explanations
  * Transparency in RecSys
  * Cold-start solutions
- **Use in Project:** Cross-domain recommendation baseline

---

##  KEY RESEARCH PAPERS (2018-2024)

### 8. **SHAP (Lundberg & Lee, 2017)** 
- **Title:** A Unified Approach to Interpreting Model Predictions
- **Conference:** NeurIPS 2017
- **Citation:** Lundberg, S. M., & Lee, S. I. (2017). A unified approach to interpreting model predictions. Advances in neural information processing systems, 30.
- **Use in Project:** Primary explainability engine

### 9. **LIME (Ribeiro et al., 2016)** 
- **Title:** "Why Should I Trust You?" Explaining Predictions
- **Conference:** KDD 2016
- **Citation:** Ribeiro, M. T., Singh, S., & Guestrin, C. (2016). "Why should I trust you?" Explaining the predictions of any classifier. KDD.
- **Use in Project:** Model-agnostic explanations

### 10. **Fairlearn & AIF360**
- **Microsoft Fairlearn** (Bird et al., 2020)
- **IBM AIF360** (Bellamy et al., 2018)
- **Use in Project:** Bias detection & mitigation

### 11. **Alibi Detect (Klaise et al., 2020)**
- **Seldon Technologies** - Open-source drift detection
- **Methods:** Kolmogorov-Smirnov, MMD, Chi-Square
- **Use in Project:** Adaptive learning, drift detection

### 12. **Exploring XAI Landscape (MDPI 2024)**
- **Authors:** Big Data & Cognitive Computing
- **Systematic Review:** 53 papers (2018-2024)
- **Key Findings:**
  * Healthcare XAI applications
  * Interpretability vs performance
  * User trust factors
- **Use in Project:** Literature review section

---

##  REGULATORY & ETHICAL FRAMEWORKS

### 13. **IEEE Ethics in AI**
- **Ethically Aligned Design** (2019)
- **Principles:** Transparency, accountability, bias awareness
- **Use in Project:** Ethical AI monitor design

### 14. **OECD AI Principles** (2019)
- **Five Principles:**
  * Inclusive growth
  * Human-centered values
  * Transparency
  * Robustness
  * Accountability
- **Use in Project:** Compliance checklist

### 15. **ISO/IEC 42001:2023** - AI Management System
- **New Standard:** AI governance & risk management
- **Use in Project:** Enterprise deployment guidelines

### 16. **MODEL REPORTING & TRANSPARENCY STANDARDS**

###  **Model Cards for Model Reporting**
- **Mitchell, M., et al. (2019)** - Model Cards for Model Reporting  
  Paper: https://arxiv.org/abs/1810.03993  
  Published: ACM FAT* 2019 (Fairness, Accountability, and Transparency)
  
- **Google Research (2019)** - Model Card Toolkit  
  GitHub: https://github.com/tensorflow/model-card-toolkit  
  Documentation: https://modelcards.withgoogle.com
  
- **Hugging Face (2022)** - Model Card Guidelines  
  Docs: https://huggingface.co/docs/hub/model-cards  
  Template: https://github.com/huggingface/huggingface_hub/blob/main/src/huggingface_hub/templates/modelcard_template.md

- **IBM AI Factsheets (2020)** - Supplier's Declaration of Conformity  
  Related to Model Cards but more comprehensive (360-degree view)

**Use in Project:**
- EU AI Act Article 13 (Technical Documentation)
- Transparency template for each model version
- Automated compliance report generation
- Model registry metadata (MLflow integration)

**Why Critical for XAE-Frame:**
1. **Industry Standard**: Google, Hugging Face, OpenAI all use Model Cards
2. **EU AI Act Alignment**: Article 13 requires technical documentation
3. **Template Ready**: Can generate Model Cards automatically from MLflow
4. **Thesis Defense**: "We follow Google's Model Card standard"

---

##  DOMAIN-SPECIFIC XAI

### 17. **Healthcare XAI**
- **Holzinger et al. (2019)** - Causability in Medical AI
- **Focus:** Doctor-patient explanation needs
- **Use in Project:** Multi-audience explanation design

### 18. **Financial XAI**
- **Bussmann et al. (2021)** - Explainable AI in Fintech
- **Regulations:** MiFID II, FCRA
- **Use in Project:** Finance domain adaptation

### 19. **E-Commerce RecSys**
- **Hou et al. (2024)** - Bridging Language and Items for Retrieval
  * arXiv:2403.03952
  * LLM-based recommendations
- **Use in Project:** Text-based feature engineering

---

##  EDA-SPECIFIC METHODOLOGIES

### 20. **Exploratory Data Analysis (Tukey, 1977)**
- **Classic Reference:** Exploratory Data Analysis
- **Principles:** Visual thinking, robust statistics
- **Use in Project:** EDA philosophy

### 21. **Statistical Methods for ML (Hastie et al., 2009)**
- **The Elements of Statistical Learning**
- **Topics:** Bias-variance, cross-validation, feature selection
- **Use in Project:** Statistical rigor in EDA

### 22. **Data Quality Assessment (Batini & Scannapieco, 2016)**
- **Principles:** Completeness, accuracy, consistency, timeliness
- **Use in Project:** Data trustworthiness assessment

---

##  VISUALIZATION & REPORTING

### 23. **Matplotlib/Seaborn Best Practices**
- **Waskom (2021)** - Seaborn: Statistical data visualization
- **Use in Project:** Publication-quality figures

### 24. **Plotly for Interactive XAI**
- **Plotly Technologies** - Dash for ML
- **Use in Project:** Interactive dashboards

### 25. **3D Visualization (Matplotlib 3D)**
- **Hunter (2007)** - Matplotlib: A 2D graphics environment
- **Extension:** mplot3d for 3D scatter/surface
- **Use in Project:** High-dimensional feature space visualization

---

##  BUSINESS IMPACT MEASUREMENT

### 26. **A/B Testing Methodology**
- **Kohavi & Longbotham (2017)** - Online Controlled Experiments
- **Use in Project:** Business impact validation

### 27. **Customer Lifetime Value (CLV)**
- **Gupta & Lehmann (2005)** - Managing Customers as Investments
- **Use in Project:** Revenue impact estimation

---

##  THESIS-SPECIFIC CITATIONS

### 28. **Cross-Domain Recommendation**
- **Cantador et al. (2015)** - Cross-domain recommender systems
- **Use in Project:** Transfer learning methodology

### 29. **Explainable Recommendation Systems**
- **Zhang & Chen (2020)** - Explainable Recommendation: A Survey
- **Citation:** ACM Computing Surveys
- **Use in Project:** Literature review

### 30. **Adaptive Learning Systems**
- **Gama et al. (2014)** - A Survey on Concept Drift Adaptation
- **Citation:** ACM Computing Surveys
- **Use in Project:** Drift detection methodology

---

##  ADDITIONS v3.5

### 31. **Redis for ML Feature Store**
- **Redis Labs (2023)** - Redis as a Feature Store
  * URL: https://redis.io/docs/manual/patterns/
- **Feast.dev (2023)** - Feature Store Best Practices
  * URL: https://www.featurestore.org
- **Tecton (2022)** - Building a Feature Store
  * Blog: Uber Engineering
- **Use in Project:** Real-time personalization layer (<100ms latency)

---

### 32. **Behavior Drift Detection**
- **Rabanser et al. (2019)** - Failing Loudly: An Empirical Study of Methods for Detecting Dataset Shift
  * Conference: NeurIPS 2019
- **Lu et al. (2018)** - Learning under Concept Drift: A Review
  * Journal: IEEE TKDE
- **Bifet & Gavaldà (2007)** - Learning from Time-Changing Data with Adaptive Windowing
  * Conference: SIAM SDM
- **Use in Project:** CTR/Conversion drift detection, KS-test implementation

---

### 33. **Champion/Challenger A/B Testing**
- **Kohavi et al. (2020)** - Trustworthy Online Controlled Experiments: A Practical Guide
  * Publisher: Cambridge University Press
- **Bakshy et al. (2014)** - Designing and Deploying Online Field Experiments
  * Conference: WWW 2014
- **Netflix (2019)** - Experimentation Platform
  * Tech Blog: Netflix TechBlog
- **Use in Project:** Auto-retraining engine, model rollout strategy

---

### 34. **MLOps & Model Retraining**
- **Paleyes et al. (2022)** - Challenges in Deploying Machine Learning (Cambridge)
  * Journal: ACM Computing Surveys
- **Sculley et al. (2015)** - Hidden Technical Debt in Machine Learning Systems (Google)
  * Conference: NeurIPS 2015
- **Breck et al. (2017)** - The ML Test Score (Google)
  * Conference: NeurIPS 2017
- **MLflow (2024)** - Model Registry & Versioning Best Practices
  * Docs: https://mlflow.org/docs/latest/model-registry.html
- **Use in Project:** Automated retraining pipeline, MLflow integration

---

### 35. **Immutable Audit Logs (Blockchain-Inspired)**
- **Szabo (1997)** - The Idea of Smart Contracts (Blockchain foundations)
  * Original paper
- **Nakamoto (2008)** - Bitcoin: A Peer-to-Peer Electronic Cash System
  * Whitepaper
- **Hyperledger (2020)** - Blockchain for Enterprise Applications
  * Documentation
- **Use in Project:** Hash-chain audit trail, tamper-proof decision logs

---

### 36. **EU AI Act Technical Implementation**
- **EU Commission (2024)** - AI Act Official Text
  * URL: https://artificialintelligenceact.eu/
- **EU AI Act (2024)** - Article 12: Logging (Technical Requirements)
- **EU AI Act (2024)** - Article 13: Transparency & Explainability
- **EU AI Act (2024)** - Article 15: Accuracy, Robustness, Cybersecurity
- **ISO/IEC 23894 (2023)** - AI Risk Management
- **Use in Project:** Regulation pack implementation, compliance reporting

---

### 37. **Cardinality & Feature Engineering**
- **Micci-Barreca (2001)** - A Preprocessing Scheme for High-Cardinality Categorical Attributes
  * Conference: SIGKDD Explorations
- **Cerda & Varoquaux (2019)** - Encoding High-Cardinality String Categorical Variables
  * Journal: IEEE TPAMI
- **Use in Project:** High-cardinality feature handling (brands, categories)

---

##  NOVEL CONTRIBUTIONS (For Citation in Thesis)

### OUR WORK: XAE-Frame
1. **Explanation Knowledge Transfer** (Novel)
   - First framework to transfer semantic explanations across domains
   - Cite as: "Özgür, N. (2025). XAE-Frame: Explainable, Adaptive, and Ethical AI Framework for Cross-Domain Personalization."

2. **NIST-Compliant Adaptive Explanations** (Novel)
   - Automated retraining + explanation recalibration
   - Integrates all 4 NIST principles

3. **Cross-Domain Fairness Monitoring** (Novel)
   - Tracks bias propagation during transfer learning
   - EU AI Act compliant by design

---

##  CITATION FORMAT FOR THESIS

**McKinsey + NIST + DARPA + EU AI Act + xAI 2024 + Our Work**

Example paragraph:
"Following NIST's four principles of XAI (Phillips et al., 2021) and DARPA's user-centric evaluation framework (Gunning & Aha, 2019), we design explanation interfaces that comply with EU AI Act transparency requirements (EU Regulation 2024/1689). Our approach integrates SHAP (Lundberg & Lee, 2017) for local explanations and Alibi Detect (Klaise et al., 2020) for drift monitoring, validated using McKinsey's business impact framework (McKinsey, 2022). This methodology, presented at xAI 2024 conference standards, contributes three novel components to the XAI literature..."

---

##  SUMMARY

**EDA Section:**
1. NIST IR 8312 → Knowledge limits baseline
2. DARPA XAI → Explanation evaluation
3. EU AI Act → Fairness audit
4. McKinsey → Business value mapping
5. xAI 2024 papers → Latest techniques
6. Tukey (1977) → EDA philosophy
7. Batini & Scannapieco → Data quality

**For All Sections:**
- **Data Trustworthiness** → NIST Principle 4
- **Fairness** → EU AI Act + Fairlearn
- **Temporal Drift** → Alibi Detect + Gama et al.
- **Explainability** → DARPA framework + SHAP
- **Business Value** → McKinsey + CLV literature

---

##  PROFESSIONAL SOURCE CITATION (FOR NOTEBOOKS)

When starting any analysis or module (e.g., 01_eda.ipynb, feature_engineering.py), use the following structure to ensure transparency and reproducibility:

```markdown
## Section X: Analysis Name

**Theoretical Foundation:**
This analysis follows [NIST IR 8312]'s Knowledge Limits principle 
and [DARPA XAI]'s user trust framework, ensuring our model abstains 
from predictions when confidence is below established thresholds.

**Regulatory Compliance:**
Per [EU AI Act Article 13], we document baseline fairness metrics 
before model training to enable transparent audit trails.

**Practical Implementation:**
Using [Alibi Detect] for out-of-distribution detection, we establish
confidence calibration following [Guo et al. 2017] methodology.

**Business Relevance:**
As demonstrated by [McKinsey 2022], transparent AI systems achieve
10%+ higher customer trust, directly impacting conversion rates.
```




