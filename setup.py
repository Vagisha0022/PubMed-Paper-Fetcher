from setuptools import setup, find_packages

setup(
    name="pubmed-utils",  # Name of your package
    version="0.1.0",  # Initial version of the package
    packages=find_packages(),  # Automatically discover and include all packages in the project
    install_requires=[  # List any external dependencies here
        "requests",  # This is your main dependency for making HTTP requests
    ],
    entry_points={  # Define the command-line entry point for the executable script
        'console_scripts': [
            'get-papers-list = main:main',  # This assumes you have a 'main' function in your 'main.py' file
        ],
    },
    classifiers=[  # Classifiers are used to categorize the package on PyPI
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Minimum required Python version
)
