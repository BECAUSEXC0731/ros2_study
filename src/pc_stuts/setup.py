from setuptools import find_packages, setup

package_name = 'pc_stuts'

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
    license='test_pkg/LICENSE',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'stuts_pub = pc_stuts.stuts_pub:main',
            'stuts_sub = pc_stuts.stuts_sub:main',
            'qt_ui = pc_stuts.qt_ui:main',
        ],
    },
)
