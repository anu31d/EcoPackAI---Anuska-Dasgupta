"""
Obfuscated utility functions for core operations
"""
import base64
import hashlib
import json

class _O:
    """Obfuscated operations handler"""
    
    @staticmethod
    def _e(data):
        """Encode data"""
        try:
            _s = json.dumps(data) if not isinstance(data, str) else data
            _b = base64.b85encode(_s.encode()).decode()
            return _b
        except:
            return None
    
    @staticmethod
    def _d(data):
        """Decode data"""
        try:
            _b = base64.b85decode(data.encode()).decode()
            try:
                return json.loads(_b)
            except:
                return _b
        except:
            return None
    
    @staticmethod
    def _h(data):
        """Hash data"""
        return hashlib.sha256(str(data).encode()).hexdigest()
    
    @staticmethod
    def _x(_a, _b, _c=1):
        """Obfuscated calculation"""
        try:
            return (_a * _c + _b * (1 - _c)) if _c <= 1 else _a + _b
        except:
            return 0

def _calculate_score(_params):
    """Obfuscated scoring function"""
    _w = [0.4, 0.4, 0.2]
    _v = []
    for _k in ['biodegradability', 'recyclability', 'renewable']:
        _val = _params.get(_k, 50)
        if _k == 'renewable':
            _val = 80 if _val else 20
        _v.append(_val)
    
    _score = sum(_O._x(_v[i], _w[i], 1) * _w[i] for i in range(len(_w)))
    return round(_score, 2)

def _apply_weights(_data, _weights):
    """Apply weighted calculation"""
    _result = 0
    for _k, _w in _weights.items():
        if _k in _data:
            _result += _data[_k] * _w
    return _result

# Obfuscated constants
_VALID_CATS = _O._e(["Food", "Electronics", "Cosmetics", "Pharmacy"])
_VALID_SHIP = _O._e(["Air", "Road", "Sea"])
_CONFIG_HASH = _O._h("ecopack_config_v1")
