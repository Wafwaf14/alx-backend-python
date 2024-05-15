#!/usr/bin/env python3
"""
Complex typess - mixedd list
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """returns sufm of mixed list as a float"""
    return sum(mxd_lst)