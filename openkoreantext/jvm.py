import os
import atexit

from glob import glob
from jpype import *

@atexit.register
def clean_up():
    shutdownJVM()

class_paths = [
    'jar/scala-library-2.12.1.jar',
    'jar/twitter-text-1.14.3.jar',
    'jar/open-korean-text-1.1.jar',
]

path_prefix = os.path.dirname(os.path.realpath(__file__))
class_paths = glob(os.path.join(path_prefix, 'jar', '*.jar'))

parameters = [
    '-Djava.class.path={}'.format(
        os.pathsep.join(class_paths)
    ),
    '-ea',
]

startJVM(getDefaultJVMPath(), *parameters)