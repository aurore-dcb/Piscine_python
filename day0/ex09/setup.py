from setuptools import setup, find_packages

setup(
    name="ft_package",
    version="0.0.1",
    author="aducobu",
    author_email="aducobu@student.42.fr",
    description="My first package creation",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/aurore-dcb/Piscine_python/tree/main/day0/ex09",
    project_urls={
        "Bug Tracker": "https://github.com/aurore-dcb/Piscine_python/tree/main/day0/ex09",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.8",
    license="MIT",
)