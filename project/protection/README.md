# 🔒 Protection System

This folder contains all protection mechanisms for EcoPackAI.

## Structure

```
protection/
├── protection.py           # Core environment validation
├── obfuscate_utils.py      # Obfuscation utilities
├── config_protection.py    # Configuration encryption
├── obfuscator.py           # Additional obfuscation tools
├── setup_protection.py     # Setup script (run this first!)
├── remove_protection.py    # Emergency removal script
├── .env_key               # Your environment key (git-ignored)
├── frontend/
│   └── protection.js       # Frontend protection
└── docs/
    ├── README.md           # Full documentation
    ├── QUICKSTART.md       # Quick start guide
    ├── SUMMARY.md          # Implementation summary
    ├── VISUAL.md           # Visual overview
    └── WHAT_FORKERS_SEE.md # Forker experience

```

## Quick Start

### First Time Setup

1. **Run setup**:
   ```bash
   cd project/protection
   python setup_protection.py
   ```

2. **Set environment variable** (from setup output):
   ```powershell
   $env:ECOPACK_KEY='your_generated_key_here'
   ```

3. **Verify**:
   ```bash
   python setup_protection.py verify
   ```

### Daily Usage

Just run your application normally - protection is automatic!

```bash
cd project
python backend/app.py
```

## Documentation

- **Full Guide**: [docs/README.md](docs/README.md)
- **Quick Start**: [docs/QUICKSTART.md](docs/QUICKSTART.md)
- **Visual Overview**: [docs/VISUAL.md](docs/VISUAL.md)
- **What Forkers See**: [docs/WHAT_FORKERS_SEE.md](docs/WHAT_FORKERS_SEE.md)

## How It Works

### Backend Integration
Backend files import from this folder:
```python
from protection.protection import _P, _INSTANCE_ID
from protection.obfuscate_utils import _O, _calculate_score
```

### Frontend Integration
HTML files include the protection script:
```html
<script src="../protection/frontend/protection.js"></script>
```

## Protection Layers

1. ✅ **Environment Fingerprinting** - Machine-specific validation
2. ✅ **Code Obfuscation** - Hard-to-read code
3. ✅ **Configuration Encryption** - Protected settings
4. ✅ **Frontend Protection** - Anti-debugging
5. ✅ **Runtime Validation** - Continuous checks

## Important Files

- **`.env_key`** - DO NOT commit! (already in .gitignore)
- **`protection.py`** - Core validation logic
- **`setup_protection.py`** - Run once to setup

## Current Status

**Environment Key**: Set via `ECOPACK_KEY` environment variable
**Status**: ✅ Active and working
**Location**: `project/protection/`

---

For more details, see [docs/README.md](docs/README.md)
