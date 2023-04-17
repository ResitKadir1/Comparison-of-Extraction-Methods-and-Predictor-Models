

import pandas as pd
import os
import glob
import pandasql as ps
from pathlib import Path


LGI =r"C:\Users\resit\Downloads\Comparison-of-Extraction-Methods-and-Predictor-Models\datasets\cpu_LGI"
PCA =r"C:\Users\resit\Downloads\Comparison-of-Extraction-Methods-and-Predictor-Models\datasets\PCA3"
GREEN =r"C:\Users\resit\Downloads\Comparison-of-Extraction-Methods-and-Predictor-Models\datasets\cpu_GREEN"
CHROM =r"C:\Users\resit\Downloads\Comparison-of-Extraction-Methods-and-Predictor-Models\datasets\cpu_CHROM"
GT =r"C:\Users\resit\Downloads\Comparison-of-Extraction-Methods-and-Predictor-Models\datasets\GroundTruthData"
GT_AVG =r"C:\Users\resit\Downloads\Comparison-of-Extraction-Methods-and-Predictor-Models\datasets\GT_AVG"
target = r"C:\Users\resit\Downloads\Comparison-of-Extraction-Methods-and-Predictor-Models"

LGI_l = os.listdir(LGI)     ; LGI_name   =   [] ; LGI_fileN   = []
PCA_l = os.listdir(PCA)     ; PCA_name   =   [] ; PCA_fileN   = []
GREEN_l = os.listdir(GREEN) ; GREEN_name =   [] ; GREEN_fileN = []
CHROM_l = os.listdir(CHROM) ; CHROM_name =   [] ; CHROM_fileN = []
GT_l = os.listdir(GT)       ; GT_name    =   [] ; GT_fileN    = []
GTA_l = os.listdir(GT_AVG)       ; GTA_name    =   [] ; GTA_fileN    = []



for i in LGI_l:
    if i.endswith(".txt"):
        full_path = f"{LGI}/{i}"
        name = i.split(".")[0]
        LGI_name.append(name)
        ext  = i.split(".")[1]
        df = pd.read_csv(full_path, encoding='utf8', engine='python')
        LGI_fileN.append(len(df))

for i in GREEN_l:
    if i.endswith(".txt"):
        full_path = f"{GREEN}/{i}"
        name = i.split(".")[0]
        GREEN_name.append(name)
        ext  = i.split(".")[1]
        df = pd.read_csv(full_path, encoding='utf8', engine='python')
        GREEN_fileN.append(len(df))


for i in CHROM_l:
    if i.endswith(".txt"):
        full_path = f"{CHROM}/{i}"
        name = i.split(".")[0]
        CHROM_name.append(name)
        ext  = i.split(".")[1]
        df = pd.read_csv(full_path, encoding='utf8', engine='python')
        CHROM_fileN.append(len(df))


for i in PCA_l:
    if i.endswith(".txt"):
        full_path = f"{PCA}/{i}"
        name = i.split(".")[0]
        PCA_name.append(name)
        ext  = i.split(".")[1]
        df = pd.read_csv(full_path)#, encoding='utf8', engine='python')
        PCA_fileN.append(len(df))
        #data = pd.DataFrame({'name':PCA_name,'Avarage':PCA_fileN})
        #print(data)


for i in GT_l:
    if i.endswith(".txt"):
        full_path = f"{GT}/{i}"
        name = i.split(".")[0]
        GT_name.append(name)
        ext  = i.split(".")[1]
        df = pd.read_csv(full_path, encoding='utf8', engine='python')
        sum1000 = len(df)//1000
        GT_fileN.append(sum1000)
        #data = pd.DataFrame({'name':GT_name,'Avarage':GT_fileN})
        #print(data)

for i in GTA_l:
    if i.endswith(".txt"):
        full_path = f"{GT_AVG}/{i}"
        name = i.split(".")[0]
        GTA_name.append(name)
        ext  = i.split(".")[1]
        df = pd.read_csv(full_path)#, encoding='utf8', engine='python')
        GTA_fileN.append(len(df))

    
df = pd.DataFrame(list(zip(GT_name,LGI_fileN,GREEN_fileN,CHROM_fileN,PCA_fileN,GT_fileN,GTA_fileN))
                  ,columns=["File Names",'LGI','GREEN','CHROM',"PCA","GT","GTA"]).set_index("File Names",drop=False)

print(df)
df.to_csv(target+"/"+'DataPointSchema.csv')

