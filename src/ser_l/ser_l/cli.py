import rclpy
from rclpy.node import Node
from interfaces.srv import Comb
class Cli(Node):
    def __init__(self):
        super().__init__('cli')
        self.ns=self.get_namespace()
        self.cli = self.create_client(Comb, self.ns+'comb')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = Comb.Request()
    def send_request(self, s1, s2):
        self.req.s1 = s1
        self.req.s2 = s2

        self.future = self.cli.call_async(self.req)
        rclpy.spin_until_future_complete(self, self.future)
        self.get_logger().info("s: %s" % self.future.result().s)
def main(args=None):
    rclpy.init(args=args)
    cli=Cli()
    s1=""
    s2=""
    while s1!="exit" and s2!="exit":
        s1=input("input s1: ")
        s2=input("input s2: ")
        cli.send_request(s1, s2)
    rclpy.shutdown()
    cli.destroy_node()