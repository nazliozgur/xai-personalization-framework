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
