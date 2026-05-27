from setuptools import find_packages, setup
import glob

package_name = 'face_detect'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # 安装 resource 目录下的所有图片文件
        ('share/' + package_name + '/resource', glob.glob('resource/*.png')),
        ('share/' + package_name + '/launch', glob.glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='xc2204',
    maintainer_email='xc2204@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
                'srv_face_detect = face_detect.srv_face_detect:main',
                'client_face_detect = face_detect.client_face_detect:main',
                'video_detect = face_detect.video_detect:main',
        ],
    },
)
