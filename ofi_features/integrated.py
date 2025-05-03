import numpy as np
from .multi_level import multi_level_ofi

def integrated_ofi(filtered_order_book, w):
    """
    Calculate the multi-level OFI vector from a filtered order book snapshot 
    and projects it onto the first principal component vector `w`, obtained via PCA on historical data.
    The result is normalized using the L1 norm of `w` so that the weights sum to 1.

    Arguments:
    filtered_order_book -- dict or DataFrame containing 'bid' and 'ask' levels
    w -- first principal component vector based on PCA on historical data represented as a numpy array

    Returns:
    float -- Integrated OFI
    """
    ofi = np.dot(multi_level_ofi(filtered_order_book), w) / np.sum(np.abs(w))

    return ofi
