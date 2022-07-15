from tmplAPI import VERSION

import setuptools

setuptools.setup(
    name='tmplAPI',
    version=VERSION,
    description="A simple REST API that implements a a request header's modification template",
    url="https://github.com/calvinfarias/REST-tmplAPI",
    packages=setuptools.find_packages(),
    install_requires=[
        'fastapi',
        'uvicorn',
        'pytest',
        'requests'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Linux",
    ]
)

