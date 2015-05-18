"""
Tests for `objectifiedetree`.
"""
import pytest
from objectifiedetree import *


def test_dot_notation():
    tree = ET.fromstring('<root><a><b/></a></root>')

    assert tree.a is not None
    assert tree.a.b is not None
