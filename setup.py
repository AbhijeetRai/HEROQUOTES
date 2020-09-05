import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="heroquotes", # Replace with your own username
    version="1.0",
    author="Abhijeet Rai",
    author_email="abraj306@gmail.com",
    description="A package for superhero quotes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AbhijeetRai/superheroquotes",
    keywords = ['Super hero quotes', 'Superhero quotes', 'Marvel', 'DC', 'dc', 'Dc'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
