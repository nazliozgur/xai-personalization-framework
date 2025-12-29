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
