import pandas as pd
import numpy as np
df=pd.read_excel(r'/users/yoezeljai/desktop/python programs/openpyxl_data/test.xlsx')
#df.head()
#pd.pivot_table(df,index=['Manager'])
pd.pivot_table(df,index=["MANAGER","LOGIN"],values=["RESOLVES"],aggfunc=np.sum)
df.to_excel(r'/users/yoezeljai/desktop/python programs/openpyxl_data/test_pivot.xlsx')
