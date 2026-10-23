import setuptools

setuptools.setup(
    name="alpha_asymmetry_calculations",
    version="0.1.0",
    author="Justin Bowen",
    author_email="justinbowen@uchicago.edu",
    description="test package for PSYC 46050",
    url="https://github.com/justinbowen2004/PSYC46050_Week3.git",
    packages=setuptools.find_packages(),
    install_requires=[
        'mne',
        'numpy',
        'scipy',
        'matplotlib',
        'decorator',
        'jinja2',
        'lazy-loader',
        'packaging',
        'pooch',
        'tqdm',
    ],
)