load("@rules_python//python:defs.bzl", "py_library")
load("@my_deps//:requirements.bzl", "requirement")


py_library(
  name = "structure",
  srcs = ["structure.py"],
  deps = [
      requirement("anytree"),
  ],
  visibility = ["//visibility:public"],
)