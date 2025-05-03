import numpy as np
from .best_level import single_level_ofi

def cross_asset_ofi(filtered_order_book, target_symbol):
    """
    Calculate cross-asset OFI for the events in the filtered order book.
    This function extracts the contemporaneous best-level OFIs of all other stocks (excluding the target stock)
    at each timestamp.

    Arguments:
    filtered_order_book -- dict or DataFrame containing 'bid' and 'ask' levels
    target_symbol -- the symbol of the stock for which we want to calculate the cross-asset OFI
    (e.g., 'AAPL', 'MSFT', etc.)

    Returns:
    numpy array -- cross-asset OFI where each entry corresponds to a symbol/asset excluding the target stock
    """
    filtered_order_book_no_target = filtered_order_book[filtered_order_book['symbol'] != target_symbol]
    grouped = filtered_order_book_no_target.groupby('symbol')

    ofis = []

    for symbol, group in grouped:
        cross_asset_ofi = single_level_ofi(group)
        ofis.append(cross_asset_ofi)
    
    return np.array(ofis)
