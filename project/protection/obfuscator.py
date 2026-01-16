"""
Code Obfuscator Utility
Use this to further obfuscate sensitive Python files
"""
import base64
import zlib
import marshal
import py_compile
import os

def obfuscate_string(text):
    """Obfuscate a string using multiple encoding layers"""
    # Layer 1: Base64
    encoded = base64.b64encode(text.encode()).decode()
    # Layer 2: Reverse
    reversed_text = encoded[::-1]
    # Layer 3: Base85
    final = base64.b85encode(reversed_text.encode()).decode()
    return final

def deobfuscate_string(obfuscated):
    """Deobfuscate a string"""
    # Reverse Layer 3
    decoded = base64.b85decode(obfuscated.encode()).decode()
    # Reverse Layer 2
    unreversed = decoded[::-1]
    # Reverse Layer 1
    original = base64.b64decode(unreversed.encode()).decode()
    return original

def create_obfuscated_import(module_name, function_name):
    """Create obfuscated import statement"""
    import_str = f"from {module_name} import {function_name}"
    obf = obfuscate_string(import_str)
    return f"exec(__import__('base64').b85decode('{obf}'.encode()).decode()[::-1].encode()).decode()"

def compile_to_pyc(source_file, output_file=None):
    """Compile Python file to bytecode"""
    if output_file is None:
        output_file = source_file + 'c'
    try:
        py_compile.compile(source_file, output_file, doraise=True)
        print(f"✓ Compiled {source_file} to {output_file}")
        return True
    except Exception as e:
        print(f"✗ Failed to compile {source_file}: {e}")
        return False

def obfuscate_variable_names(code, var_mapping=None):
    """Replace variable names with obfuscated versions"""
    if var_mapping is None:
        var_mapping = {
            'materials_df': '_m_df',
            'preprocessing_pipeline': '_pp_pipe',
            'rf_cost_model': '_rf_m',
            'xgb_co2_model': '_xgb_m',
            'ranking_config': '_r_cfg',
            'sustainability_score': '_sus_sc',
            'co2_performance_score': '_co2_sc'
        }
    
    obfuscated_code = code
    for original, obfuscated in var_mapping.items():
        obfuscated_code = obfuscated_code.replace(original, obfuscated)
    
    return obfuscated_code

# Example usage
if __name__ == "__main__":
    print("Code Obfuscator Utility")
    print("=" * 50)
    
    # Example: Obfuscate a string
    test_str = "SELECT * FROM materials WHERE type = 'biodegradable'"
    obf = obfuscate_string(test_str)
    print(f"Original: {test_str}")
    print(f"Obfuscated: {obf}")
    print(f"Deobfuscated: {deobfuscate_string(obf)}")
    print()
    
    # Example: Create obfuscated import
    obf_import = create_obfuscated_import("pandas", "DataFrame")
    print(f"Obfuscated import: {obf_import}")
