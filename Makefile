CXX = g++
CXX += -I/Users/christopherrogan/GitHub/matplotlib-cpp/
#CXX += -I/usr/local/Cellar/python/3.7.1/Frameworks/Python.framework/Versions/3.7/include/python3.7m/
CXX += -I/usr/local/Cellar/python\@3.9/3.9.1_6/Frameworks/Python.framework/Versions/3.9/include/python3.9/
CXX += -I/usr/local/lib/python3.9/site-packages/numpy/core/include

GLIBS =  -L/usr/local/Cellar/python\@3.9/3.9.1_6/Frameworks/Python.framework/Versions/3.9/lib/
GLIBS += -lpython3.9

CXXFLAGS = -std=c++14

SRCDIR = ./src/

all: Random_matplotlib.x

Random_matplotlib.x:  $(SRCDIR)Random_matplotlib.C
	$(CXX) $(CXXFLAGS) -o Random_matplotlib.x $(GLIBS) $ $<
	touch MakeReducedNtuple.x

clean:
	rm -f *.x
	rm -rf *.dSYM
