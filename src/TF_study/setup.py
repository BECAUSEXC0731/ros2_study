from setuptools import find_packages, setup

package_name = 'TF_study'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='xc2204',
    maintainer_email='xc2204@todo.todo',
    description='TODO: Package description',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'static_tf_broadcaster = TF_study.static_TF_broadcast:main',
            'dynamic_tf_broadcaster = TF_study.dynamic_TF_broadcast:main',
            'tf_listen = TF_study.tf_listen:main',
        ],
    },
)
