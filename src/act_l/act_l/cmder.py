import rclpy
from rclpy.node import Node
from interfaces.action import Trans
from rclpy.action import ActionClient

class Cmder(Node):
    def __init__(self):
        super().__init__('cmder')
        self.action_client = ActionClient(
            self,
            Trans,
            'trans')
        self.action_client.wait_for_server(timeout_sec=1.0)
    
    def send_goal(self, s1):
        # Only set s1 in the goal (matching the action definition)
        goal_msg = Trans.Goal()
        goal_msg.s1 = s1
        
        # Send goal and wait for result
        self.future = self.action_client.send_goal_async(goal_msg)
        rclpy.spin_until_future_complete(self, self.future)
        goal_handle = self.future.result()
        
        if not goal_handle.accepted:
            self.get_logger().info('Goal rejected')
            return
            
        self.get_logger().info('Sending goal: %s' % s1)
        
        # Wait for result
        self.result_future = goal_handle.get_result_async()
        rclpy.spin_until_future_complete(self, self.result_future)
        result = self.result_future.result().result
        
        # Use the correct field name for the result
        self.get_logger().info('Result: %s' % result.s2)

def main(args=None):
    rclpy.init(args=args)
    cmder = Cmder()
    cmder.send_goal('4563')  # Only pass s1
    cmder.destroy_node()
    rclpy.shutdown()