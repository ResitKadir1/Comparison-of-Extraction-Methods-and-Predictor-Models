import pandas as pd
import os
import glob
lst = r"C:\Users\resit\Downloads\Comparison-of-Extraction-Methods-and-Predictor-Models\datasets\cpu_GREEN"
#'/Users/reka/Desktop/Pro_IND/LGI'

lstd = os.listdir(lst)

"""
input           output
M056_T06.txt --> M056_T6.txt

Check the file name ,
if the name doesnt match rename it.
"""

for i in lstd:
  if i.endswith(".txt"):
    full_path = f"{lst}/{i}"
    name = i.split('.')[0] 
    ext = i.split('.')[1]
    folder = name.split("_")[0]
    file = name.split("_")[1]
    txt =".txt"
    if file =="T01":
      file ="T1"
      new = folder+"_"+file+txt
      os.rename(full_path,lst+'/'+new)
      print(i,new)