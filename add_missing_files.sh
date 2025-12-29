#!/bin/bash

# XAE-Frame v3.6 - ADD MISSING FILES SCRIPT
# Adds only the files that are missing from current structure

set -e
BASE_DIR="$HOME/Desktop/xai-personalization-framework"
cd "$BASE_DIR"

echo "XAE-Frame v3.6 - Adding Missing Files"
echo "========================================="
echo ""

# CREATE MISSING DIRECTORIES

echo "Creating missing directories..."
mkdir -p src/explainability
mkdir -p src/realtime
mkdir -p src/compliance
mkdir -p tests

# Create __init__ files
touch src/explainability/__init__.py
touch src/realtime/__init__.py
touch src/compliance/__init__.py
touch tests/__init__.py

echo "Directories created!"
echo ""


# 1. src/explainability/fidelity.py

echo "Creating src/explainability/fidelity.py..."

cat > src/explainability/fidelity.py << 'PYEOF'
"""
v3.6: Explanation Fidelity Checker
Validates that explanations accurately represent model behavior.

Author: Nazlı Özgür
Date: December 2025
"""
import numpy as np
from scipy.stats import pearsonr


class FidelityChecker:
    """Validate explanation quality and model agreement."""
    
    def __init__(self, threshold=0.80):
        self.threshold = threshold
    
    def check_model_agreement(self, model1, model2, X_test):
        """
        Check agreement between two models (e.g., LightGBM vs Decision Tree).
        
        Returns:
            dict: Fidelity metrics
        """
        print("Checking Model Agreement Fidelity...")
        
        pred1 = model1.predict(X_test)
        pred2 = model2.predict(X_test)
        
        correlation, p_value = pearsonr(pred1, pred2)
        
        # Binary agreement (within 10% tolerance)
        tolerance = 0.1
        agreement = np.mean(np.abs(pred1 - pred2) / (np.abs(pred1) + 1e-8) < tolerance)
        
        results = {
            'correlation': correlation,
            'p_value': p_value,
            'binary_agreement': agreement,
            'passes_threshold': correlation >= self.threshold
        }
        
        print(f"   Correlation: {correlation:.4f}")
        print(f"   Agreement: {agreement:.2%}")
        print(f"   Status: {'PASS' if results['passes_threshold'] else 'FAIL'}")
        
        return results
    
    def check_shap_fidelity(self, model, X, shap_values):
        """
        Check if SHAP values accurately represent model predictions.
        
        Returns:
            dict: SHAP fidelity metrics
        """
        print("\n Checking SHAP Fidelity...")
        
        actual_pred = model.predict(X)
        
        if len(shap_values.shape) == 2:
            shap_pred = shap_values.sum(axis=1)
        else:
            shap_pred = shap_values
        
        correlation, p_value = pearsonr(actual_pred, shap_pred)
        mae = np.mean(np.abs(actual_pred - shap_pred))
        
        results = {
            'correlation': correlation,
            'p_value': p_value,
            'mae': mae,
            'passes_threshold': correlation >= 0.90
        }
        
        print(f"   SHAP Correlation: {correlation:.4f}")
        print(f"   MAE: {mae:.4f}")
        print(f"   Status: {'PASS' if results['passes_threshold'] else 'FAIL'}")
        
        return results
    
    def check_explanation_stability(self, explainer, X, epsilon=0.01, n_trials=5):
        """
        Check robustness of explanations to input perturbations.
        
        Returns:
            dict: Stability metrics
        """
        print(f"\n Checking Explanation Stability (ε={epsilon})...")
        
        shap_original = explainer.shap_values(X)
        correlations = []
        
        for trial in range(n_trials):
            X_noisy = X + np.random.normal(0, epsilon, X.shape)
            shap_noisy = explainer.shap_values(X_noisy)
            
            corr, _ = pearsonr(shap_original.flatten(), shap_noisy.flatten())
            correlations.append(corr)
        
        avg_stability = np.mean(correlations)
        
        results = {
            'mean_stability': avg_stability,
            'std_stability': np.std(correlations),
            'min_stability': np.min(correlations),
            'passes_threshold': avg_stability >= 0.80
        }
        
        print(f"   Mean Stability: {avg_stability:.4f}")
        print(f"   Status: {'PASS' if results['passes_threshold'] else 'FAIL'}")
        
        return results


if __name__ == "__main__":
    print("Fidelity Checker Ready!")
    print("Use: checker = FidelityChecker()")
PYEOF

echo "fidelity.py created!"

# 2. src/explainability/counterfactual.py

echo "Creating src/explainability/counterfactual.py..."

