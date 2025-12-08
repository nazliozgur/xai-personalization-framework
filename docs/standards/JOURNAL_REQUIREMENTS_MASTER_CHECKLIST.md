#  XAE-FRAME: INTERNATIONAL JOURNAL REQUIREMENTS MASTER CHECKLIST

**Purpose:** Ensure all project phases meet top-tier journal publication standards  
**Last Updated:** December 2025  
**Applies To:** EDA, Preprocessing, Feature Engineering, Modeling, XAI, Deployment

---

##  TARGET JOURNALS & IMPACT FACTORS

### **Tier 1 (Nature/Science Level)**
- ✅ **Nature Machine Intelligence** (Impact Factor: ~25.9)
- ✅ **Management Science (INFORMS)** (IF: ~5.4)
- ✅ **MIT Technology Review** (Prestige publication)

### **Tier 2 (Top CS/AI Conferences)**
- ✅ **NeurIPS** (Top 3 ML conference)
- ✅ **ACM RecSys** (Top recommendation systems)
- ✅ **IEEE TKDE** (IF: ~8.9)

### **Tier 3 (Specialized High-Impact)**
- ✅ **ACM Computing Surveys** (IF: ~16.6)
- ✅ **Information Fusion (Elsevier)** (IF: ~18.6)
- ✅ **Expert Systems With Applications (ESWA)** (IF: ~8.5)
- ✅ **Towards Data Science (TDS)** (Community standard)
- ✅ **Journal of Intelligent & Fuzzy Systems** (IF: ~2.0)

---

##  CRITICAL REQUIREMENTS (ALL JOURNALS)

### **1. VISUALIZATION STANDARDS**

#### **Nature Machine Intelligence Requirements:**
```
✅ Color-blind friendly colors MANDATORY
   "Authors are encouraged to consider the needs of colourblind readers"
   ❌ No red-green combinations
   ✅ Use: green-magenta, turquoise-red, yellow-blue, CB_COLORS

✅ Verbal cues in legends
   "Use verbal cues to describe keys, eg. 'open red triangles', not visual cues"
   
✅ Error bars & statistical info
   "Include description of centre values (median/average) and all error bars"
   "Give sample size (n number), state statistical test, provide P values"
   
✅ Contrast ratio ≥4.5:1 for text
   (Accessibility standard)
   
✅ Maximum 6 main figures (Articles)
   Extended Data: max 10 items
   
✅ High resolution
   300+ DPI for raster, vector preferred (SVG/PDF)
```

#### **IEEE TKDE Requirements:**
```
✅ IEEE style figures (clean, professional)
✅ 300 DPI minimum
✅ Vector graphics preferred (EPS, PDF)
✅ Single-column width: 3.5 inches
✅ Double-column width: 7.16 inches
✅ Font size: 8-10pt minimum (readable when scaled)
```

#### **ACM Requirements:**
```
✅ ACM style compliance
✅ Color figures encouraged (online), grayscale-compatible (print)
✅ Caption format: "Figure X. Description"
✅ All axes labeled with units
✅ Legends inside or beside figures
```

---

### **2. STATISTICAL RIGOR**

#### **Nature Machine Intelligence:**
```
✅ Sample size (n) ALWAYS reported
✅ Statistical tests NAMED (t-test, Mann-Whitney, etc.)
✅ P-values provided
✅ Center values specified (mean vs median)
✅ Error bars explained (SD, SE, CI)
✅ Multiple testing correction (if applicable)
```

#### **Management Science (INFORMS):**
```
✅ Robustness checks
✅ Sensitivity analysis
✅ Business impact quantification
✅ A/B testing methodology
✅ Statistical significance + practical significance
```

---

### **3. REPRODUCIBILITY (CRITICAL FOR ALL)**

#### **Nature Machine Intelligence - Data/Code Policy:**
```
✅ Data availability statement REQUIRED
✅ Code availability statement REQUIRED
✅ "Data, materials, code comply with transparency standards"
✅ GitHub/Zenodo links for code
✅ Protocols.io for step-by-step methods
✅ ORCID for all authors
```

#### **IEEE/ACM Standards:**
```
✅ Pseudocode for algorithms
✅ Hyperparameters documented
✅ Random seeds specified
✅ Hardware specifications
✅ Runtime measurements
✅ Dataset splits (train/val/test) exact percentages
```

