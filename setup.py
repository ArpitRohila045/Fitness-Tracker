from setuptools import find_packages, setup
from typing import List

def getRequirements(requirements : str) -> List[str]:
    """
    Docstring for getRequirements
    
    :param requirements: Description
    :type requirements: str
    :return: Description
    :rtype: List[str]
    """
    pass

setup(
    name="fitness-tracking",
    version='0.0.1',
    author="Arpit Rohila",
    author_email="arpitrohila07@gmail.com",
    packages=find_packages(),
    packages=getRequirements('requirements.txt')
)