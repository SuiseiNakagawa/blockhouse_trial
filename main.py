import pandas as pd
import numpy as np
from ofi_features.utils import filter_by_time
from ofi_features.best_level import single_level_ofi
from ofi_features.multi_level import multi_level_ofi
from ofi_features.cross_asset import cross_asset_ofi

# Load the order book data
data_path = 'data/first_25000_rows.csv'
order_book = pd.read_csv(data_path)

# Convert the 'ts_event' column to datetime
order_book['ts_event'] = pd.to_datetime(order_book['ts_event'])

# Filter the order book by time
# Update the time frame as desired
# Setting the start and endtimes to be equal results in filtering by a sigle timestamp
start_time = pd.to_datetime('2024-10-21T11:54:29.221064336Z')
end_time = pd.to_datetime('2024-10-21T11:54:41.235907431Z')
filtered_order_book = filter_by_time(order_book, start_time, end_time)

# Calculate Best-Level OFI
best_level_result = single_level_ofi(filtered_order_book)
print("Best-Level OFI:", best_level_result)

# Calculate Multi-Level OFI
multi_level_result = multi_level_ofi(filtered_order_book)
print("Multi-Level OFI:", multi_level_result)

# Calculate Integrated OFI
# Estimating first principal component w based on Figure 2(a) in Cont et al. (2023)
w1_estimated = np.array([0.05, 0.09, 0.11, 0.12, 0.12, 0.12, 0.11, 0.10, 0.09, 0.09])
integrated_result = np.dot(multi_level_result, w1_estimated)
print("Integrated OFI:", integrated_result)

# Calculate Cross-Asset OFI for a target symbol
target_symbol = 'AAPL'  # Replace with the desired symbol
cross_asset_result = cross_asset_ofi(filtered_order_book, target_symbol)
print("Cross-Asset OFI:", cross_asset_result)

# Save the results to a CSV file# Save the results to a CSV file
pd.DataFrame({'Best_Level_OFI': [best_level_result]}).to_csv('outputs/best_level_ofi.csv', index=False)
pd.DataFrame({'Multi_Level_OFI': multi_level_result}).to_csv('outputs/multi_level_ofi.csv', index=False)
pd.DataFrame({'Integrated_OFI': [integrated_result]}).to_csv('outputs/integrated_ofi.csv', index=False)
pd.DataFrame({'Cross_Asset_OFI': cross_asset_result}).to_csv('outputs/cross_asset_ofi.csv', index=False)
print("Results saved to the outputs folder.")