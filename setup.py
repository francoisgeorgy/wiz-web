from setuptools import setup

setup(
    name='wiz',
    version='1.0.0',
    py_modules=['wiz'],  # Name of your Python file without .py
    install_requires=[],  # Add dependencies here if needed
    entry_points={
        'console_scripts': [
            'wiz=wiz:main',
        ],
    },
)
