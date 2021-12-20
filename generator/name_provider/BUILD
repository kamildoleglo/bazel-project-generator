load("@rules_python//python:defs.bzl", "py_library")
load("@my_deps//:requirements.bzl", "requirement")


py_library(
  name = "random_name_provider",
  srcs = ["random_name_provider.py", "name_provider.py"],
  deps = [
    requirement("random-word"),
    requirement("pyyaml"),
  ],
  visibility = ["//visibility:public"],
)