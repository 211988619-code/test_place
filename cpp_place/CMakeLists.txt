cmake_minimum_required(VERSION 3.10)
project(IMU_OOP_Test) # 项目名字顺便改个有意义的
set(CMAKE_CXX_STANDARD 14)

# 找 Eigen
find_package(Eigen3 REQUIRED)

# ==========================================
# 1. 制作零件（注意这里的源文件变成了 imu.cpp，零件名叫 imu_lib）
# ==========================================
add_library(imu_lib src/imu.cpp)
target_include_directories(imu_lib PUBLIC include)
target_link_libraries(imu_lib PUBLIC Eigen3::Eigen)

# ==========================================
# 2. 组装成品
# ==========================================
add_executable(imu_test src/main.cpp)

# ==========================================
# 3. 链接零件（注意链接的是 imu_lib）
# ==========================================
target_link_libraries(imu_test PRIVATE imu_lib)
