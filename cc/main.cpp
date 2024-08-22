#include <pybind11/embed.h>
#include <pybind11/pybind11.h>

#include <iostream>
#include <ostream>

namespace py = pybind11;

int main() {
  py::scoped_interpreter guard{};
  std::string version = Py_GetVersion();
  std::cout << "Python version: " << version << std::endl;

  // Print the path to the Python interpreter
  wchar_t* path = Py_GetProgramFullPath();
  std::wcout << "Python interpreter path: " << path << std::endl;

  PyObject* modules = PyImport_GetModuleDict();
  Py_ssize_t pos = 0;
  PyObject *key, *value;
  std::cout << "Printing modules: " << std::endl;
  while (PyDict_Next(modules, &pos, &key, &value)) {
    if (PyModule_Check(value)) {
      std::string name = PyModule_GetName(value);
      std::cout << "\t" << name << std::endl;
    }
  }

  std::cout << std::endl << "Trying the module." << std::endl;
  py::module my_module = py::module::import("python.my_lib.py_module");
  std::cout << "Try to run the function." << std::endl;
  py::object parquet_reader = my_module.attr("NumpyWrapper")(42);
  py::object int_value = parquet_reader.attr("get_size")();

  int cpp_int = py::int_(int_value);
  std::cout << cpp_int << std::endl;

  parquet_reader.attr("plot")();

  return 0;
}