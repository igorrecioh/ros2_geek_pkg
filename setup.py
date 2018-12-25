from setuptools import setup

package_name = 'ros2_geek_pkg'

setup(
    name=package_name,
    version='0.0.1',
    packages=[],
    py_modules=[
        'geek_publisher',
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    author='Igor Recio',
    author_email='igor.recio.h@gmail.com',
    maintainer='Igor Recio',
    maintainer_email='igor.recio.h@gmail.com',
    keywords=['ROS2'],
    classifiers=[
        'Intended Audience :: Beginners',
        'License :: None',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description='First ROS2 package',
    license='None',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'geek_publisher = geek_publisher:main',
        ],
    },
)