---

### **4. ETHICAL AI & BIAS (Nature Machine Intelligence Priority)**

#### **Required Disclosures:**
```
✅ Bias assessment documented
✅ Fairness metrics reported
✅ Protected attributes handled
✅ "Ethics & Inclusion statement" (if using human data)
✅ Local researchers involvement (if applicable)
✅ Limitations section MANDATORY
```

---

### **5. FIGURE QUALITY CHECKLIST (ENFORCEABLE)**

```python
# Nature Machine Intelligence Figure Checklist:

□ Color-blind safe palette (CB_COLORS)
□ Verbal legend descriptions ("blue circles" not just "○")
□ Sample size (n=X) in caption or on figure
□ Statistical test named (e.g., "Mann-Whitney U, p<0.001")
□ Error bars with explanation (SD, SE, 95% CI)
□ Contrast ratio ≥4.5:1
□ Vector format (SVG/PDF) or 300+ DPI PNG
□ Font size ≥8pt when scaled
□ Axes labeled with units
□ Title clear and informative
□ Caption follows "Figure X. Description" format
□ No unexplained abbreviations
□ Grid subtle (alpha=0.3) or absent
□ Professional styling (no default matplotlib)
□ Accessible to grayscale/print
```

---

##  PHASE-SPECIFIC REQUIREMENTS

### **PHASE 1: EDA (Current Phase)**

#### **Nature Machine Intelligence:**
```
✅ Descriptive statistics (n, mean, median, SD)
✅ Distribution visualizations (histograms, KDE)
✅ Missing data analysis
✅ Outlier detection methodology
✅ Correlation analysis (with p-values)
✅ Temporal analysis (if time-series)
✅ Sample size justification
```

#### **ACM RecSys:**
```
✅ Sparsity analysis (user-item matrix)
✅ Cold-start problem quantification
✅ Power-law distribution (users/items)
✅ Temporal dynamics
✅ Dataset bias analysis
```

#### **Information Fusion:**
```
✅ Multi-modal data fusion strategy
✅ Data quality per modality
✅ Integration methodology
✅ Complementarity analysis
```

---

### **PHASE 2: DATA PREPROCESSING**

```
✅ Missing value handling (with justification)
✅ Outlier treatment (IQR, Z-score, domain knowledge)
✅ Normalization/scaling (method + reason)
✅ Feature encoding (categorical → numerical)
✅ Data leakage prevention documented
✅ Train/val/test split BEFORE preprocessing
✅ Preprocessing pipeline reproducible
```

---

### **PHASE 3: FEATURE ENGINEERING**

```
✅ Feature creation rationale (domain knowledge)
✅ Feature selection methodology
✅ Correlation with target variable
✅ Feature importance (univariate analysis)
✅ Dimensionality reduction (if used)
✅ Feature interaction analysis
✅ Computational cost documented
```

---

### **PHASE 4: BASELINE MODEL TRAINING**

#### **Nature Machine Intelligence:**
```
✅ Model architecture detailed
✅ Hyperparameter search strategy (grid, random, Bayesian)
✅ Cross-validation (k-fold, stratified)
✅ Training curves (loss, accuracy over epochs)
✅ Convergence criteria
✅ Overfitting prevention (early stopping, regularization)
✅ Baseline comparisons (simple models)
```

#### **IEEE TKDE:**
```
✅ Computational complexity (Big-O)
✅ Scalability analysis
✅ Runtime on standard hardware
✅ Memory footprint
✅ Comparison with SOTA methods
```

---

### **PHASE 5: XAI INTEGRATION (SHAP)**

#### **Nature Machine Intelligence (XAI Priority):**
```
✅ Explanation method justified (why SHAP?)
✅ SHAP values visualization (beeswarm, waterfall)
✅ Feature importance ranking
✅ Explanation consistency checked
✅ User study (if applicable) - qualitative feedback
✅ Explanation accuracy (NIST Principle 3)
✅ Explanation coverage (% of predictions explained)
```

#### **ACM Computing Surveys:**
```
✅ Comparison of XAI methods (SHAP vs LIME vs others)
✅ Taxonomy of explanations (local, global, example-based)
✅ Evaluation metrics for explanations
✅ Literature review comprehensive
```

---

### **PHASE 6: ADAPTIVE LEARNING**

