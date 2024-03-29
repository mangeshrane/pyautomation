from setuptools import setup

setup(
    name='pyautomation',
    version='1.0',
    author='mrane',
    author_email='ranemangesh555@gmail.com',
    packages=['pyautomation',
              'pyautomation.api',
              'pyautomation.browsers',
              'pyautomation.configuration',
              'pyautomation.data_providers',
              'pyautomation.file_manager',
              'pyautomation.web',
              ],
    scripts=[],
    #Entry point to found by pytest
    entry_points={'pytest11': ['pytest-pyautomation=pyautomation.plugin',],
                  'console_scripts': ['pyautomation=pyautomation.project_setup:main'],},
    url='',
    license='',
    description='',
    long_description=open('README.md').read(),
    install_requires=[
        "allure-pytest==2.6.2",
        "allure-python-commons==2.6.2",
        "apipkg==1.5",
        "atomicwrites==1.3.0",
        "attrs==19.1.0",
        "certifi==2019.3.9",
        "chardet==3.0.4",
        "colorama==0.4.1",
        "execnet==1.6.0",
        "idna==2.8",
        "more-itertools==7.0.0",
        "pluggy==0.9.0",
        "py==1.8.0",
        "pytest==4.4.0",
        "pytest-forked==1.0.2",
        "pytest-xdist==1.28.0",
        "PyYAML==5.1",
        "requests==2.21.0",
        "selenium==3.141.0",
        "six==1.12.0",
        "urllib3==1.24.1",
        "xlrd==1.2.0",
        "pytest-html==1.20.0",
    ],
    classifiers=["Framework :: Pytest"],
)