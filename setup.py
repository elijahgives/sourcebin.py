import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sourcebin",
    version="1.0.1",
    author="author",
    author_email="hi@elijah.rip",
    description="Sourcebin API wrapper for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/elijahgives/sourcebin.py",
    packages=["sourcebin"],
    install_requires=["aiohttp"],
    license="LICENSE",
    classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
         "Operating System :: OS Independent",
     ],
)