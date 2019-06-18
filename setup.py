from distutils.core import setup
from Cython.Build import cythonize




setup(name='supercubos',
      version='0.1',
      py_modules=['supercubos'],
      ext_modules = cythonize("supercubos/csampling.pyx")
)
