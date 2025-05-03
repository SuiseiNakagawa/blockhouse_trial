def bid_of(order_book, n, m):
    """
    Calculate Bid Order Flow (OF) at time n at level m (1-indexed to align with Cont et al. (2023)).
    Arguments:
    order_book -- dict or DataFrame containing 'bid' and 'ask' levels
    n -- number of levels to consider
    Returns:
    float -- Bid OF
    """
    n = n - 1
    m = m - 1
    bid_price_column = f'bid_px_{m:02d}' 
    bid_size_column = f'bid_sz_{m:02d}'

    if order_book.iloc[n][bid_price_column] > order_book.iloc[n-1][bid_price_column]:
        bid_of = order_book.iloc[n][bid_size_column] 
    elif order_book.iloc[n][bid_price_column] < order_book.iloc[n-1][bid_price_column]:
        bid_of = -order_book.iloc[n][bid_size_column]
    else:
        bid_of = order_book.iloc[n][bid_size_column] - order_book.iloc[n-1][bid_size_column]

    return bid_of


def ask_of(order_book, n, m):
    """
    Calculate Ask Order Flow (OF) at time n at level m (1-indexed to align with Cont et al. (2023)).
    Arguments:
    order_book -- dict or DataFrame containing 'bid' and 'ask' levels
    n -- number of levels to consider
    Returns:
    float -- Ask OF
    """
    n = n - 1
    m = m - 1
    ask_price_column = f'ask_px_{m:02d}' 
    ask_size_column = f'ask_sz_{m:02d}'

    if order_book.iloc[n][ask_price_column] > order_book.iloc[n-1][ask_price_column]:
        ask_of = -order_book.iloc[n][ask_size_column] 
    elif order_book.iloc[n][ask_price_column] < order_book.iloc[n-1][ask_price_column]:
        ask_of = order_book.iloc[n][ask_size_column]
    else:
        ask_of = order_book.iloc[n][ask_size_column] - order_book.iloc[n-1][ask_size_column]

    return ask_of

def filter_by_time(order_book, start_time, end_time):
    """
    Filter the order book to only include events in the interval [start_time, end_time].
    Arguments:
    order_book -- DataFrame containing 'ts_event' column
    start_time -- start time for the calculation as a datetime object
    end_time -- end time for the calculation as a datetime object
    Returns:
    DataFrame -- filtered order book
    """
    return order_book[(order_book['ts_event'] >= start_time) & (order_book['ts_event'] <= end_time)]