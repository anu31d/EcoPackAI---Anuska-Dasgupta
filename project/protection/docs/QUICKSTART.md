# 🔒 Protection Quick Start Guide

## Setup (First Time Only)

1. **Run setup script**:
   ```bash
   cd project
   python setup_protection.py
   ```

2. **Copy the environment variable command from output and run it**:
   ```powershell
   $env:ECOPACK_KEY='your_generated_key_here'
   ```

3. **Verify**:
   ```bash
   python setup_protection.py verify
   ```

## Daily Usage

Just run your application normally:
```bash
cd project
python backend/app.py
```

The protection is automatic - no extra steps needed!

## What's Protected?

✅ **Backend Code**:
- Environment fingerprinting
- Obfuscated calculations
- Encrypted configurations
- Runtime validation

✅ **Frontend Code**:
- Anti-debugging
- Console obfuscation
- Dev tools blocking
- Source protection

✅ **Configuration**:
- Encrypted config files
- Environment-specific keys

## If Someone Tries to Fork

They will encounter:
- ⚠️ Environment validation warnings
- ⚠️ Obfuscated code
- ⚠️ Missing encryption keys
- ⚠️ Anti-debugging alerts
- ⚠️ Disabled dev tools

## Key Files (DO NOT COMMIT)

❌ `backend/.env_key` - Your environment key
❌ `config/.protected_config` - Encrypted settings
❌ Any file with your `ECOPACK_KEY`

These are already in `.gitignore` ✅

## Quick Checks

**Is protection working?**
```bash
python setup_protection.py verify
```

**Environment variable set?**
```powershell
echo $env:ECOPACK_KEY
```

**All files present?**
- ✅ `backend/protection.py`
- ✅ `backend/obfuscate_utils.py`
- ✅ `backend/config_protection.py`
- ✅ `frontend/js/protection.js`

## Troubleshooting

**Warning: "Environment validation notice"**
→ Set `ECOPACK_KEY`: `$env:ECOPACK_KEY='your_key'`

**Protection not working?**
→ Run: `python setup_protection.py verify`

## Moving to New Machine

1. Copy project files
2. Run `setup_protection.py` on new machine
3. Set new `ECOPACK_KEY`
4. Done!

---

**Remember**: This protection makes your code significantly harder to copy, but not impossible. Keep sensitive data secure!
