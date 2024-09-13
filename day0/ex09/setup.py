from setuptools import setup

setup(
    name="ft_package",
    version="0.0.1",
    author="aducobu",
    author_email="aducobu@student.42.fr",
    description="My first package creation",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/aurore-dcb/Piscine_python/",
    project_urls={
        "Bug Tracker": "https://github.com/aurore-dcb/Piscine_python/",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    python_requires=">=3.8",
    license="MIT",
)
