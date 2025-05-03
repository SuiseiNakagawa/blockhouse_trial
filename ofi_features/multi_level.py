import numpy as np
from .best_level import single_level_ofi

def multi_level_ofi(filtered_order_book):
    """
    Calculate Order Flow Imbalance (OFI) for multiple levels of the order book, then normalizes based on average depth and number of events.
    Multi-level OFI is defined as a vector in Cont et al. (2023), where each component corresponds to a level of the order book.
    
    Arguments:
    filtered_order_book -- DataFrame containing 'bid' and 'ask' levels, already filtered by time
    
    Returns:
    numpy array -- Multi-Level OFI where each entry corresponds to a level
    """
    book_depths = np.zeros(10)
    for m in range(0, 10):
        bid_size_column = f'bid_sz_{m:02d}' 
        ask_size_column = f'ask_sz_{m:02d}'
        total_depth = np.sum(filtered_order_book[bid_size_column] + filtered_order_book[ask_size_column])
        book_depths[m-1] = total_depth / (2 * len(filtered_order_book))
    average_depth = np.mean(book_depths)

    ofis = np.array([single_level_ofi(filtered_order_book, m=m) / average_depth for m in range(1, 11)])

    return ofis
