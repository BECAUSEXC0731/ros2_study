import launch
import launch_ros
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():
    urdf_path = os.path.join(
        get_package_share_directory('urdf_study'), 'urdf', 'study_urdf_processed.urdf'
    )

    rviz_path = os.path.join(
        get_package_share_directory('urdf_study'), 'rviz', 'study_rviz.rviz'
    )

    world_path = os.path.join(
        get_package_share_directory('urdf_study'), 'world', 'room2.world'
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

    # 【修改1】移除 joint_state_publisher 节点
    # Gazebo 仿真中关节状态由 gazebo_ros_joint_state_publisher 插件发布
    # 保留此节点会在 Gazebo 未就绪时产生冲突的 /joint_states

    action_rviz2 = launch.actions.ExecuteProcess(
        cmd=['rviz2', '-d', rviz_path],
        output='screen'
    )

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
            'extra_gazebo_args': '--verbose -s libgazebo_ros_init.so -s libgazebo_ros_factory.so',
        }.items()
    )

    # 【修改2】增加 -timeout 参数，解决 WSL2 下 Gazebo 启动慢导致的间歇性失败
    action_spawn_entity = launch_ros.actions.Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=[
            '-topic', 'robot_description',
            '-entity', 'my_robot',
            '-z', '0.095',
            '-timeout', '120'  # ← 关键修改：从默认30秒增加到120秒
        ],
        output='screen'
    )

    return launch.LaunchDescription([
        action_robot_state_publisher,
        # joint_state_publisher 已移除
        action_rviz2,
        action_launch_gazebo,
        action_spawn_entity,
    ])