from setuptools import setup, find_packages

setup(
    name="snapshot",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "snapshot = snapshot.task1:main",
        ],
    },
    install_requires=[
        'psutil',
        'argparse'
    ],
    version="0.1",
    author="Alena Averchanka",
    author_email="Alena_Averchanka1@epam.com",
    description="App which monitoring the system/server.",
    license="MIT"
)
