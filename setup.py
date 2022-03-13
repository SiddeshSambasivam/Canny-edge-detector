import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="CannyEdgeDetector",
    version="0.0.1",
    author="Siddesh Sambasivam Suseela",
    author_email="siddesh002@ntu.edu.sg",
    description="An implementation of canny edge detection algorithm with sub-pixel accuracy for EE4208.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SiddeshSambasivam/Canny-edge-detector",
    project_urls={
        "Bug Tracker": "https://github.com/SiddeshSambasivam/Canny-edge-detector/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "attrs==21.4.0",
        "iniconfig==1.1.1",
        "numpy ",
        "opencv-python==4.5.5",
        "packaging==21.3",
        "pluggy==1.0.0",
        "py==1.11.0",
        "pyparsing==3.0.7",
        "pytest==7.0.1",
        "tomli==2.0.1"
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)