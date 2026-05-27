import launch
import launch_ros

from ament_index_python.packages import get_package_share_directory




def generate_launch_description():
    #执行终端的命令
    execute_command = launch.actions.ExecuteProcess(
        cmd=['ros2', 'topic', 'list'],
        output='screen'
    )
    #启动其他功能包里的launch文件
    action_inlude_path = launch.actions.IncludeLaunchDescription(
        launch.launch_description_sources.PythonLaunchDescriptionSource(
            [get_package_share_directory('turtlesim'), 'launch', 'multisim.launch.py'])
    )
    #声明参数出来
    actions_declare_log=launch.actions.DeclareLaunchArgument(
        'log',
        default_value='妈呀',
        description='日志参数'
    )
    action_group=launch.actions.GroupAction([
        launch.actions.TimerAction(
            period=5.0,
            actions=[
                action_inlude_path,
                execute_command,

            ]
        ),
        
    ])










    return launch.LaunchDescription([
        launch_ros.actions.Node(
            package='face_detect',
            executable='client_face_detect',
            name='face_detect_client',
            output='screen',
            parameters=[
                {'use_sim_time': False}
            ]
        ),
        launch_ros.actions.Node(
            package='face_detect',
            executable='srv_face_detect',
            name='face_detect',
            output='screen',
            parameters=[
                {'use_sim_time': False}
                ,
                {'log': launch.substitutions.LaunchConfiguration('log',default='>............')}
            ]
        ),
        action_group
    ])
