from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT='-e .'

def get_requirements(file_path:str) -> List[str]:
    '''
    get the list of all the libraries in requirements
    '''
    requirements = []
    

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n',"") for req in requirements]
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)


    return requirements 



setup(
name='mlproject1',
version='0.0.1',
author='PrachiPatel',
author_email='prachi.patel.business@gmail.com',
packages=find_packages(),
install_requires= get_requirements('requirements.txt')
)