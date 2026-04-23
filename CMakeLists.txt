# 1. 规定 CMake 最低版本
cmake_minimum_required(VERSION 3.10)

# 2. 给这个项目起个名字
project(IMU_Test)

# 3. 指定 C++ 标准（现在默认都用 C++14 或 11）
set(CMAKE_CXX_STANDARD 14)

# 4. 生成一个可执行文件
# 格式：add_executable(生成的程序名  源代码路径)
add_executable(imu_test src/main.cpp)
