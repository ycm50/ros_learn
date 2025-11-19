import rclpy
from rclpy.node import Node
from interfaces.action import Trans
from rclpy.action import ActionServer

class Doer(Node):
    def __init__(self):
        super().__init__('doer')
        self.action_server = ActionServer(
            self,
            Trans,
            'trans',
            self.execute_callback)
    
    def execute_callback(self, goal_handle):
        self.get_logger().info('Executing goal...')
        
        # Only use s1 from the request
        s1 = goal_handle.request.s1
        
        # Create feedback with s3 field (matching the action definition)
        feedback_msg = Trans.Feedback()
        feedback_msg.s3 = s1  # Use s3 instead of partial_trans
        goal_handle.publish_feedback(feedback_msg)
        self.get_logger().info('Feedback: %s' % feedback_msg.s3)
        
        # Set result with s2 field (matching the action definition)
        goal_handle.succeed()
        result_msg = Trans.Result()
        result_msg.s2 = s1  # Use s2 for the result
        
        self.get_logger().info('Result: %s' % result_msg.s2)
        return result_msg  # Return the result

def main(args=None):
    rclpy.init(args=args)
    doer = Doer()
    rclpy.spin(doer)
    doer.destroy_node()
    rclpy.shutdown()