from setuptools import setup, find_packages

import djm_client

setup(
    name=djm_client.__package__,
    version=djm_client.__version__,
    description=('Dejamobile Take Home - Client'),
    author='Antoine BUHOT',
    author_mail='buhot.a@gmail.com',
    license='MIT',
    packages=find_packages(exclude=['unit_tests',]),
    install_requires=[
        "djm-sdk"
    ],
    entry_points={
        'console_scripts': [
            'djm-client = djm_client.__main__:main'
        ]
    }
)