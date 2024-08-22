# Embedded python example

## Update your requirements_lock.txt
This must be done first! This must be re-run anytime your python version is changed.
`bazel run //python:requirements.update`

## Running py_binary
`bazel run //python:np_wrapper` 

## Running cc_binary
`bazel run //cc:my_cc_binary`
