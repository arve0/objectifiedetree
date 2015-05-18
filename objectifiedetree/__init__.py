__author__ = 'Arve Seljebu'
__email__ = 'arve.seljebu@gmail.com'
from os.path import join, dirname
__version__ = open(join(dirname(__file__), 'VERSION')).read().strip()
__all__ = ['ET', 'ElementTree', 'Element']


from .etree import ElementTree as ET


def __getattr__(self, key):
    return self.find('./' + key)

class ElementTree(ET.ElementTree):
    __getattr__ = __getattr__

class Element(ET.Element):
    __getattr__ = __getattr__
