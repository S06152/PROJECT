from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirement(file_path:str)->List[str]:
    '''
    this function will return the list of requirement
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readline()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

setup(
    name = 'MACHINE_LEARNING',
    version = '0.0.1',
    author = 'Sanjeev Kumar',
    author_email = 'sanjeev.ece.imps@gmail.com',
    packages = find_packages(),
    install_requires = get_requirement('requirement.txt')
)