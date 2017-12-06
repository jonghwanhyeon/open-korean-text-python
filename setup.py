import os
import subprocess

from setuptools import setup, find_packages
from setuptools.command.install import install

class InstallCommand(install):
    def run(self):
        original_working_directory = os.getcwd()
        path_prefix = os.path.dirname(os.path.realpath(__file__))

        os.chdir(os.path.join(path_prefix, 'openkoreantext', 'jar'))
        for group_id, artifact_id in [
                ('org.openkoreantext', 'open-korean-text'),
                ('org.scala-lang', 'scala-library'),
                ('com.twitter', 'twitter-text')
            ]:
            print('downloading {group_id}.{artifact_id}.jar'.format(group_id=group_id, artifact_id=artifact_id))
            subprocess.call([ 'python3', 'download-jar.py', group_id, artifact_id ])
        os.chdir(original_working_directory)

        super().run()

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
    install_requires=[ 'Jpype1' ],
    package_data={
        'openkoreantext': [ 'jar/*.jar' ]
    },
    cmdclass={
        'install': InstallCommand,
    }
)
