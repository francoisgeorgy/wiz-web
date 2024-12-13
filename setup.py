from setuptools import setup

setup(
    name='wiz',
    version='1.0.0',
    py_modules=['wiz'],
    install_requires=[],
    entry_points={
        'console_scripts': [
            'wiz=wiz:main',
        ],
    },
)
