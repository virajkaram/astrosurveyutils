import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="surveyutils",
    version="0.0.1",
    author="Viraj Karambelkar",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/virajkaram/surveyutils",
    keywords="astronomy surveys coverage",
    packages=setuptools.find_packages(),
    package_data={
        'surveyutils': ['data/*']
    },
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires='>=3.7',
    install_requires=[
        "astropy",
        "numpy",
        "pandas",
        "jupyter",
        "matplotlib",
        "mocpy==0.12.0",
        "pandas"
    ]
)