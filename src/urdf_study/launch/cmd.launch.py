import launch
import launch_ros
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():
    # 【修复1】统一使用小写 urdf，避免 Linux 大小写敏感导致读取失败
    # 请确保你的实际文件夹名称与此一致，若为大写请改回 'URDF'
    urdf_path = os.path.join(
        get_package_share_directory('urdf_study'), 'urdf', 'cmd_vel.urdf'
    )
    
    rviz_path = os.path.join(
        get_package_share_directory('urdf_study'), 'rviz', 'study_rviz.rviz'
    )
    
    world_path = os.path.join(
        get_package_share_directory('urdf_study'), 'world', 'study_world.sdf'
    )

    # 读取 URDF 内容并增加异常处理
    try:
        with open(urdf_path, 'r') as f:
            robot_description = f.read()
    except FileNotFoundError:
        raise FileNotFoundError(
            f"URDF file not found: {urdf_path}\n"
            "Please check the folder name case (urdf vs URDF) and filename."
        )

    action_robot_state_publisher = launch_ros.actions.Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': robot_description}]
    )

    # 【注意】仿真时建议关闭 joint_state_publisher_gui
    # 因为 Gazebo 会通过 /joint_states 发布真实关节状态
    # 同时运行两者会导致话题冲突和 TF 树震荡
    action_joint_state_publisher = launch_ros.actions.Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        name='joint_state_publisher',
        output='screen',
        # 如果确实需要 GUI 调试 URDF，可改回 True
        parameters=[{'use_gui': False}]
    )

    action_rviz2 = launch.actions.ExecuteProcess(
        cmd=['rviz2', '-d', rviz_path],
        output='screen'
    )

    # 【修复2】添加 Gazebo ROS2 桥接必需的额外参数
    action_launch_gazebo = launch.actions.IncludeLaunchDescription(
        launch.launch_description_sources.PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory('gazebo_ros'), 
                'launch', 
                'gazebo.launch.py'
            )
        ),
        launch_arguments={
            'world': world_path,
            # 关键：加载 ROS2-Gazebo 桥接插件，否则所有 gazebo_ros 插件均失效
            'extra_gazebo_args': '--verbose -s libgazebo_ros_init.so -s libgazebo_ros_factory.so',
        }.items()
    )

    action_spawn_entity = launch_ros.actions.Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=[
            '-topic', 'robot_description',
            '-entity', 'my_robot',
            # 【修复3】指定初始高度，配合 URDF 中 0.095 的底盘高度防止初始穿透
            '-z', '0.095'
        ],
        output='screen'
    )

    return launch.LaunchDescription([
        action_robot_state_publisher,
        action_joint_state_publisher,
        action_rviz2,
        action_launch_gazebo,
        action_spawn_entity,
    ])