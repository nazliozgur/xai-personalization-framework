# XAE-Frame v3.6 Development Checklist

## v3.6 ENHANCEMENTS APPLIED:

### IMPROVEMENT 1: Metadata Layer (Uber/Google Pattern)
- [x] `ProxyAnalyzer.export_to_yaml()` added
- [x] `FeatureStore._load_metadata()` added
- [x] `FeatureStore.get_feature_metadata()` added
- [ ] **TODO:** Call `export_to_yaml()` in EDA notebook

### IMPROVEMENT 2: feature_metadata.yaml (Governance)
- [x] Created `config/feature_metadata.yaml`
- [ ] **TODO:** Update with actual project features (Phase 2 Day 3)

### IMPROVEMENT 3: Dashboard Main Entry (app.py)
- [x] Created `src/dashboard/app.py`
- [x] Dual-entry system (Admin vs User)
- [ ] **TODO:** Test dashboard (Phase 6 Day 1)

### IMPROVEMENT 4: Fairlearn → Phase 2 EDA
- [ ] **TODO Phase 2 Day 2:** Add Fairlearn bias assessment
  ```python
  from fairlearn.metrics import demographic_parity_ratio
  
  dpr = demographic_parity_ratio(
      y_true=y,
      y_pred=predictions,
      sensitive_features=df['verification_status']
  )
  print(f"Demographic Parity Ratio: {dpr:.3f}")
  ```

### IMPROVEMENT 5: Training-Serving Skew Test Reminder
- [x] Created `tests/skew_tests.py`
- [ ] **TODO Phase 3 Day 7:** Run skew tests in integration testing
  ```bash
  pytest tests/skew_tests.py -v
  ```

---

## PHASE-BY-PHASE REMINDERS:

### PHASE 2: EDA & BASELINE 

**Day 2 (EDA):**
- [ ] Run Fairlearn bias assessment (IMPROVEMENT 4)
- [ ] Generate proxy taxonomy JSON
- [ ] **Export proxy taxonomy to YAML** (IMPROVEMENT 1)
  ```python
  analyzer.export_to_yaml('config/feature_metadata.yaml')
  ```

**Day 3 (Feature Engineering):**
- [ ] Update `feature_metadata.yaml` with actual features
- [ ] Validate metadata loaded in FeatureStore

**Day 4 (Baseline Training):**
- [ ] Train dual baselines (LightGBM + Tree)
- [ ] Check fidelity (>0.80)

### PHASE 3: ADAPTIVE LOOP 

**Day 7 (Integration Testing):**
- [ ] **RUN SKEW TESTS** (IMPROVEMENT 5)
  ```bash
  pytest tests/skew_tests.py -v
  ```
- [ ] Verify training-serving consistency
- [ ] Check drift detection

### PHASE 6: DEMO & API 

**Day 1 (Dashboard):**
- [ ] Test `src/dashboard/app.py` (IMPROVEMENT 3)
- [ ] Verify dual-entry works
- [ ] Test admin vs user view switching

---

## SUCCESS CRITERIA (v3.6 Enhanced):

- [x] Metadata layer integrated
- [x] feature_metadata.yaml created
- [x] Dashboard main entry created
- [ ] Fairlearn in EDA (Phase 2 Day 2)
- [ ] Skew tests passed (Phase 3 Day 7)
- [ ] All 5 improvements verified

---

**Last Updated:** December 28, 2025  
**Author:** Nazlı Özgür
