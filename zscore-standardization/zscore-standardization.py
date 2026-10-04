import numpy as np

def zscore_standardize(X: list, axis: int = 0, eps: float = 1e-12) -> np.ndarray:
    x = np.asarray(X, dtype = float)
    x_bar = np.mean(x, axis = axis, keepdims = True)
    std = np.std(x, axis = axis, keepdims = True)
    safe_std = np.where(std > eps, std, 1.0)
    return (x-x_bar) / safe_std