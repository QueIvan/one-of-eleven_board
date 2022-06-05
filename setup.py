from setuptools import setup, find_packages

setup(
    name='one_of_eleven_board',
    version='0.1.0',
    packages=find_packages(include=['one_of_eleven_board', 'one_of_eleven_board.*']),
    install_requires=[
        'numpy',
        'adafruit-python-shell',
        'adafruit-blinka',
    ],
    entry_points={
        'console_scripts': ['test_board=one_of_eleven_board.main:main']
    }
)