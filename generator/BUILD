load("@rules_python//python:defs.bzl", "py_binary")
load("@my_deps//:requirements.bzl", "requirement")


py_binary(
  name = "main",
  srcs = ["main.py"],
  deps = [
    "//generator/name_provider:random_name_provider",
    "//generator/build_file_generator:build_file_generator",
    "//generator/code_generator:code_generator",
    "//generator/structure:structure",
  ]
)