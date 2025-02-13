import os
import ast
import networkx as nx

# Set the root directory for scanning
ROOT_DIR = "backend/src"

def find_imports(file_path):
    """Extract import statements from a Python file."""
    imports = set()
    with open(file_path, "r", encoding="utf-8") as f:
        try:
            tree = ast.parse(f.read(), filename=file_path)
        except SyntaxError:
            return imports  # Skip files with syntax errors
        
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    imports.add(alias.name)
            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    imports.add(node.module)
    return imports

def build_import_graph():
    """Build a directed graph of import dependencies."""
    graph = nx.DiGraph()
    
    for root, _, files in os.walk(ROOT_DIR):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                module_name = file_path.replace("/", ".").replace(".py", "").replace("backend.src.", "src.")
                
                imports = find_imports(file_path)
                for imp in imports:
                    graph.add_edge(module_name, imp)
    
    return graph

def detect_circular_imports():
    """Detect and print circular imports in the project."""
    graph = build_import_graph()
    
    try:
        cycles = list(nx.simple_cycles(graph))
        if cycles:
            print("\n🚨 **Circular Imports Detected!** 🚨\n")
            for cycle in cycles:
                print(" 🔁 -> ".join(cycle))
            print("\n❌ **Fix these circular dependencies to avoid import errors!**")
        else:
            print("\n✅ **No circular imports detected. You're good to go!** 🎉")
    except Exception as e:
        print(f"\n⚠️ Error detecting circular imports: {e}")

if __name__ == "__main__":
    detect_circular_imports()
