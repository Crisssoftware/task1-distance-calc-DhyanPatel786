import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from std_msgs.msg import Float32
import math

class DistanceCalculator(Node):
    def __init__(self):            #sets up the node needed for the program
        super().__init__('distance_calculator')
        self.subscription = self.create_subscription(
            Pose,                  #sees the turtles position
            '/turtle1/pose',       #this listen to incoming messages about the position
            self.pose_callback,    #its a function which is called when a message arrives(meaning whena new message is given to turtle1/pos the callback fucntion is called )
            10)                    #buffer of messages(like there is a wsiting room for 10 messages)
        self.publisher = self.create_publisher(Float32, '/turtle1/distance_from_origin', 10)  #it will send the computed data to turtle1/distance_from_origin
        self.get_logger().info("Distance Calculator Node Started")                            #signals that the node has started successfully if it was not shown then there was error in this part

    def pose_callback(self, msg):                           #calculated the distance and gives output of the caculation
                                                            #actaully calculated teh distance from the origin
        distance = math.sqrt(msg.x ** 2 + msg.y ** 2)

                                                            # Publish the distance
        distance_msg = Float32()                            #sets data type of the computed distance in this case its flaot
        distance_msg.data = distance
        self.publisher.publish(distance_msg)

                                                            #give output of the calculated distance
        self.get_logger().info(f'Distance from Origin: {distance:.2f}')

def main(args=None):
    rclpy.init(args=args)
    node = DistanceCalculator()
    rclpy.spin(node)                                        #keep the node in  a loop thus it goes on till it's manually interupted by ctrl + c
    node.destroy_node()
    rclpy.shutdown()                                        #shutsdown the program and ends it and clears all the memory used in the program

if __name__ == '__main__':                                  #the program stars here and starts teh main fucntion
    main()