cat > src/explainability/counterfactual.py << 'PYEOF'
"""
v3.6: Counterfactual Explanation Generator
DiCE-ML integration for actionable user-facing recommendations.

Author: Nazlı Özgür
Date: December 2025
"""
import pandas as pd
import numpy as np


class CounterfactualExplainer:
    """
    Generate actionable counterfactual explanations.
    Shows users what they can change to get desired outcomes.
    """
    
    def __init__(self, model, data, continuous_features=None, categorical_features=None):
        self.model = model
        self.data = data
        self.continuous_features = continuous_features or []
        self.categorical_features = categorical_features or []
        self.dice_exp = None
    
    def setup_dice(self):
        """Initialize DiCE explainer (requires: pip install dice-ml)."""
        try:
            import dice_ml
            
            d = dice_ml.Data(
                dataframe=self.data,
                continuous_features=self.continuous_features,
                outcome_name='target'
            )
            
            m = dice_ml.Model(model=self.model, backend='sklearn')
            self.dice_exp = dice_ml.Dice(d, m)
            
            print("DiCE explainer initialized!")
            
        except ImportError:
            print("DiCE-ML not installed. Run: pip install dice-ml")
            self.dice_exp = None
    
    def generate_counterfactuals(self, query_instance, desired_outcome, 
                                 total_CFs=3, proximity_weight=0.5):
        """
        Generate counterfactual explanations.
        
        Returns:
            pd.DataFrame: Counterfactual examples
        """
        if self.dice_exp is None:
            print("DiCE not initialized. Run setup_dice() first.")
            return None
        
        try:
            dice_result = self.dice_exp.generate_counterfactuals(
                query_instance,
                total_CFs=total_CFs,
                desired_class=desired_outcome,
                proximity_weight=proximity_weight
            )
            
            cf_df = dice_result.cf_examples_list[0].final_cfs_df
            return cf_df
            
        except Exception as e:
            print(f"Error generating counterfactuals: {e}")
            return None
    
    def filter_actionable_features(self, counterfactuals, proxy_taxonomy):
        """
        Filter counterfactuals to only show actionable features.
        
        Returns:
            pd.DataFrame: Filtered counterfactuals
        """
        if counterfactuals is None:
            return None
        
        actionable_features = []
        for feature, meta in proxy_taxonomy.items():
            if meta['type'] in ['Actionable'] and meta['gaming_risk'] != 'HIGH':
                actionable_features.append(feature)
        
        print(f"Filtered to {len(actionable_features)} actionable features")
        return counterfactuals[actionable_features] if actionable_features else counterfactuals
    
    def explain_to_user(self, original_instance, counterfactual, feature_names=None):
        """
        Generate human-readable explanation.
        
        Returns:
            list: Actionable recommendations
        """
        recommendations = []
        
        if feature_names is None:
            feature_names = original_instance.index
        
        for feature in feature_names:
            orig_val = original_instance[feature]
            cf_val = counterfactual[feature]
            
            if orig_val != cf_val:
                if isinstance(orig_val, (int, float)):
                    change_pct = ((cf_val - orig_val) / orig_val) * 100 if orig_val != 0 else 0
                    recommendations.append({
                        'feature': feature,
                        'current': orig_val,
                        'suggested': cf_val,
                        'change': cf_val - orig_val,
                        'change_pct': change_pct,
                        'message': f"Increase {feature} by {change_pct:.1f}%"
                    })
                else:
                    recommendations.append({
                        'feature': feature,
                        'current': orig_val,
                        'suggested': cf_val,
                        'message': f"Change {feature} from '{orig_val}' to '{cf_val}'"
                    })
        
        return recommendations


if __name__ == "__main__":
    print("Counterfactual Explainer Ready!")
    print("Example: 'Increase review_length by 30%'")
PYEOF

echo "counterfactual.py created!"

# 3. src/realtime/log_monitor.py

echo "Creating src/realtime/log_monitor.py..."

cat > src/realtime/log_monitor.py << 'PYEOF'
"""
v3.6: Training-Serving Skew Monitor
Implements Google ML Rule #32: Log serving data to detect skew.

Author: Nazlı Özgür
Date: December 2025
"""
import json
from datetime import datetime
from pathlib import Path


