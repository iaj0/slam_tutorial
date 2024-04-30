from launch import LaunchDescription
from launch_ros.actions import node

def generate_luanch_description():
    return LaunchDescription([
        node(
            package='demo_nodes_py',
            executable='listener',
        )
    ])