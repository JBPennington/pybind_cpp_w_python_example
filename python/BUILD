load("@rules_python//python:defs.bzl", "py_library")
load("@rules_python//python:defs.bzl", "py_binary")
load("@my_pip//:requirements.bzl", "all_requirements")

py_library(
    name = "np_wrapper_lib",
    deps = all_requirements, 
    srcs = ["my_lib/py_module.py"],
    visibility = ["//visibility:public"]
)

py_binary(
    name = "np_wrapper",
    deps =  ["np_wrapper_lib"],
    srcs = ["np_wrapper.py"],
    visibility = ["//visibility:public"],
)