class LogMonitor:
    """Monitor and log serving data for skew detection."""
    
    def __init__(self, redis_host='localhost', redis_port=6379, 
                 log_file='logs/serving.log'):
        self.log_file = Path(log_file)
        self.log_file.parent.mkdir(parents=True, exist_ok=True)
        self.use_redis = False
        
        try:
            import redis
            self.redis_client = redis.Redis(
                host=redis_host,
                port=redis_port,
                decode_responses=True
            )
            self.redis_client.ping()
            self.use_redis = True
            print("Redis connected")
        except:
            print("Redis not available, using file logging")
    
    def log_serving_request(self, raw_input, preprocessed, prediction, model_version):
        """Log a single serving request."""
        log_entry = {
            'timestamp': datetime.now().isoformat(),
            'model_version': model_version,
            'raw_input': raw_input,
            'preprocessed': preprocessed,
            'prediction': float(prediction) if hasattr(prediction, '__float__') else prediction
        }
        
        if self.use_redis:
            self.redis_client.lpush('serving_log', json.dumps(log_entry))
            self.redis_client.ltrim('serving_log', 0, 9999)
        
        with open(self.log_file, 'a') as f:
            f.write(json.dumps(log_entry) + '\n')
    
    def get_recent_logs(self, n=100):
        """Retrieve recent log entries."""
        if self.use_redis:
            raw_logs = self.redis_client.lrange('serving_log', 0, n-1)
            return [json.loads(log) for log in raw_logs]
        
        logs = []
        with open(self.log_file, 'r') as f:
            for line in f.readlines()[-n:]:
                logs.append(json.loads(line))
        return logs
    
    def detect_skew(self, training_baseline, feature='target'):
        """
        Detect distribution skew between training and serving.
        
        Returns:
            dict: Skew detection results
        """
        from scipy.stats import ks_2samp
        import numpy as np
        
        recent_logs = self.get_recent_logs(n=1000)
        
        if not recent_logs:
            print("No serving logs available")
            return None
        
        serving_values = []
        for log in recent_logs:
            if 'preprocessed' in log and feature in log['preprocessed']:
                serving_values.append(log['preprocessed'][feature])
        
        if not serving_values:
            print(f" No data for feature: {feature}")
            return None
        
        serving_values = np.array(serving_values)
        training_values = np.array(training_baseline.get(feature, []))
        
        if len(training_values) == 0:
            print(f" No training baseline for: {feature}")
            return None
        
        statistic, p_value = ks_2samp(training_values, serving_values)
        
        results = {
            'feature': feature,
            'ks_statistic': statistic,
            'p_value': p_value,
            'n_training': len(training_values),
            'n_serving': len(serving_values),
            'training_mean': float(np.mean(training_values)),
            'serving_mean': float(np.mean(serving_values)),
            'skew_detected': p_value < 0.05
        }
        
        print(f"\n🔍 Skew Detection for '{feature}':")
        print(f"   KS Statistic: {statistic:.4f}")
        print(f"   p-value: {p_value:.4f}")
        print(f"   Status: {'SKEW!' if results['skew_detected'] else 'No skew'}")
        
        return results


if __name__ == "__main__":
    print("Log Monitor Ready!")
    print("Tracks training-serving consistency (Google Rule #32)")
PYEOF

echo "log_monitor.py created!"

# 4. src/compliance/governance.py

echo "Creating src/compliance/governance.py..."

cat > src/compliance/governance.py << 'PYEOF'
"""
v3.6: EU AI Act & NIST Compliance Checker
Validates compliance with EU AI Act and NIST IR 8312.

Author: Nazlı Özgür
Date: December 2025
"""
import json
from datetime import datetime


