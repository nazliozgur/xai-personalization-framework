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
