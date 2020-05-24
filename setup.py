import setuptools

with open("README.md") as fp:
    long_description = fp.read()

setuptools.setup(
    name="boxcli",
    version="1.4.0",
    author="Anish Jewalikar",
    author_email="anishjewalikar@gmail.com",
    description="Create simple and beautiful boxes in the terminal.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NightShade256/boxcli",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=["grapheme", "colorama"],
)
