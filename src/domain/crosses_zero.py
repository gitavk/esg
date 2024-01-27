import numpy as np


def crosses_zero_cnt(signal: list[int]) -> int:
    signs = np.sign(signal)
    zeor_cross_posions = np.diff(signs)
    return len([x for x in zeor_cross_posions if x])
