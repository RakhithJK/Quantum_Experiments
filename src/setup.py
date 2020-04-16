import setuptools

setuptools.setup(
    name                            = "orquestra",
    packages                        = setuptools.find_packages(where = "python"),
    url="https://github.com/bt3gl/Quantum-Experiments ",
    package_dir                     = {
        "" : "python"
    },
    classifiers                     = (
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ),
    install_requires = [
       "urllib3",
       "requests",
   ],
)