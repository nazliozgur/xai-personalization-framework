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
