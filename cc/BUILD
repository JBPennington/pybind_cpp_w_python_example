cc_binary(
    name = "my_cc_binary",
    srcs = ["main.cpp"],
    deps = [
        "@rules_python//python/cc:current_py_cc_headers",
        "@rules_python//python/cc:current_py_cc_libs",
        "@pybind11",
    ],
    data = [
        "//python:np_wrapper_lib",
        
    ]
)