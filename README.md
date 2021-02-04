# PHSX815 Spring 2021 Week 1 

## Random number generation and data visualization

This repository contains three examples (coded in three different
ways) that illustrates random number generation and simple data
visualization (plotting). Three different plotting libraries are used
(which requires users to independently download and setup/install
these libraries - instructions at the links below)

- [matplotlib](https://matplotlib.org/) (Python)
- [matplotlib](https://matplotlib-cpp.readthedocs.io/en/latest/
) (C++)
- [ROOT](https://root.cern/) (C++)

## Example usage

### [matplotlib](https://matplotlib.org/) (Python)

The python file `python/Random_python.py` can be run from the command
line by typing:

	<> python python/Random_python.py

This requires a working Python distribution (so that the `python`
executable exists) with the Python package `numpy` also installed.

### [matplotlib](https://matplotlib-cpp.readthedocs.io/en/latest/
) (C++)

The C++ source file `src/Random_matplotlib.C` can be compiled into an
executable by changing directories to the main folder of this
repository (the folder containing the file `Makefile`) and typing:

	<> make

In order for this to be successful, users need to edit the `Makefile`
in order to include the correct paths to
- the `matplotlib-cpp` GitHub package
- the header files (in the `include` folder) for Python
- the header files for `numpy`
- the shared library for python
Users can see the
[matplotlib (C++) documentaion](https://matplotlib-cpp.readthedocs.io/en/latest/)
for more information about where to find these folders on their
machine.

This will create the `Random_matplotlib.x`, executable which can be
run from the command line by typing:

	<> ./Random_matplotlib.x

### [ROOT](https://root.cern/) (C++)

The C++ macro `macros/Random_ROOT.C`is set up to run in the `ROOT`
command line interpreter environment. To use this functionality, users
must first download and install `ROOT` on their machine (this will
create shared libraries and header files that can be used in compiled
C++ code, like the previous example, and the `root` executable).

To enter the `ROOT` command line environment users can type:

	<> root

From the `ROOT` command line users can then run the
`macros/Random_ROOT.C` macro by typing:

	<> .x macros/Random_ROOT.C+
