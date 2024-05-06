from setuptools import setup, find_packages

setup(
    name="dundie",
    version="0.1.0", # semantic versioning
    description="Reward Point System for Dunder Mifflin",
    author="Cesar Rocha",
    packages=find_packages(),   
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "dundie=dundie.__main__:main"
        ]
    }   
)