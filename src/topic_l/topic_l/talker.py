import rclpy
from rclpy.node import Node
from interfaces.msg import Speak
class Talker(Node):
    def __init__(self):
        super().__init__('talker')
        self.ns=self.get_namespace()
        self.publisher = self.create_publisher(Speak, self.ns+'chatter', 10)
        self.timer=self.create_timer(1.0, self.speaking)
        self.num=0
    def speaking(self):
        self.num+=1
        msg=Speak()
        msg.s="hello world"
        msg.n=self.num
        self.publisher.publish(msg)
def main(args=None):
    rclpy.init(args=args)
    talker=Talker()
    rclpy.spin(talker)
    talker.destroy_node()
    rclpy.shutdown()
