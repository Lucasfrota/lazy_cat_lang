@echo off
set PATH=C:\Program Files (x86)\Dev-Cpp\MinGW32\bin
g++ %*.cpp -o %*.exe -I"C:\Program Files (x86)\Dev-Cpp\MinGW32\include" -I"C:\Program Files (x86)\Dev-Cpp\MinGW32\lib\gcc\mingw32\4.7.2\include\c++"  -L"C:\Program Files (x86)\Dev-Cpp\MinGW32\lib" -L"C:\Program Files (x86)\Dev-Cpp\MinGW32\mingw32\lib" -static-libstdc++ -static-libgcc