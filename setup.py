from setuptools import setup,find_packages
from typing import List


Hypen_e_dot="-e ."
def get_requirements(file_path:str)->List:
    requirements=[]

    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if Hypen_e_dot in requirements:
            requirements.remove(Hypen_e_dot)

    return requirements


setup(

    name="Kidney Tumor Classifier",
    version="0.0.1",
    description="A project this is used to classify the tumor in kidney",
    author="Avinash",
    author_email="polisettyavinash2@gmail.com",
    packages=find_packages(),
    install_requirs=get_requirements('requirements.txt')

)