from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    pkg = get_package_share_directory("scope89_ptz")
    
    urdf_file = os.path.join(pkg, "urdf", "scope89_ptz.urdf")
    with open(urdf_file, 'r') as f:
        robot_desc = f.read()
    
    ros2ctrl = os.path.join(pkg, "config", "ptz_ros2_controllers.yaml")
    sim_time = {"use_sim_time": True}
    
    # Robot State Publisher for PTZ
    ptz_rsp = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        namespace="ptz_camera",
        parameters=[
            {"robot_description": robot_desc},
            sim_time
        ],
        output="screen",
    )
    
    # ros2_control node for PTZ
    ptz_control = Node(
        package="controller_manager",
        executable="ros2_control_node",
        namespace="ptz_camera",
        parameters=[
            {"robot_description": robot_desc},
            ros2ctrl,
            sim_time
        ],
        output="screen",
    )
    
    # Joint state broadcaster spawner
    sp_js = Node(
        package="controller_manager",
        executable="spawner",
        arguments=[
            "ptz_joint_state_broadcaster",
            "--controller-manager", "/ptz_camera/controller_manager"
        ],
        output="screen"
    )
    
    # PTZ controller spawner (initially inactive)
    sp_ptz = Node(
        package="controller_manager",
        executable="spawner",
        arguments=[
            "ptz_controller",
            "--controller-manager", "/ptz_camera/controller_manager",
            "--inactive"  # Don't activate yet
        ],
        output="screen"
    )
    
    return LaunchDescription([
        ptz_rsp,
        ptz_control,
        sp_js,
        sp_ptz,
    ])