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
    version='1.0.0',
    description='Python interface to Open Korean Text Processor',
    url='https://github.com/jonghwanhyeon/open-korean-text-python',
    author='Jonghwan Hyeon',
    author_email='hyeon0145@gmail.com',
    license='Apache 2.0',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: Korean',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Scientific/Engineering :: Information Analysis',
    ],
    keywords='open-korean-text open-korean-text-processor',
    packages=find_packages(),
    install_requires=[ 'Jpype1' ],
    python_requires='>=3',
    package_data={
        'openkoreantext': [ 'jar/*.jar' ]
    },
    cmdclass={
        'install': InstallCommand,
    }
)
