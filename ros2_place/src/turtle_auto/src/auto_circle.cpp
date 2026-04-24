#include "rclcpp/rclcpp.hpp"
#include "geometry_msgs/msg/twist.hpp"

// 创建一个类继承自 Node
class AutoCircle : public rclcpp::Node {
public:
    AutoCircle() : Node("auto_circle_node") {
        // 1. 创建一个发布者，负责往 /turtle1/cmd_vel 这个话题发消息
        publisher_ = this->create_publisher<geometry_msgs::msg::Twist>("/turtle1/cmd_vel", 10);
        
        // 2. 创建一个定时器，每 0.1 秒执行一次 timer_callback 函数
        timer_ = this->create_wall_timer(std::chrono::milliseconds(100), 
                                         std::bind(&AutoCircle::timer_callback, this));
        RCLCPP_INFO(this->get_logger(), "自动驾驶小海龟已启动！准备画圈...");
    }

private:
    void timer_callback() {
        // 3. 定义速度消息
        auto message = geometry_msgs::msg::Twist();
        message.linear.x = 2.0;  // 线速度：往前走（米/秒）
        message.angular.z = 1.0; // 角速度：同时转弯（弧度/秒）
        
        // 4. 把消息发布出去
        publisher_->publish(message);
    }
    
    rclcpp::Publisher<geometry_msgs::msg::Twist>::SharedPtr publisher_;
    rclcpp::TimerBase::SharedPtr timer_;
};

int main(int argc, char *argv[]) {
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<AutoCircle>());
    rclcpp::shutdown();
    return 0;
}
