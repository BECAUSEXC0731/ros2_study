import launch 
import launch_ros
from ament_index_python.packages import get_package_share_directory
import os





def generate_launch_description():
    #获取urdf的路径
    urdf_path = os.path.join(get_package_share_directory('urdf_study'), 'URDF', 'cmd_vel.urdf')
    rviz_path=os.path.join(get_package_share_directory('urdf_study'),'rviz','study_rviz.rviz')
    action_robot_state_publisher = launch_ros.actions.Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': open(urdf_path).read()}]
    )

    action_joint_state_publisher = launch_ros.actions.Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        name='joint_state_publisher',
        output='screen',
        parameters=[{'use_gui': True}]
    )
    
    action_rviz2=launch.actions.ExecuteProcess(
        cmd=['rviz2', '-d', rviz_path],
        output='screen'
    )

    action_launch_gazebo=launch.actions.IncludeLaunchDescription(
        launch.launch_description_sources.PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')
        ),
        launch_arguments={'world': os.path.join(get_package_share_directory('urdf_study'), 'world', 'study_world.sdf')}.items()  
    )

    action_spawn_entity=launch_ros.actions.Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=['-topic', 'robot_description', '-entity', 'my_robot'],
        output='screen'
    )

    return launch.LaunchDescription([
        action_robot_state_publisher,
        action_joint_state_publisher,
        action_rviz2,
        action_launch_gazebo,
        action_spawn_entity
         
    ])