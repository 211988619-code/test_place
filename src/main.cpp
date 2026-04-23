#include <iostream>

int main() {
    std::cout << "IMU 数据处理模块启动..." << std::endl;
    float accel[3] = {0.1, 0.0, -9.8};
    std::cout << "当前加速度: x=" << accel[0] << ", y=" << accel[1] << ", z=" << accel[2] << std::endl;
    return 0;
}
