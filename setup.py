import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="extractfq",
    version="0.0.3",
    author='Guanliang Meng',
    author_email='mengguanliang@foxmail.com',
    description="Extract some fastq reads from the beginning of the files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires='>=3',
    url='https://github.com/linzhi2013/extractfq',
    packages=setuptools.find_packages(),
    include_package_data=True,
    # install_requires=[],

    entry_points={
        'console_scripts': [
            'extractfq=extractfq.extractfq:main',
        ],
    },
    classifiers=(
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
    ),
)