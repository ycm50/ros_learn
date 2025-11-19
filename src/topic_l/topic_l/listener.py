import rclpy
from rclpy.node import Node
from interfaces.msg import Speak
class Listener(Node):
    def __init__(self):
        super().__init__('listener')
        self.ns=self.get_namespace()
        self.subscription = self.create_subscription(Speak, self.ns+'chatter',self.listening, 10)
    def listening(self, msg):
        self.get_logger().info('I heard: "%s" with number %d' % (msg.s, msg.n))
def main(args=None):
    rclpy.init(args=args)
    listener=Listener()
    rclpy.spin(listener)
    listener.destroy_node()
    rclpy.shutdown()
