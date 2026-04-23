#pragma once
#include <Eigen/Dense>
#include <iostream>

class IMUProcessor {
private:
    // 私有变量：外部无法直接访问，只能通过类内部的函数来改
    Eigen::Vector3d raw_accel_;    // 存放原始数据
    Eigen::Vector3d scaled_accel_; // 存放缩放后的数据
    double scale_factor_;          // 缩放系数

public:
    // 1. 构造函数：对象“出生”时自动调用的函数，用来做初始化
    IMUProcessor(double scale);

    // 2. 行为函数：接收新数据，并进行处理
    void updateRawAccel(double x, double y, double z);

    // 3. 行为函数：打印当前状态
    // 后面的 const 表示这是一个“只读”函数，它保证不会修改类里的数据
    void printStatus() const; 
};
