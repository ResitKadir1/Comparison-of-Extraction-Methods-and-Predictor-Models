
import os
import pandas as pd
import glob
import numpy as np
import csv

source =r"C:\Users\resit\Downloads\Comparison-of-Extraction-Methods-and-Predictor-Models\datasets\sil"
target =r"C:\Users\resit\Downloads\Comparison-of-Extraction-Methods-and-Predictor-Models\datasets\GT_AVG"


'''
Each Freame has ~40 data point
Each second has 25 Frames
Each second has ~ 1000 data point while Our methods has only one data point for each second
'''

lst1 = os.listdir(source)
for i in lst1:
 if i.endswith('.txt'):
  full_path =f'{source}/{i}'
  df = pd.read_csv(full_path, encoding='utf8', engine='python')
  name = i.split('.')[0] 
  ext = i.split('.')[1]
  seconds = 5000 #calc start approx after 5 second video start

 start = 0
 tlist = []
 for i in range(0, len(df.index)):
    if (i + 1)%1000 == 0:
        result = df.iloc[start:i+1].mean()
        result=round(result, 2)
        tlist.append(result)
        start = i + 1
        #result.to_csv(try_+"/"+name+'.txt', index=False)
        final_list_frame = pd.DataFrame(np.array(tlist))#.T)
        final_list_frame.to_csv(target+"/"+name+'.txt', index=False)
print(final_list_frame)