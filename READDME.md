Pybind not using data dependencies given
Repo structure
. ├── MODULE.bazel ├── WORKSPACE ├── cc │ ├── BUILD │ └── main.cpp └── python ├── BUILD │ ├── my_lib │ ├── pycache │ │ └── py_module.cpython-310.pyc │ └── py_module.py ├── np_wrapper.py └── requirements.txt

Running py_binary
In this repo I try to give a simple example of the problem with using a specific python interpreter within pybind11. When we run bazel run //python:np_wrapper the np_wrapper_lib which holds a class is added as a dependency and is used properly. A python environment is installed and used. Python interpreter path is given as /home/ubuntu/.cache/bazel/_bazel_ubuntu/3e80dbd7cc6a6d46719ae059a09edcbc/execroot/_main/bazel-out/k8-fastbuild/bin/python/np_wrapper.runfiles/rules_python~0.31.0~python~python_3_10_x86_64-unknown-linux-gnu/bin/python3.

When running cc_binary
When the C++ target is run bazel run //cc:my_cc_binary the interpreter is set to /usr/bin/python3, this the numpy lib is not installed (if not on your system) and my_lib is also not found. When I look into the runfiles it seems like all needed scripts are copied but I don't know how to tell pybind/python rules to create a python interpreter with the desired libs and use it as py_binary does.

Using python py_binary
If we execute the py_binary