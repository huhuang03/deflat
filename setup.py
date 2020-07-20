from setuptools import setup

setup(
    name = 'deflat',
    version = '1.0.0',
    description = 'deflat the llvm flatten',
    entry_points = {
        'console_scripts': [
            'deflat=deflat:main'
        ]
    },
    install_requires = [
        'barf',
        'angr'
    ]
)