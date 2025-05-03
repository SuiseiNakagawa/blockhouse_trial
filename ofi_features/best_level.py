from .utils import ask_of, bid_of

def single_level_ofi(filtered_order_book, m=1):
    """
    Calculate Best-Level Order Flow Imbalance (OFI) for the events in the filtered order book.
    
    Arguments:
    order_book -- dict or DataFrame containing 'bid' and 'ask' levels
    m -- level of the order book to consider (default is 1, which is the best level)
    
    Returns:
    float -- Best-Level OFI
    """
    ofi = 0
    for n in range(0, len(filtered_order_book)):
        ofi += bid_of(filtered_order_book, n=n, m=m) - ask_of(filtered_order_book, n=n, m=m)
    return ofi
