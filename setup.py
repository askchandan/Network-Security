'''
This setup.py file is essential part of packaging and distributing Python Projects.
It is used by setuptools (or disutils in older Python versions) to define the 
configuration of the project, such as its metadata, dependencies and more.
'''

from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    '''
    This function reads a requirements file and returns a list of them.
    '''
    requirements=[]
    try:
        with open(file_path) as file_obj:
            requirements=file_obj.readlines()
            requirements=[req.replace("\n", "") for req in requirements]

            if HYPHEN_E_DOT in requirements:
                requirements.remove(HYPHEN_E_DOT)

    except FileNotFoundError as e:
        print(f"File Not Found {file_path}: {e}")

    return requirements



setup(
    name="Network Security Project",
    version="0.0.1",
    author="Chandan Malakar",
    author_email="chandanmalakar7549@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)