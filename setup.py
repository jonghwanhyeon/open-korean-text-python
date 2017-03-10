from setuptools import setup, find_packages

setup(
    name='open-korean-text-python',
    version='0.1.1',
    description='Python interface to Open Korean Text Processor',
    url='https://github.com/hyeon0145/open-korean-text-python',
    author='Jonghwan Hyeon',
    author_email='hyeon0145@gmail.com',
    license='Apache 2.0',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3 :: Only'
    ],
    keywords='open-korean-text open-korean-text-processor',
    packages=find_packages(),
    package_data={ '': ['jar/*.jar'] },
    install_requires=['Jpype1'],
)
