import setuptools
from api import VERSION

setuptools.setup(
    name='RESTAPI1stTMPL',
    version=VERSION,
    url="https://github.com/calvinfarias/RESTAPI1stTMPL",
    description="A simple REST API that implements a request header's modification",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: MIT License",
        "Operating System :: Linux",
    ],
)

