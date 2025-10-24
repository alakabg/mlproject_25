from setuptools import setup, find_packages

#Function to read the requirements.txt file and return a list of dependencies

HYPEN_E_DOT = '-e .'
def get_requirements(filename):
    with open(filename, 'r') as file:
        requirements = file.readlines()
    r = [req.strip() for req in requirements]
    
    if HYPEN_E_DOT in r:
        r.remove(HYPEN_E_DOT)
        
    return r

setup(
    name='ml_project_setup',
    version='0.0.1',
    author= "Alaka",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)