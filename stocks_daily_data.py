from nsetools import Nse
import pandas as pd
import time
nse = Nse()
all_stock_codes = nse.get_stock_codes()
df_final = pd.DataFrame()
i = 0
with open("daily_data/0_log.txt", "w") as log:
    for key in all_stock_codes:
        try:
            stock_code = key
            q = nse.get_quote(key)
            df = pd.DataFrame([q])
        
            if i%50 == 0:
                print(f'Finished getting data for: {i} stocks, last stock code:{stock_code}')
            i += 1
            df.to_csv('daily_data/'+stock_code+'.csv',mode='a', index = False, header=None)
            
        except Exception as e:
            log.write(f'{time.strftime("%Y%m%d-%H%M%S")} ERROR: Failed downloading {stock_code}, Reason: {str(e)}')
            continue
#df_final.to_csv('daily_data/Stocks_daily_data.xlsx')