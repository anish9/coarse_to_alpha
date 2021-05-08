import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="alphax", # Replace with your own username
    version="2.0",
    author="Josh Anish",
    author_email="josh.anish1@gmail.com",
    description="alpha rough estimator",
    long_description="alpha rough estimator",
    long_description_content_type="text/markdown",
    url="https://github.com/anish9/coarse_to_alpha",
    project_urls={
        "Bug Tracker": "https://github.com/anish9/coarse_to_alpha/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",include_package_data=True
)