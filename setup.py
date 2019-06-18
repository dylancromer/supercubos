from distutils.core import setup, Extension
from Cython.Build import cythonize
import numpy




extension = Extension("csampling", ["supercubos/csampling.pyx"], include_dirs=[numpy.get_include()])

setup(name='supercubos',
      version='0.1',
      py_modules=['supercubos'],
      ext_modules = cythonize(extension, include_path=[numpy.get_include()]),
      include_dirs=[numpy.get_include()],
)