```
✅ Drift detection methodology (KS-test, MMD)
✅ Retraining triggers defined
✅ Concept drift vs covariate drift
✅ Online learning vs batch retraining
✅ Performance degradation curves
✅ Retraining cost analysis
✅ A/B testing for model updates
```

---

### **PHASE 7: ETHICAL AI MONITORING**

#### **Nature Machine Intelligence (Ethics Priority):**
```
✅ Bias metrics (demographic parity, equal opportunity)
✅ Fairness across protected attributes
✅ Disparate impact analysis
✅ Mitigation strategies documented
✅ Continuous monitoring dashboard
✅ Ethics & Inclusion statement
✅ Limitations acknowledged
```

---

### **PHASE 8: BUSINESS IMPACT MEASUREMENT**

#### **Management Science (INFORMS):**
```
✅ Business metrics (revenue, conversion, retention)
✅ A/B testing methodology (sample size, duration)
✅ Statistical vs practical significance
✅ ROI calculation
✅ Cost-benefit analysis
✅ Sensitivity analysis (what-if scenarios)
✅ Long-term impact projection
```

---

### **PHASE 9: CROSS-DOMAIN TRANSFER**

```
✅ Source domain characteristics
✅ Target domain characteristics
✅ Domain gap analysis
✅ Transfer learning methodology
✅ Performance comparison (with vs without transfer)
✅ Negative transfer risk
✅ Adaptation strategy
```

---

### **PHASE 10: API & DASHBOARD**

```
✅ System architecture diagram
✅ API documentation (endpoints, parameters)
✅ Dashboard usability testing
✅ Response time benchmarks
✅ Scalability testing
✅ Security considerations
✅ User manual/tutorial
```

---

##  WRITING STANDARDS

### **Abstract (Nature Machine Intelligence):**
```
✅ 100-150 words
✅ No references
✅ Problem statement
✅ Method summary
✅ Key results (quantified)
✅ Significance/impact
```

### **Methods Section:**
```
✅ Concise but complete
✅ Reproducible by expert
✅ All parameters specified
✅ Software versions listed
✅ Statistical tests named
✅ Limitations discussed
```

### **Results Section:**
```
✅ Figures/tables referenced
✅ Statistical significance reported
✅ Effect sizes provided
✅ Negative results included
✅ No interpretation (save for Discussion)
```

### **Discussion Section:**
```
✅ Results interpretation
✅ Comparison with literature
✅ Limitations acknowledged
✅ Future work suggested
✅ Broader impact discussed
```

---

##  PEER REVIEW PREPARATION

### **Common Reviewer Concerns (Address Proactively):**
```
✅ Sample size sufficient?
✅ Statistical tests appropriate?
✅ Baselines fair?
✅ Overfitting controlled?
✅ Limitations acknowledged?
✅ Reproducibility ensured?
✅ Novelty clear?
✅ Significance demonstrated?
✅ Writing clear?
✅ Figures publication-quality?
```

---

##  NOVELTY CLAIMS (MUST JUSTIFY)

### **XAE-Frame Novel Contributions:**
```
✅ Explanation knowledge transfer (FIRST framework)
✅ NIST-compliant adaptive XAI (UNIQUE integration)
✅ Cross-domain fairness monitoring (NOVEL approach)
✅ Business-impact-driven XAI (PRACTICAL focus)
```

### **How to Justify Novelty:**
```
✅ Literature gap analysis
✅ Comparison table (existing vs proposed)
✅ Ablation studies (what each component adds)
✅ Performance improvements quantified
✅ Use cases demonstrated
```

---

##  COMMON REJECTION REASONS (AVOID!)

### **Nature Machine Intelligence:**
```
❌ Insufficient novelty
❌ Limited significance
❌ Poor reproducibility
❌ Inadequate statistical rigor
❌ Ethics concerns
❌ Writing quality issues
❌ Figures not publication-quality
❌ Methods not detailed enough
```

### **IEEE TKDE:**
```
❌ No comparison with SOTA
❌ Computational complexity not analyzed
❌ Scalability not demonstrated
❌ Limited experimental validation
❌ No ablation study
```

### **ACM RecSys:**
```
❌ Dataset too small/simple
❌ No cold-start analysis
❌ No user study
❌ Offline metrics only (no online A/B test)
❌ Not compared with RecSys baselines
```

