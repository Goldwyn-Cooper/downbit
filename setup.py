from setuptools import setup, find_packages

setup(
    name='downbit',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests',
        'pandas'
    ],
)