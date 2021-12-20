from pathlib import Path

from anytree import PostOrderIter

from generator.build_file_generator.build_file_generator import BuildFileGenerator
from generator.structure.structure import path_to_root


class PythonBuildFileGenerator(BuildFileGenerator):
    def __init__(self, root_path, tree, build_file_generator=None):
        self.build_file_generator = build_file_generator
        self.root_path = root_path
        self.tree = tree
        super()

    def generate(self):
        for node in PostOrderIter(self.tree):
            build_file_content = """load("@rules_python//python:defs.bzl", "py_binary")
        
py_binary(
  name = "{name}",
  srcs = ["{srcs}"],
  deps = [{deps}],
  visibility = ["//visibility:public"],
)
"""
            deps = node.children
            print("deps")
            print([a for a in deps])
            targets = ["\"" + self._bazel_target(n) + "\"" for n in deps]
            targets = ", ".join(targets)

            content = build_file_content.format(name=node.label, deps=targets, srcs=node.label + ".py")
            location = self.root_path + path_to_root(node, suffix="BUILD")

            Path(location.rpartition('/')[0]).mkdir(parents=True, exist_ok=True)
            with open(location, "w+") as file:
                file.write(content)

        location = self.root_path + "WORKSPACE"
        content = """load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "rules_python",
    url = "https://github.com/bazelbuild/rules_python/releases/download/0.5.0/rules_python-0.5.0.tar.gz",
    sha256 = "cd6730ed53a002c56ce4e2f396ba3b3be262fd7cb68339f0377a45e8227fe332",
)

load("@rules_python//python:pip.bzl", "pip_install")

pip_install(
   name = "my_deps",
   requirements = "//:requirements.txt",
)
"""
        with open(location, "w+") as file:
            file.write(content)

        if self.build_file_generator is not None:
            self.build_file_generator.generate()

    def _bazel_target(self, node):
        return "//" + path_to_root(node)[:-1] + ":" + node.label
