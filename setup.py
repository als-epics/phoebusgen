import setuptools
import versioneer

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as fh:
    requirements = [line.strip() for line in fh]

setuptools.setup(
    name="phoebusgen",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    author="Tynan Ford",
    author_email="tford@lbl.gov",
    description="Control screen generator for Phoebus",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tynanford/phoebusgen",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        "Topic :: Software Development :: Code Generators"
    ],
    python_requires='>=3.5',
    install_requires=requirements,
)

