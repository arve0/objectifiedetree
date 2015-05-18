# objectifiedetree

[![build-status-image]][travis]
[![pypi-version]][pypi]
[![wheel]][pypi]

## Overview

Wouldn't it be nice to use dot notation for ElementTrees? This package allows for:

```python
tree = ET.fromstring('<root><a><b c="asdf" /></a></root>')
a = tree.a
b = a.b
b.attrib['c'] == "asdf" # True
```

`tree.a` will be a [`Element`-object](https://docs.python.org/3.4/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element) with the extra `__getattr__` method. This means that you can use the element as you would do normally, but names in your XML that crases with python's methods or attributes must be accessed through `tree.find(xpath)`.

This package uses the python implementation of etree, which makes it slower than the C-implementation found in CPython. An alternative would be to mmonkey-patch the built-in with [forbiddenfruit](https://github.com/clarete/forbiddenfruit), but I haven't looked into this.

`objectifiedetree` has copied the python implementation of etree from [CPython 3.4 Lib/xml/etree](https://github.com/python/cpython/tree/master/Lib/xml/etree) and will probably only work with Python 3.4.

## Installation

Install using `pip`...

```bash
pip install objectifiedetree
```

## Example

```python
from objectifiedetree import *

tree = ET.parse('/path/to/file.xml')
# dot notation :-)
el = tree.xpath.to.your.element

# use normal etree attributes
print(el.attrib)

# access name crashes
attrib_el = el.find('./attrib')
```

## Development
Install dependencies and link development version of objectifiedetree to pip:
```bash
git clone https://github.com/arve0/objectifiedetree
cd objectifiedetree
pip install -r requirements.txt # install dependencies and objectifiedetree-package
```

### Testing
```bash
tox
```

### Build documentation locally
To build the documentation:
```bash
pip install -r docs/requirements.txt
make docs
```



[build-status-image]: https://secure.travis-ci.org/arve0/objectifiedetree.png?branch=master
[travis]: http://travis-ci.org/arve0/objectifiedetree?branch=master
[pypi-version]: https://pypip.in/version/objectifiedetree/badge.svg
[pypi]: https://pypi.python.org/pypi/objectifiedetree
[wheel]: https://pypip.in/wheel/objectifiedetree/badge.svg
