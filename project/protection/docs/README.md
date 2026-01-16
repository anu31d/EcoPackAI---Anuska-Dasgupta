# 🔒 EcoPackAI Protection System

## Overview

This project has been enhanced with multi-layer protection mechanisms to prevent unauthorized copying and forking while maintaining full functionality for the authorized environment.

## Protection Layers

### 1. Environment Fingerprinting
- **Hardware ID Generation**: Creates unique fingerprint based on machine characteristics
- **User Context Validation**: Validates execution environment against authorized system
- **Timestamp Checks**: Ensures code runs within valid timeframes

### 2. Code Obfuscation
- **String Encoding**: Sensitive strings are encoded using Base85 encoding
- **Variable Name Obfuscation**: Critical variables use non-descriptive names
- **Function Logic Masking**: Core algorithms wrapped in obfuscated utility functions
- **Import Hiding**: Dynamic imports prevent easy code analysis

### 3. Frontend Protection
- **Anti-Debugging**: Detects developer tools and debugging attempts
- **Console Obfuscation**: Randomizes console method availability
- **Right-Click Protection**: Partially disables context menu
- **Keyboard Shortcut Blocking**: Prevents common dev tool shortcuts
- **Source Code Protection**: Makes viewing and copying source more difficult

### 4. Configuration Encryption
- **Encrypted Config Files**: Sensitive configurations stored in encrypted format
- **XOR Encryption**: Lightweight encryption for configuration data
- **Key Derivation**: Environment-specific keys for decryption

### 5. Runtime Validation
- **Continuous Checks**: Periodic validation during execution
- **Session Tracking**: Monitors execution context
- **Fallback Modes**: Graceful degradation without exposing logic

## Setup Instructions

### Initial Setup (One-Time)

1. **Run the protection setup script**:
```bash
python project/setup_protection.py
```

2. **Set the environment variable** (copy from setup output):
```powershell
# Temporary (current session):
$env:ECOPACK_KEY='your_generated_key_here'

# Permanent (recommended):
[System.Environment]::SetEnvironmentVariable('ECOPACK_KEY', 'your_generated_key_here', 'User')
```

3. **Verify the setup**:
```bash
python project/setup_protection.py verify
```

### Running the Application

After setup, run the application normally:
```bash
cd project
python backend/app.py
```

The protection system will automatically:
- Validate your environment
- Load encrypted configurations
- Enable all obfuscation layers
- Monitor for unauthorized access attempts

## For Authorized Users (You)

### What You Need:
1. ✅ Your machine (where setup was run)
2. ✅ The `ECOPACK_KEY` environment variable set
3. ✅ Original project files intact

### Expected Behavior:
- Application runs normally
- No errors or warnings
- Full functionality available
- All features work as intended

## For Unauthorized Users (Forkers)

### What They Will Experience:
1. ⚠️ Environment validation warnings
2. ⚠️ Missing decryption keys
3. ⚠️ Obfuscated code that's hard to understand
4. ⚠️ Anti-debugging detection
5. ⚠️ Limited console access for debugging
6. ⚠️ Disabled developer tools shortcuts
7. ⚠️ Encrypted configuration files they can't read
8. ⚠️ Critical variables and functions with non-descriptive names

### They Would Need to:
- Reverse engineer the obfuscation layer
- Understand the fingerprinting system
- Decrypt protected configurations
- Bypass anti-debugging checks
- Reconstruct original variable names
- Understand the encoding schemes
- Deal with runtime validation failures

## Protection Files

### Backend Protection:
- `backend/protection.py` - Core environment validation
- `backend/obfuscate_utils.py` - Obfuscated utility functions
- `backend/config_protection.py` - Configuration encryption
- `backend/obfuscator.py` - Additional obfuscation tools
- `backend/.env_key` - Your environment key (git-ignored)

### Frontend Protection:
- `frontend/js/protection.js` - Client-side protection

### Configuration:
- `config/.protected_config` - Encrypted configuration (git-ignored)

## Security Best Practices

### DO:
✅ Keep `ECOPACK_KEY` private
✅ Add `.env_key` to `.gitignore` (already done)
✅ Run setup_protection.py on your machine only
✅ Keep protection files updated
✅ Verify setup after pulling changes

### DON'T:
❌ Commit `.env_key` to Git
❌ Share your `ECOPACK_KEY`
❌ Disable protection layers
❌ Remove obfuscation from code
❌ Commit `.protected_config` files

## Maintenance

### Updating Protection:
If you modify core logic, update the obfuscation:
```bash
python project/backend/obfuscator.py
```

### Regenerating Keys:
If you need to regenerate environment keys:
```bash
python project/setup_protection.py
```

### Checking Protection Status:
```bash
python project/setup_protection.py verify
```

## Technical Details

### Fingerprinting Algorithm:
- Combines: Machine ID + Processor + Hostname + MAC Address
- Hashes using SHA-256
- Creates 32-character unique identifier

### Obfuscation Techniques:
- Base64 encoding for strings
- Base85 encoding for complex data
- Variable name shortening
- Function wrapping
- Dynamic imports

### Encryption:
- XOR cipher with derived keys
- SHA-256 key derivation
- Base85 encoding for storage

## Troubleshooting

### "Environment validation warning"
**Solution**: Set the `ECOPACK_KEY` environment variable:
```powershell
$env:ECOPACK_KEY='your_key_here'
```

### "Protection modules not found"
**Solution**: Ensure all protection files exist in `backend/`:
- protection.py
- obfuscate_utils.py
- config_protection.py

### Configuration decryption fails
**Solution**: Regenerate protected config:
```bash
python project/setup_protection.py
```

## Legal Notice

This protection system is designed to:
1. Protect intellectual property
2. Prevent unauthorized usage
3. Maintain code confidentiality
4. Deter casual copying

**Note**: This is not military-grade encryption but provides significant deterrence against casual forking and copying attempts.

## Support

If you need to move the project to a new machine:
1. Run `setup_protection.py` on the new machine
2. Update the `ECOPACK_KEY` environment variable
3. Verify setup with `setup_protection.py verify`

---

**Remember**: Keep your environment key secure and never commit it to version control!
