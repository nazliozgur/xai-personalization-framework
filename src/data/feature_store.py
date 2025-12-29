"""
v3.6 ENHANCED: Feature Store with Metadata Layer
Ensures features are computed identically + stores governance metadata.
Implements: Google ML Rule #32 + Uber Feature Store pattern

Author: Nazlı Özgür
Date: December 2025
"""
import pandas as pd
import numpy as np
import redis
import json
import yaml
from datetime import datetime
from pathlib import Path


class FeatureStore:
    """
    Single source of truth for feature computation WITH metadata layer.
    Used in BOTH training and serving to ensure consistency.
    
    IMPROVEMENT 1: Metadata integration (Uber/Google pattern)
    """
    
    def __init__(self, redis_host='localhost', redis_port=6379, use_cache=True,
                 metadata_path='config/feature_metadata.yaml'):
        """
        Initialize feature store with metadata layer.
        
        Args:
            redis_host (str): Redis server host
            redis_port (int): Redis server port
            use_cache (bool): Whether to use Redis caching
            metadata_path (str): Path to feature metadata YAML
        """
        self.use_cache = use_cache
        self.metadata = self._load_metadata(metadata_path)
        
        if use_cache:
            try:
                self.redis_client = redis.Redis(
                    host=redis_host, 
                    port=redis_port,
                    decode_responses=True
                )
                self.redis_client.ping()
                print("Connected to Redis feature store")
            except redis.ConnectionError:
                print("Redis not available, caching disabled")
                self.use_cache = False
    
    def _load_metadata(self, metadata_path):
        """
        IMPROVEMENT 1: Load feature metadata from YAML.
        
        Args:
            metadata_path (str): Path to feature_metadata.yaml
        
        Returns:
            dict: Feature metadata
        """
        path = Path(metadata_path)
        
        if not path.exists():
            print(f"Metadata file not found: {metadata_path}")
            return {'features': {}}
        
        with open(path, 'r') as f:
            metadata = yaml.safe_load(f)
        
        print(f"Loaded feature metadata from {metadata_path}")
        return metadata
    
    def get_feature_metadata(self, feature_name):
        """
        Get metadata for a specific feature.
        
        Args:
            feature_name (str): Feature name
        
        Returns:
            dict: Metadata (type, gaming_risk, etc.)
        """
        return self.metadata.get('features', {}).get(feature_name, {
            'type': 'Unknown',
            'gaming_risk': 'UNKNOWN'
        })
    
    def compute_features(self, raw_data, feature_config=None):
        """
        Compute features from raw data WITH metadata attachment.
        THIS IS THE SINGLE SOURCE OF TRUTH!
        
        Args:
            raw_data (dict or pd.Series): Raw input data
            feature_config (dict, optional): Feature computation config
        
        Returns:
            dict: {
                'features': computed feature values,
                'metadata': feature metadata (type, gaming_risk)
            }
        """
        features = {}
        
        # Temporal features (Causal)
        if 'timestamp' in raw_data:
            features.update(self._compute_temporal_features(raw_data))
        
        # Text features (Proxy)
        if 'text' in raw_data:
            features.update(self._compute_text_features(raw_data))
        
        # User features (Proxy)
        if 'user_id' in raw_data:
            features.update(self._compute_user_features(raw_data))
        
        # Product features (Proxy)
        if 'product_id' in raw_data:
            features.update(self._compute_product_features(raw_data))
        
        # Attach metadata
        feature_metadata = {}
        for feat_name in features.keys():
            feature_metadata[feat_name] = self.get_feature_metadata(feat_name)
        
        return {
            'features': features,
            'metadata': feature_metadata
        }
    
    def _compute_temporal_features(self, data):
        """Compute temporal features."""
        features = {}
        
        if 'timestamp' in data:
            ts = pd.to_datetime(data['timestamp'])
            now = pd.Timestamp.now()
            
            features['days_since_event'] = (now - ts).days
            features['hour_of_day'] = ts.hour
            features['day_of_week'] = ts.dayofweek
            features['is_weekend'] = 1 if ts.dayofweek >= 5 else 0
        
        return features
    
    def _compute_text_features(self, data):
        """Compute text features."""
        features = {}
        
        if 'text' in data:
            text = str(data['text'])
            features['text_length'] = len(text)
            features['word_count'] = len(text.split())
            features['avg_word_length'] = np.mean([len(w) for w in text.split()]) if text else 0
        
        return features
    
    def _compute_user_features(self, data):
        """Compute user-level features (requires historical data)."""
        features = {}
        
        # These would come from cache or database
        user_id = data.get('user_id')
        if user_id and self.use_cache:
            cached_stats = self.get_user_stats(user_id)
            if cached_stats:
                features.update(cached_stats)
        
        return features
    
    def _compute_product_features(self, data):
        """Compute product-level features (requires historical data)."""
        features = {}
        
        # These would come from cache or database
        product_id = data.get('product_id')
        if product_id and self.use_cache:
            cached_stats = self.get_product_stats(product_id)
            if cached_stats:
                features.update(cached_stats)
        
        return features
    
    def cache_features(self, entity_id, features, ttl=86400):
        """
        Cache computed features in Redis.
        
        Args:
            entity_id (str): Unique identifier (user_id, product_id, etc.)
            features (dict): Features to cache
            ttl (int): Time-to-live in seconds (default: 24 hours)
        """
        if not self.use_cache:
            return
        
        key = f"features:{entity_id}"
        self.redis_client.setex(key, ttl, json.dumps(features))
    
    def get_cached_features(self, entity_id):
        """
        Retrieve cached features from Redis.
        
        Args:
            entity_id (str): Unique identifier
        
        Returns:
            dict or None: Cached features or None if not found
        """
        if not self.use_cache:
            return None
        
        key = f"features:{entity_id}"
        cached = self.redis_client.get(key)
        
        if cached:
            return json.loads(cached)
        return None
    
    def get_user_stats(self, user_id):
        """Get user statistics from cache."""
        return self.get_cached_features(f"user_stats:{user_id}")
    
    def get_product_stats(self, product_id):
        """Get product statistics from cache."""
        return self.get_cached_features(f"product_stats:{product_id}")
    
    def batch_compute(self, df):
        """
        Compute features for a batch of records.
        
        Args:
            df (pd.DataFrame): Batch of raw data
        
        Returns:
            pd.DataFrame: DataFrame with computed features
        """
        feature_list = []
        
        for idx, row in df.iterrows():
            result = self.compute_features(row.to_dict())
            feature_list.append(result['features'])
        
        return pd.DataFrame(feature_list)


# Example usage
if __name__ == "__main__":
    # Initialize feature store with metadata
    fs = FeatureStore(use_cache=False)
    
    # Sample raw data
    raw_data = {
        'user_id': 'user_123',
        'product_id': 'prod_456',
        'timestamp': '2025-12-28 22:00:00',
        'text': 'This is a great product! Highly recommended.',
        'rating': 5
    }
    
    # Compute features WITH metadata
    result = fs.compute_features(raw_data)
    
    print("Computed Features:")
    for k, v in result['features'].items():
        metadata = result['metadata'].get(k, {})
        print(f"   {k}: {v} | Type: {metadata.get('type', 'Unknown')}")
    
    print("\n Training-Serving Consistency + Governance Metadata!")
