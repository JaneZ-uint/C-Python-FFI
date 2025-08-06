import ctypes

lib = ctypes.CDLL('./lib/lib.so')

lib.hello.restype = None

lib.add.argtypes = [ctypes.c_int, ctypes.c_int]
lib.add.restype = ctypes.c_int

print(lib.add(826,131))

lib.hello()