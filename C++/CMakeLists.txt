cmake_minimum_required(VERSION 3.25)
project(GTS)

set(CMAKE_CXX_STANDARD 14)

add_executable(GTS
        Lagrange.cpp Newton.cpp "Simpson.cpp" HinhThang.cpp Chiadoi.cpp PPLap.cpp Gauss_Jordan.cpp Jacobi_Iteration.cpp Gauss_Seidei.cpp Daycung.cpp Tieptuyen.cpp)
