#!/usr/bin/env python3
"""
Complex types - stringv and int/float to tuple
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """takesq a string k and an int ottt float v as
    argumentsss and returns a tuple"""
    return (k, v * v)