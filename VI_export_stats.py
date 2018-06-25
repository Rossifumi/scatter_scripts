# -*- coding: utf-8 -*-

import pandas as pd

file_list = []  
fl = file( "filenames_list.txt", "r" )  
  
for line in fl.readlines():  
    file_list.append(line.rstrip())

count = 0
df_list =[]
df = pd.DataFrame()

for f in file_list:
    count += 1
    df = pd.read_table(f,sep="\t",dtype='object')
    df = df[['Chromosome','Position','Gene','HGVSC','HGVSP','ClinVar','Variant Read Frequency','Total Read Depth']]
    df.columns = ['Chromosome','Position','Gene','HGVSC','HGVSP','ClinVar',"".join(["Freq_S",str(count)]),"".join(["Depth_S",str(count)])]
    df_list.append(df)

result = pd.merge(df_list[0], df_list[1], how='outer', on=['Chromosome','Position','Gene','HGVSC','HGVSP','ClinVar'])
for i in range(2,count):
    result = pd.merge(result, df_list[i], how='outer', on=['Chromosome','Position','Gene','HGVSC','HGVSP','ClinVar'])

result.to_csv('VI_export_stats.csv',index=False,sep=',')
