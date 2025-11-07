from setuptools import setup, find_packages

setup(
    name='server_report',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'psutil',
        'pywin32',
    ],
    entry_points={
        'console_scripts': [
            'server-report=server_report.main:main',
        ],
    },
    author='Lakshmanan',
    description='System health and service status report generator',
)