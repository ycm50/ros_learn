#include "rclcpp/rclcpp.hpp"
#include "interfaces/msg/speak.hpp"


class Speaker : public rclcpp::Node
{
private:
    
public:
    std::string ns;
    std::string topic_name;
    rclcpp::Publisher<interfaces::msg::Speak>::SharedPtr publisher_;
    rclcpp::TimerBase::SharedPtr timer_;
    void timer_callback();
    Speaker();
    ~Speaker();
private:
    // 私有成员
};

Speaker::Speaker() : Node("speaker")
{
    this->ns = this->get_namespace();
    this->topic_name = this->ns + "chat";
    this->publisher_ = this->create_publisher<interfaces::msg::Speak>(this->topic_name, 10);
    this->timer_ = this->create_wall_timer(std::chrono::seconds(1), std::bind(&Speaker::timer_callback, this));
}

Speaker::~Speaker()
{
}
void Speaker::timer_callback()
{
    static int count = 0;
    auto message = interfaces::msg::Speak();
    message.s = "hello world";
    message.n = count++;
    this->publisher_->publish(message);
}

int main(int argc, char * argv[])
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<Speaker>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}