---

##  TIMELINE FOR PUBLICATION-READY WORK

```
Week 1-2:  EDA (publication-quality figures)
Week 3-4:  Preprocessing + Feature Engineering
Week 5-6:  Baseline models (with all metrics)
Week 7-8:  XAI integration (SHAP analysis)
Week 9-10: Adaptive + Ethical AI
Week 11:   Business impact + Cross-domain
Week 12:   API/Dashboard + Documentation
Week 13-14: Manuscript writing
Week 15-16: Internal review + revisions
Week 17:   Submission!
```

---

##  FINAL PRE-SUBMISSION CHECKLIST

```
□ All figures color-blind safe (CB_COLORS)
□ All figures 300+ DPI or vector
□ All statistical tests named + p-values
□ Sample sizes (n) always reported
□ Code on GitHub (public or upon request)
□ Data availability statement
□ Ethics statement (if applicable)
□ ORCID for all authors
□ References formatted (journal style)
□ Supplementary materials organized
□ Methods reproducible
□ Limitations acknowledged
□ Novelty clearly stated
□ Baselines comprehensive
□ Figures captioned properly
□ Tables formatted correctly
□ No plagiarism (self or others)
□ All co-authors approved
□ Funding acknowledged
□ Competing interests declared
□ Manuscript proofread (grammar/spelling)
```

---

##  KEY PAPERS TO CITE (YOUR RESEARCH BASE)

1. **Transformer (NeurIPS 2017):**  
   Vaswani et al., "Attention Is All You Need"

2. **XAI Survey (ACM Computing Surveys 2021):**  
   Guidotti et al., "A Survey on Explainable AI: Techniques, Taxonomies, Challenges"

3. **RecSys Survey (ACM 2020):**  
   Zhang et al., "Deep Learning for Recommender Systems"

4. **Information Fusion (Elsevier 2022):**  
   Gao et al., "Information Fusion in Deep Learning: A Survey"

5. **Interpretable ML (Community Standard):**  
   Molnar, "Interpretable Machine Learning" (Book)

6. **Recent (2025):**  
   "Adaptive autoregressive diffusion for humanized antibodies" (Nature-level)  
   "High-level visual representations aligned with LLMs" (Neuroscience + AI)

---

##  IMMEDIATE ACTIONS FOR CURRENT EDA

### **Priority 1: Update Figures to Journal Standards**
```python
# Add to EVERY figure cell:

# 1. Use CB_COLORS
colors = [CB_COLORS['blue'], CB_COLORS['orange'], CB_COLORS['green']]

# 2. Add statistical annotations
ax.text(x, y, f'n={len(data)}, p={p_value:.3f}', fontsize=10)

# 3. Verbal legend
ax.legend(['Group A (blue circles)', 'Group B (orange triangles)'])

# 4. Save multi-format
save_publication_figure(fig, 'figure_name', formats=['png', 'svg', 'pdf'])

# 5. Add caption
add_figure_caption(fig, "Description. n=X samples. Statistical test: Y, p<0.001.")
```

### **Priority 2: Add Methods Documentation**
```markdown
## Methods: Exploratory Data Analysis

### Data Source
Amazon Reviews 2023 dataset (McAuley et al., 2023), All_Beauty category.
Sample size: n=701,156 reviews from 254,000+ users.

### Statistical Tests
- Mann-Whitney U test for group comparisons (non-parametric)
- Pearson correlation for continuous variables
- Chi-square test for categorical associations
- Significance threshold: α=0.05 with Bonferroni correction

### Visualization
Color-blind safe palette (Wong 2011). All figures 300 DPI, vector formats.
Software: Python 3.9, matplotlib 3.7, seaborn 0.12.

### Data Quality
Missing data: <5% for all critical features. Outliers identified via IQR method.
No data excluded unless explicitly noted.
```

---

##  REMEMBER: EVERY DECISION MUST BE JUSTIFIED!

**Reviewer will ask:**
- "Why this method?" → Cite literature
- "Why this threshold?" → Domain knowledge or data-driven
- "Why exclude X?" → Statistical or scientific reason
- "Why this visualization?" → Clarity and accessibility

**Always have an answer ready in the manuscript!**

---

 **This checklist will be updated as project progresses through each phase.**

