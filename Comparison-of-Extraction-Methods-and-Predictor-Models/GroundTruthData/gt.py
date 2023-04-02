import os


path ="/home/data_shares/faces_reka_stgr/Physiology"
subpath ="/M001"
ssubpath ="/T1"



lst = os.listdir(path)
lst2 = os.listdir(path+subpath)
lst3 = os.listdir(path+subpath+ssubpath)
for i in lst:
 for j in lst2:
  for q in lst3:
   print(i+"/"+j+"/"+q)
  # new_name =path+"/"+i+"_"+j+".txt"
  # old_name =path+"/"+i+"/"+j+"/"+q
  # if True:
  #  os.rename(old_name,new_name)
  #  print(old_name)


