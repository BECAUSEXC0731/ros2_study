import launch
import launch_ros
import os
from ament_index_python.packages import get_package_share_directory




def generate_launch_description():
    #执行终端的命令
    execute_command = launch.actions.ExecuteProcess(
        cmd=['ros2', 'topic', 'list'],
        output='screen'
    )
    execute_rqt = launch.actions.ExecuteProcess(
        condition=launch.conditions.IfCondition(
            launch.substitutions.LaunchConfiguration('rqt', default='0')
        ),
        cmd=[   'rqt'],
        output='screen'
    )
    #启动其他功能包里的launch文件
    action_inlude_path = launch.actions.IncludeLaunchDescription(
        launch.launch_description_sources.PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory('turtlesim'), 'launch', 'multisim.launch.py')
        )
    )
    #声明参数出来
    actions_declare_ifrqt=launch.actions.DeclareLaunchArgument(
        'rqt',
        default_value='0',
        description='是否启动rqt工具'
    )
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
                execute_rqt

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
                {'log': launch_ros.parameter_descriptions.ParameterValue(
                    launch.substitutions.LaunchConfiguration('log', default='>............'), 
                    value_type=str)}
            ]
        ),
        action_group
    ])
