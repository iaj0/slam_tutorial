from launch import LaunchDescription
from launch_ros.actions import Node

def generate_luanch_description():
    return LaunchDescription([
        Node(
            package='demo_nodes_cpp',
            executable='talker',
        )
    ])