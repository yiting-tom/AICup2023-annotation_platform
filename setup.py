import os
from setuptools import setup, find_packages

def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    line_iter = (line.strip() for line in open(filename))

    return [line for line in line_iter if line and not line.startswith("#")]

requirements = parse_requirements("requirements.txt")

setup(
    name="AI Cup Annotation Platform",
    version="alpha1.0",
    author="NCKU IKM Lab",
    license="Apache 2.0",
    url="github.com/yiting-tom/AICup2023-annotation_platform",
    packages=find_packages(),
    install_requires=requirements,
)

data_dir = "data"
if not os.path.exists(data_dir):
    os.mkdir(data_dir)
