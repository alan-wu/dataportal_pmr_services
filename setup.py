from setuptools import setup
from setuptools import find_packages

version = '0.0.1'

classifiers = """
Development Status :: 3 - Alpha
Intended Audience :: Developers
Operating System :: OS Independent
Programming Language :: JavaScript
Programming Language :: Python :: 3
Programming Language :: Python :: 3.5
Programming Language :: Python :: 3.6
""".strip().splitlines()

setup(
    name='dataportal_pmr_services',
    version=version,
    description='Services of PMR',
    long_description=open('README.md').read(),
    classifiers=classifiers,
    keywords='',
    author='Auckland Bioengineering Institute',
    url='https://github.com/alan-wu/dataportal_pmr_services',
    packages=find_packages('src', exclude=['ez_setup']),
    package_dir={'': 'src'},
    namespace_packages=['dataportal_map'],
    zip_safe=False,
    install_requires=[
        'setuptools>=12',
        'requests',
        'pmr2.client @ https://api.github.com/repos/alan-wu/pmr2.client/tarball/scaffold',
        'pmr2.wfctrl @ https://api.github.com/repos/PMR2/pmr2.wfctrl/tarball/master',
    ],

    include_package_data=True,
    python_requires='>=3.5',
    # test_suite="",
)
