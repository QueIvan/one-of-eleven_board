from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name='one_of_eleven_board',
    version='0.1.0',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(include=['one_of_eleven_board', 'one_of_eleven_board.*']),
    author='Jan Szewczyk',
    author_email='szewczykjan2@gmail.com',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    python_requires=">=3.7, <4",
    install_requires=[
        'numpy',
        'adafruit-python-shell',
        'adafruit-blinka',
        'unittest',
    ],
    entry_points={
        'console_scripts': ['run_board=one_of_eleven_board.main:main']
    }
)