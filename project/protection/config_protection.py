"""
Encrypted Configuration System
Stores sensitive configuration in obfuscated format
"""
import base64
import hashlib
import json
import os

class ConfigProtection:
    """Handles encrypted configuration"""
    
    def __init__(self, key=None):
        self._key = key or os.environ.get('ECOPACK_CONFIG_KEY', 'default_key')
        self._salt = 'ecopack_salt_v1'
        
    def _derive_key(self):
        """Derive encryption key"""
        combined = f"{self._key}{self._salt}"
        return hashlib.sha256(combined.encode()).digest()
    
    def _xor_encrypt(self, data, key):
        """Simple XOR encryption"""
        key_bytes = key * (len(data) // len(key) + 1)
        return bytes([data[i] ^ key_bytes[i] for i in range(len(data))])
    
    def encrypt_config(self, config_dict):
        """Encrypt configuration dictionary"""
        json_str = json.dumps(config_dict)
        key = self._derive_key()
        encrypted = self._xor_encrypt(json_str.encode(), key)
        encoded = base64.b85encode(encrypted).decode()
        return encoded
    
    def decrypt_config(self, encrypted_str):
        """Decrypt configuration string"""
        try:
            decoded = base64.b85decode(encrypted_str.encode())
            key = self._derive_key()
            decrypted = self._xor_encrypt(decoded, key)
            config = json.loads(decrypted.decode())
            return config
        except Exception as e:
            print(f"⚠ Config decryption failed: {e}")
            return None
    
    def store_encrypted(self, config_dict, filepath):
        """Store encrypted configuration to file"""
        encrypted = self.encrypt_config(config_dict)
        with open(filepath, 'w') as f:
            f.write(encrypted)
        print(f"✓ Configuration encrypted and saved to {filepath}")
    
    def load_encrypted(self, filepath):
        """Load encrypted configuration from file"""
        try:
            with open(filepath, 'r') as f:
                encrypted = f.read()
            return self.decrypt_config(encrypted)
        except FileNotFoundError:
            print(f"⚠ Config file not found: {filepath}")
            return None

# Default protected configuration
DEFAULT_CONFIG = {
    "model_paths": {
        "cost": "ml/models/rf_cost.joblib",
        "co2": "ml/models/xgb_co2.joblib",
        "preprocessing": "ml/models/preprocessing/preprocessing_pipeline.pkl"
    },
    "ranking_weights": {
        "sustainability": 0.6,
        "co2_performance": 0.4
    },
    "validation": {
        "max_weight": 1000,
        "min_weight": 0.01,
        "fragility_range": [0, 1]
    },
    "protected": True
}

# Create instance
_config_protection = ConfigProtection()

def get_protected_config():
    """Get configuration with protection"""
    config_file = os.path.join(os.path.dirname(__file__), '..', 'config', '.protected_config')
    config = _config_protection.load_encrypted(config_file)
    if not config:
        config = DEFAULT_CONFIG
        # Try to create protected config file
        try:
            _config_protection.store_encrypted(DEFAULT_CONFIG, config_file)
        except:
            pass
    return config

def save_protected_config(config_dict):
    """Save configuration with protection"""
    config_file = os.path.join(os.path.dirname(__file__), '..', 'config', '.protected_config')
    _config_protection.store_encrypted(config_dict, config_file)

# Auto-generate protected config on import
if __name__ != "__main__":
    try:
        _cfg = get_protected_config()
    except:
        _cfg = DEFAULT_CONFIG
