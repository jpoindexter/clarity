import os
import ast

# Function to get all Python files
def get_python_files(directory):
    py_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                py_files.append(os.path.join(root, file))
    return py_files

# Function to parse imports from a file
def parse_imports(filepath):
    imports = []
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            tree = ast.parse(f.read(), filename=filepath)
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        imports.append(alias.name)
                elif isinstance(node, ast.ImportFrom):
                    imports.append(node.module)
    except Exception as e:
        print(f"Error parsing {filepath}: {e}")
    return imports

# Function to detect circular dependencies
def detect_circular_imports(directory):
    imports_map = {}
    py_files = get_python_files(directory)

    for file in py_files:
        rel_path = os.path.relpath(file, directory)
        imports_map[rel_path] = parse_imports(file)

    circular_dependencies = []
    for file, imports in imports_map.items():
        for imp in imports:
            imp_file = f"{imp.replace('.', '/')}.py"
            if imp_file in imports_map and file in imports_map[imp_file]:
                circular_dependencies.append((file, imp_file))

    return circular_dependencies

# Main execution
if __name__ == "__main__":
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src"))
    circular_deps = detect_circular_imports(project_root)

    if circular_deps:
        print("❌ Circular imports detected:")
        for dep in circular_deps:
            print(f"🔁 {dep[0]} <-> {dep[1]}")
    else:
        print("✅ No circular imports detected.")
