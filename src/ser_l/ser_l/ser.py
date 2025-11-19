import rclpy
from rclpy.node import Node
from interfaces.srv import Comb
class Ser(Node):
    def __init__(self):
        super().__init__('ser')
        self.ns=self.get_namespace()
        self.srv = self.create_service(Comb, self.ns+'comb', self.comb)
    def comb(self, request, response):
        response.s = request.s1 + request.s2
        self.get_logger().info("s1: %s, s2: %s, s: %s" % (request.s1, request.s2, response.s))
        return response
def main(args=None):
    rclpy.init(args=args)
    ser=Ser()
    rclpy.spin(ser)
    ser.destroy_node()
    rclpy.shutdown()
