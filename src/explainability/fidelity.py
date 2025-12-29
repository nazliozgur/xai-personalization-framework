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
