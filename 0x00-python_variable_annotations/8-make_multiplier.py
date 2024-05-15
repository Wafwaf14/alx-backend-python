#!/usr/bin/env python3
"""
Complex typessss - functions
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returnsss a function thast multiplies a float my multiplier"""
    def retfunc(x: float) -> float:
        """multiplis a float by multiplier"""
        return multiplier * x
    return retfunc