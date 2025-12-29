"""
v3.6: Proxy vs Causal Feature Classifier
Labels each feature as: [Causal], [Proxy], [Actionable]

Author: Nazlı Özgür
Date: December 2025
"""
import pandas as pd
import json
from pathlib import Path


class ProxyAnalyzer:
    """
    Classify features by manipulability and gaming risk.
    
    Feature Types:
    - Causal: Unchangeable (age, demographics)
    - Proxy: Changeable, gameable (votes, engagement)
    - Actionable: User can legitimately change (verified status)
    """
    
    def __init__(self):
        self.taxonomy = {}
    
    def classify_feature(self, feature_name, feature_data=None):
        """
        Classify a single feature.
        
        Args:
            feature_name (str): Name of the feature
            feature_data (pd.Series, optional): Feature values for analysis
        
        Returns:
            dict: Classification metadata
        """
        feature_lower = feature_name.lower()
        
        # Causal features (unchangeable)
        causal_keywords = ['age', 'date', 'created', 'birth', 'gender', 
                          'location', 'country', 'state', 'city']
        if any(kw in feature_lower for kw in causal_keywords):
            return {
                'type': 'Causal',
                'manipulable': False,
                'gaming_risk': 'NONE',
                'causal_parent': 'demographics',
                'description': 'Unchangeable demographic or temporal feature'
            }
        
        # Proxy features (changeable, high gaming risk)
        proxy_keywords = ['vote', 'count', 'frequency', 'score', 'rating', 
                         'review', 'engagement', 'activity', 'interaction']
        if any(kw in feature_lower for kw in proxy_keywords):
            return {
                'type': 'Proxy',
                'manipulable': True,
                'gaming_risk': 'HIGH',
                'causal_parent': None,
                'description': 'Easily manipulable engagement metric'
            }
        
        # Actionable features (user can change legitimately)
        actionable_keywords = ['verified', 'length', 'text', 'purchase', 
                              'subscription', 'premium']
        if any(kw in feature_lower for kw in actionable_keywords):
            return {
                'type': 'Actionable',
                'manipulable': True,
                'gaming_risk': 'MEDIUM',
                'causal_parent': None,
                'description': 'User can legitimately modify this feature'
            }
        
        # Default: Unknown
        return {
            'type': 'Unknown',
            'manipulable': None,
            'gaming_risk': 'UNKNOWN',
            'causal_parent': None,
            'description': 'Feature type not yet classified'
        }
    
    def analyze_dataset(self, df):
        """
        Analyze all features in a DataFrame.
        
        Args:
            df (pd.DataFrame): Dataset to analyze
        
        Returns:
            dict: Complete taxonomy
        """
        print(f" Analyzing {len(df.columns)} features...")
        
        for col in df.columns:
            self.taxonomy[col] = self.classify_feature(col, df[col])
        
        # Print summary
        summary = self.get_summary()
        print(f"\n Taxonomy Summary:")
        print(f"   Total Features: {summary['total_features']}")
        print(f"   Causal: {summary['causal']}")
        print(f"   Proxy: {summary['proxy']}")
        print(f"   Actionable: {summary['actionable']}")
        print(f"   Unknown: {summary['unknown']}")
        
        return self.taxonomy
    
    def export_taxonomy(self, filepath='data/processed/proxy_taxonomy.json'):
        """Export taxonomy to JSON file."""
        filepath = Path(filepath)
        filepath.parent.mkdir(parents=True, exist_ok=True)
        
        with open(filepath, 'w') as f:
            json.dump(self.taxonomy, f, indent=2)
        
        print(f" Taxonomy exported to {filepath}")
    
    def export_to_yaml(self, filepath='config/feature_metadata.yaml'):
        """
         IMPROVEMENT 1: Export to YAML for governance readability.
        
        Args:
            filepath (str): Output YAML path
        """
        import yaml
        
        filepath = Path(filepath)
        filepath.parent.mkdir(parents=True, exist_ok=True)
        
        yaml_data = {'features': self.taxonomy}
        
        with open(filepath, 'w') as f:
            yaml.dump(yaml_data, f, default_flow_style=False, sort_keys=False)
        
        print(f" Taxonomy exported to {filepath} (YAML)")
    
    def get_summary(self):
        """Get taxonomy summary statistics."""
        types = [v['type'] for v in self.taxonomy.values()]
        return {
            'total_features': len(self.taxonomy),
            'causal': types.count('Causal'),
            'proxy': types.count('Proxy'),
            'actionable': types.count('Actionable'),
            'unknown': types.count('Unknown')
        }
    
    def get_high_risk_features(self):
        """Get list of high-risk (easily gameable) features."""
        high_risk = []
        for feature, metadata in self.taxonomy.items():
            if metadata['gaming_risk'] == 'HIGH':
                high_risk.append(feature)
        return high_risk


# Example usage
if __name__ == "__main__":
    # Demo
    import numpy as np
    
    # Create sample features
    sample_features = {
        'user_age': np.random.randint(18, 65, 100),
        'helpful_vote': np.random.randint(0, 100, 100),
        'verified_purchase': np.random.choice([True, False], 100),
        'review_length': np.random.randint(10, 500, 100),
        'account_created_date': pd.date_range('2020-01-01', periods=100),
        'avg_rating': np.random.uniform(1, 5, 100)
    }
    
    df = pd.DataFrame(sample_features)
    
    # Analyze
    analyzer = ProxyAnalyzer()
    taxonomy = analyzer.analyze_dataset(df)
    
    # Show results
    print("\n Feature Classifications:")
    for feat, meta in taxonomy.items():
        print(f"   {feat:30} → {meta['type']:12} (Gaming Risk: {meta['gaming_risk']})")
    
    # Export JSON + YAML
    analyzer.export_taxonomy()
    analyzer.export_to_yaml()
    
    # High risk features
    high_risk = analyzer.get_high_risk_features()
    print(f"\n  High-Risk Features: {high_risk}")
