import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyboost-vehicles",
    version="0.0.1",
    author="Christian Lück",
    author_email="clueck@wwu.de",
    description="Classes flattening the learning curve for python starters playing with lego boost",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lueck/pyboost-vehicles",
    project_urls={
        "Bug Tracker": "https://github.com/lueck/pyboost-vehicles/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.5",
    install_requires = [
        "wheel",
        "setuptools",
        "pylgbst==1.2.0"
        ],
    # entry_points = {
    #     'console_scripts' : [
    #         'fahrzeug=pyboost.cli:main',
    #         ],
    #     },
)
