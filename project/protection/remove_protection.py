"""
Remove Protection System (Emergency Only)
WARNING: This will remove all protection layers from your project
Only use if you need to distribute an unprotected version
"""
import os
import sys

def confirm_removal():
    """Confirm user wants to remove protection"""
    print("=" * 60)
    print("⚠️  WARNING: PROTECTION REMOVAL")
    print("=" * 60)
    print()
    print("This will remove ALL protection mechanisms from the project:")
    print("- Environment validation")
    print("- Code obfuscation")
    print("- Frontend protection")
    print("- Configuration encryption")
    print()
    print("The project will become easily copyable and forkable.")
    print()
    
    response = input("Are you SURE you want to proceed? (type 'REMOVE' to confirm): ")
    return response == "REMOVE"

def remove_protection_files():
    """Remove protection files"""
    base_dir = os.path.join(os.path.dirname(__file__), '..')
    protection_files = [
        'protection/protection.py',
        'protection/obfuscate_utils.py',
        'protection/config_protection.py',
        'protection/obfuscator.py',
        'protection/frontend/protection.js',
        'protection/setup_protection.py',
        'protection/remove_protection.py'
    ]
    
    removed = []
    for file in protection_files:
        filepath = os.path.join(base_dir, file)
        if os.path.exists(filepath):
            try:
                os.remove(filepath)
                print(f"✓ Removed: {file}")
                removed.append(file)
            except Exception as e:
                print(f"✗ Failed to remove {file}: {e}")
        else:
            print(f"⚠ Not found: {file}")
    
    return removed

def restore_original_code():
    """Instructions for restoring original code"""
    print()
    print("=" * 60)
    print("MANUAL STEPS REQUIRED")
    print("=" * 60)
    print()
    print("You need to manually edit the following files to remove")
    print("protection code and restore original functionality:")
    print()
    print("1. project/backend/app.py")
    print("   - Remove protection imports")
    print("   - Remove _P.verify() calls")
    print()
    print("2. project/backend/predict.py")
    print("   - Remove protection imports")
    print("   - Restore original VALID_CATEGORIES and VALID_SHIPPING")
    print("   - Restore original calculate_sustainability_score")
    print()
    print("3. project/frontend/index.html")
    print("   - Remove: <script src='../protection/frontend/protection.js'></script>")
    print()
    print("4. project/frontend/product.html")
    print("   - Remove: <script src='../protection/frontend/protection.js'></script>")
    print()
    print("5. project/frontend/results.html")
    print("   - Remove: <script src='../protection/frontend/protection.js'></script>")
    print()
    print("6. project/frontend/analytics.html")
    print("   - Remove: <script src='../protection/frontend/protection.js'></script>")
    print()
    print("=" * 60)

if __name__ == "__main__":
    if not confirm_removal():
        print("\n✓ Protection removal cancelled. Project remains protected.")
        sys.exit(0)
    
    print("\nRemoving protection files...")
    removed_files = remove_protection_files()
    
    print(f"\n✓ Removed {len(removed_files)} protection files")
    
    restore_original_code()
    
    print("\n⚠️  Protection system partially removed.")
    print("Complete the manual steps above to fully remove protection.")
