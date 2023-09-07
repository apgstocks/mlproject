from setuptools import find_packages,setup
from typing import List
hyfen_e_dot='-e .'
def get_requirements(file_name:str)->List[str]:
    '''
    this function return the list of requirement
    '''
    requirements=[]
    with open(file_name) as obj:
        requirements=obj.readlines()
        requirements=[r.replace('\n','') for r in requirements]

        if hyfen_e_dot in requirements:
            requirements.remove(hyfen_e_dot)
        
        return requirements

setup(
name='mlproject',
version='0.0.1',
author='apsara',
author_email='apgzip@gmail.com',
packages=find_packages(),
#install_requires=['pandas','numpy','seaborn']
install_requires=get_requirements('requirement.txt')
)