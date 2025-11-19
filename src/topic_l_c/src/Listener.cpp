#include "rclcpp/rclcpp.hpp"
#include "interfaces/msg/speak.hpp"

class Listener : public rclcpp::Node
{
private:
    
public:
    std::string ns;
    std::string topic_name;
    rclcpp::Subscription<interfaces::msg::Speak>::SharedPtr subscription_;
    void callback(const interfaces::msg::Speak::SharedPtr msg) const;
    Listener();
    ~Listener();
};
Listener::Listener() : Node("listener")
{
    this->ns = this->get_namespace();
    this->topic_name = this->ns + "chat";
    this->subscription_ = this->create_subscription<interfaces::msg::Speak>(this->topic_name, 10, std::bind(&Listener::callback, this, std::placeholders::_1));
}
Listener::~Listener()
{
}
void Listener::callback(const interfaces::msg::Speak::SharedPtr msg) const
{
    RCLCPP_INFO(this->get_logger(), "I heard: '%s' from %ld", msg->s.c_str(), msg->n);
}

int main(int argc, char * argv[])
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<Listener>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}