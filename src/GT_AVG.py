"""
Author : Resit Kadir

Get every 1000 column value avarage[:1001][1001:2001]

#Warning Return section

"""

import os
import pandas as pd
import glob
import numpy as np
import csv

def get_avg_of_GT(source,target,window_size=1000):
  '''
  Each Freame has ~40 data point
  Each second has 25 Frames
  Each second has ~ 1000 data point while Our methods has only one data point for each second
   '''
  
  #source = r"C:\Users\resit\Downloads\Comparison-of-Extraction-Methods-and-Predictor-Models\datasets\GroundTruthData"
  #target =r"C:\Users\resit\Downloads\Comparison-of-Extraction-Methods-and-Predictor-Models\datasets\GT_AVG"
  files_list = os.listdir(source)
  
  for i in files_list:
    if i.endswith('.txt'):
        full_path =f'{source}/{i}'
        df = pd.read_csv(full_path, encoding='utf8', engine='python')
        name = i.split('.')[0] 
        ext = i.split('.')[1]
        seconds = 5000 #calc start approx after 5 second video start

        start = 0
        tlist = []
    for i in range(0, len(df.index)):
        if (i + 1)%2000 == 0: ####ATTENTION HERE###
            result = df.iloc[start:i+1].mean()
            result=round(result, 2)
            tlist.append(result)
            
            start = i + 1
            final_list_frame = pd.DataFrame(np.array(tlist))#.T)
            final_list_frame.to_csv(target+"/"+name+'.txt', index=False)

  return  print(final_list_frame)

get_avg_of_GT(r"C:\Users\resit\Downloads\Comparison-of-Extraction-Methods-and-Predictor-Models\datasets\GroundTruthData"
              ,r"C:\Users\resit\Downloads\Comparison-of-Extraction-Methods-and-Predictor-Models\datasets\GT_AVG"
              ,1000)


