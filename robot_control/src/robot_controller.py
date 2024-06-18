import rospy
from geometry_msgs.msg import PoseStamped
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import actionlib

class RobotController:
    def __init__(self):
        rospy.init_node('robot_controller', anonymous=True)
        self.client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
        self.client.wait_for_server()

    def send_goal(self, x, y, z, w):
        goal = MoveBaseGoal()
        goal.target_pose.header.frame_id = "map"
        goal.target_pose.header.stamp = rospy.Time.now()
        goal.target_pose.pose.position.x = x
        goal.target_pose.pose.position.y = y
        goal.target_pose.pose.orientation.z = z
        goal.target_pose.pose.orientation.w = w

        self.client.send_goal(goal)
        self.client.wait_for_result()
        return self.client.get_result()

    def go_to_seat1(self):
        self.send_goal(5.0, 5.0, 0.707, 0.707)

    def go_to_seat2(self):
        self.send_goal(5.0, -5.0, 0.707, 0.707)

    def go_to_seat3(self):
        self.send_goal(10.0, 5.0, 0.707, 0.707)

    def go_to_seat4(self):
        self.send_goal(10.0, -5.0, 0.707, 0.707)

    def return_to_origin(self):
        self.send_goal(0.0, 0.0, 0.0, 1.0)


