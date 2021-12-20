from pathlib import Path

from anytree import PostOrderIter

from generator.code_generator.code_generator import CodeGenerator
from generator.structure.structure import path_to_root


class PythonCodeGenerator(CodeGenerator):
    def __init__(self, root_path, tree, code_generator=None):
        self.code_generator = code_generator
        self.root_path = root_path
        self.tree = tree
        super()

    def generate(self):
        for node in PostOrderIter(self.tree):
            file_content = """{project_imports}
{string}_string = "{string} " {imported_strings}"""
            content = file_content.format(string=node.label,
                                          project_imports=self._generate_imports(node),
                                          imported_strings=self._generate_imported_strings(node))
            location = self.root_path + path_to_root(node, suffix=node.label + ".py")

            Path(location.rpartition('/')[0]).mkdir(parents=True, exist_ok=True)
            with open(location, "w") as file:
                file.write(content)

        if self.code_generator is not None:
            self.code_generator.generate()

    def _generate_imports(self, node):
        import_template = """from {root_path}{project}.{project} import *"""
        imports = []
        for child in node.children:
            root_path = path_to_root(node).replace("/", ".")
            imports.append(import_template.format(root_path=root_path, project=child.label))
        return "\n".join(imports)

    def _generate_imported_strings(self, node):
        string_template = """+ {}"""
        strings = []
        for child in node.children:
            strings.append(string_template.format(child.label + "_string"))
        return " ".join(strings)