class GovernanceAuditor:
    """Audit ML system for regulatory compliance."""
    
    def __init__(self):
        self.audit_results = {}
    
    def check_data_quality(self, data_quality_score, threshold=80):
        """EU AI Act Article 10: Data Quality."""
        compliant = data_quality_score >= threshold
        
        result = {
            'article': 'EU AI Act Article 10',
            'requirement': 'Data Quality',
            'score': data_quality_score,
            'threshold': threshold,
            'compliant': compliant,
            'checked_at': datetime.now().isoformat()
        }
        
        self.audit_results['data_quality'] = result
        print(f"{'✅' if compliant else '❌'} Data Quality: {data_quality_score:.1f}/100")
        
        return result
    
    def check_fairness(self, fairness_ratio, threshold=0.80):
        """EU AI Act Article 10: Non-discrimination."""
        compliant = fairness_ratio >= threshold
        
        result = {
            'article': 'EU AI Act Article 10',
            'requirement': 'Non-Discrimination',
            'fairness_ratio': fairness_ratio,
            'threshold': threshold,
            'compliant': compliant,
            'checked_at': datetime.now().isoformat()
        }
        
        self.audit_results['fairness'] = result
        print(f"{'✅' if compliant else '❌'} Fairness: {fairness_ratio:.3f}")
        
        return result
    
    def check_nist_explainability(self, fidelity_score, threshold=0.90):
        """NIST Principle 1: Explanation."""
        compliant = fidelity_score >= threshold
        
        result = {
            'standard': 'NIST IR 8312 Principle 1',
            'requirement': 'Explanation',
            'fidelity_score': fidelity_score,
            'threshold': threshold,
            'compliant': compliant,
            'checked_at': datetime.now().isoformat()
        }
        
        self.audit_results['nist_explainability'] = result
        print(f"{'✅' if compliant else '❌'} NIST Explainability: {fidelity_score:.3f}")
        
        return result
    
    def generate_audit_report(self, filepath='docs/compliance_audit.json'):
        """Generate compliance audit report."""
        from pathlib import Path
        
        total_checks = len(self.audit_results)
        passed_checks = sum(1 for r in self.audit_results.values() if r['compliant'])
        compliance_rate = (passed_checks / total_checks * 100) if total_checks > 0 else 0
        
        report = {
            'generated_at': datetime.now().isoformat(),
            'overall_compliance': compliance_rate,
            'total_checks': total_checks,
            'passed_checks': passed_checks,
            'failed_checks': total_checks - passed_checks,
            'details': self.audit_results
        }
        
        Path(filepath).parent.mkdir(parents=True, exist_ok=True)
        with open(filepath, 'w') as f:
            json.dump(report, f, indent=2)
        
        print(f"\n{'='*60}")
        print(f"COMPLIANCE AUDIT SUMMARY")
        print(f"{'='*60}")
        print(f"Overall Compliance: {compliance_rate:.1f}%")
        print(f"Passed: {passed_checks}/{total_checks}")
        print(f"Report saved: {filepath}")
        print(f"{'='*60}")
        
        return report


if __name__ == "__main__":
    print("Governance Auditor Ready!")
    print("Checks: EU AI Act + NIST IR 8312")
PYEOF

echo "governance.py created!"

# 5. src/models/intrinsic_baseline.py

echo "Creating src/models/intrinsic_baseline.py..."

cat > src/models/intrinsic_baseline.py << 'PYEOF'
"""
v3.6: Intrinsic Baseline Model - Decision Tree
Transparent, interpretable glass-box model for comparison.

Author: Nazlı Özgür
Date: December 2025
"""
from sklearn.tree import DecisionTreeRegressor, export_text
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np


class IntrinsicBaseline:
    """Glass-box model for interpretability comparison."""
    
    def __init__(self, max_depth=5, min_samples_split=50, random_state=42):
        self.model = DecisionTreeRegressor(
            max_depth=max_depth,
            min_samples_split=min_samples_split,
            random_state=random_state
        )
        self.max_depth = max_depth
        self.feature_names = None
    
    def train(self, X_train, y_train, feature_names=None):
        """Train the decision tree."""
        print("Training Intrinsic Baseline (Decision Tree)...")
        
        if feature_names is not None:
            self.feature_names = feature_names
        elif hasattr(X_train, 'columns'):
            self.feature_names = list(X_train.columns)
        
        self.model.fit(X_train, y_train)
        
        train_pred = self.model.predict(X_train)
        train_rmse = np.sqrt(mean_squared_error(y_train, train_pred))
        train_r2 = r2_score(y_train, train_pred)
        
        print(f"   Training complete!")
        print(f"   Train RMSE: {train_rmse:.4f}")
        print(f"   Train R²: {train_r2:.4f}")
        
        return self
    
    def predict(self, X):
        """Make predictions."""
        return self.model.predict(X)
    
    def evaluate(self, X_test, y_test):
        """Evaluate model performance."""
        y_pred = self.predict(X_test)
        
        metrics = {
            'rmse': np.sqrt(mean_squared_error(y_test, y_pred)),
            'r2': r2_score(y_test, y_pred)
        }
        
        print(f"\n Test Performance:")
        print(f"   RMSE: {metrics['rmse']:.4f}")
        print(f"   R²: {metrics['r2']:.4f}")
        
        return metrics
    
    def get_rules(self):
        """Extract human-readable decision rules."""
        if self.feature_names is None:
            feature_names = [f"feature_{i}" for i in range(self.model.n_features_in_)]
        else:
            feature_names = self.feature_names
        
        rules = export_text(self.model, feature_names=feature_names)
        return rules
    
    def print_rules(self):
        """Print decision rules to console."""
        rules = self.get_rules()
        print("\n Decision Rules:")
        print("="*60)
        print(rules)
        print("="*60)


if __name__ == "__main__":
    print(" Intrinsic Baseline Ready!")
    print("Use: baseline = IntrinsicBaseline(max_depth=5)")
PYEOF

echo " intrinsic_baseline.py created!"


