#include "imu.h" // 引入刚才写的说明书

// 实现构造函数：用传入的 scale 初始化 scale_factor_，并把向量归零
IMUProcessor::IMUProcessor(double scale) : scale_factor_(scale) {
    raw_accel_ = Eigen::Vector3d::Zero();
    scaled_accel_ = Eigen::Vector3d::Zero();
}

// 实现更新函数
void IMUProcessor::updateRawAccel(double x, double y, double z) {
    // 1. 更新原始数据（Eigen 的简洁语法，直接赋值）
    raw_accel_ << x, y, z;
    
    // 2. 进行缩放计算，结果存入 scaled_accel_
    scaled_accel_ = raw_accel_ * scale_factor_;
}

// 实现打印函数
void IMUProcessor::printStatus() const {
    std::cout << "------------------------" << std::endl;
    std::cout << "原始数据: \n" << raw_accel_ << std::endl;
    std::cout << "缩放后数据: \n" << scaled_accel_ << std::endl;
    // 调用 Eigen 自带的求模长函数 .norm()
    std::cout << "总加速度大小: " << scaled_accel_.norm() << " g" << std::endl;
    std::cout << "------------------------\n" << std::endl;
}
