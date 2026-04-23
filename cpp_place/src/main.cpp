#include <iostream>
#include "imu.h"

int main() {
    std::cout << "=== 面向对象 IMU 测试程序 ===" << std::endl;

    // 1. 实例化一个对象，就像造了一台真实的 IMU 设备
    // 传入系数 0.001，这会自动调用构造函数
    IMUProcessor my_imu(0.001);

    // 2. 模拟第一次收到传感器数据
    std::cout << "[第一次更新数据]" << std::endl;
    my_imu.updateRawAccel(12345.0, 67890.0, 987.0);
    my_imu.printStatus(); // 对象自己会打印自己的状态

    // 3. 模拟第二次收到传感器数据
    // 注意：对象 my_imu 一直“活”着，它内部的数据被自动更新了
    std::cout << "[第二次更新数据]" << std::endl;
    my_imu.updateRawAccel(500.0, -200.0, 9800.0);
    my_imu.printStatus();

    return 0;
}
