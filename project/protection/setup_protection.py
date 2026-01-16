"""
Protection Setup Script
Run this once to configure your environment-specific protection
"""
import os
import sys
import hashlib
import uuid
import platform
import socket

def generate_environment_key():
    """Generate a unique key based on your machine"""
    machine_id = f"{platform.machine()}{platform.processor()}{socket.gethostname()}{uuid.getnode()}"
    env_key = hashlib.sha256(machine_id.encode()).hexdigest()[:32]
    return env_key

def setup_protection():
    """Setup protection for your environment"""
    print("=" * 60)
    print("EcoPackAI Protection Setup")
    print("=" * 60)
    print()
    
    # Generate environment key
    env_key = generate_environment_key()
    print(f"✓ Generated environment key: {env_key[:16]}...")
    print()
    
    # Create instructions
    print("SETUP INSTRUCTIONS:")
    print("-" * 60)
    print("1. Add this to your system environment variables:")
    print()
    print(f"   ECOPACK_KEY={env_key}")
    print()
    print("   On Windows (PowerShell):")
    print(f"   $env:ECOPACK_KEY='{env_key}'")
    print()
    print("   Or add permanently:")
    print(f"   [System.Environment]::SetEnvironmentVariable('ECOPACK_KEY', '{env_key}', 'User')")
    print()
    print("2. This key ties the application to YOUR machine")
    print("3. Anyone else trying to run this will get warnings")
    print("4. Keep this key secret and don't commit it to Git")
    print()
    print("-" * 60)
    
    # Save key to local file (gitignored)
    key_file = os.path.join(os.path.dirname(__file__), '.env_key')
    try:
        with open(key_file, 'w') as f:
            f.write(f"ECOPACK_KEY={env_key}\n")
            f.write(f"# Generated on: {platform.node()}\n")
            f.write(f"# Date: {__import__('datetime').datetime.now()}\n")
        print(f"✓ Key saved to: {key_file}")
        print("  (Make sure this file is in .gitignore)")
    except Exception as e:
        print(f"⚠ Could not save key file: {e}")
    
    print()
    print("=" * 60)
    print("Setup complete! Your project is now protected.")
    print("=" * 60)
    
    return env_key

def verify_setup():
    """Verify that protection is properly configured"""
    print("\nVerifying protection setup...")
    
    checks = []
    
    # Check 1: Environment variable
    env_key = os.environ.get('ECOPACK_KEY')
    if env_key:
        print("✓ ECOPACK_KEY environment variable is set")
        checks.append(True)
    else:
        print("✗ ECOPACK_KEY environment variable NOT set")
        checks.append(False)
    
    # Check 2: Protection modules exist
    protection_dir = os.path.dirname(__file__)
    protection_files = ['protection.py', 'obfuscate_utils.py', 'config_protection.py']
    
    for file in protection_files:
        filepath = os.path.join(protection_dir, file)
        if os.path.exists(filepath):
            print(f"✓ {file} exists")
            checks.append(True)
        else:
            print(f"✗ {file} NOT found")
            checks.append(False)
    
    # Check 3: Frontend protection
    frontend_protection = os.path.join(protection_dir, 'frontend', 'protection.js')
    if os.path.exists(frontend_protection):
        print(f"✓ Frontend protection.js exists")
        checks.append(True)
    else:
        print(f"✗ Frontend protection.js NOT found")
        checks.append(False)
    
    print()
    if all(checks):
        print("✓ All protection systems are in place!")
        return True
    else:
        print("⚠ Some protection components are missing")
        return False

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "verify":
        verify_setup()
    else:
        key = setup_protection()
        print("\nRun 'python setup_protection.py verify' to check setup")
