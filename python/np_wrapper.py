from my_lib.py_module import NumpyWrapper
import sys

print(sys.executable)

if __name__ == "__main__":
    
    print(f"System Executeable: {sys.executable}")
    
    np_class = NumpyWrapper(42)
    print(np_class.get_size())