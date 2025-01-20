# When is setup.py Used?

# When you’re developing a package that needs to be shared or published.
# It’s essential for making your project easy to install and distribute using pip or other tools.

from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
name='mlproject',
version='0.0.1',
author='Prajwal Alewoor',
author_email='prajwalalewoor12@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)