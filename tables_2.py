import pandas as pd
import time
start_time = time.time()

# принтить пустые
def f_1(list):
    i = 0

    for elem in list:
        if elem != (i+0):
            if elem != (i+1):
                print(elem)


f1_name = 'sgjp_pages_1-1500000.tsv'
f2_name = 'sgjp_pages_368311-1500000.tsv'
f3_name = 'sgjp_pages_653723-1500000.tsv'
f4_name = 'sgjp_pages_850806-1500000.tsv'
f5_name = 'sgjp_pages_1046852-1500000.tsv'
f6_name = 'sgjp_pages_1205921-1500000.tsv'
f7_name = 'sgjp_pages_125586-1500000.tsv'
f8_name = 'sgjp_pages_1390496-1500000.tsv'

df_1 = pd.read_csv(f1_name, sep='\t', usecols=['id', 'word_form'], low_memory=False)
df_2 = pd.read_csv(f2_name, sep='\t', usecols=['id', 'word_form'], low_memory=False)
df_3 = pd.read_csv(f3_name, sep='\t', usecols=['id', 'word_form'], low_memory=False)
df_4 = pd.read_csv(f4_name, sep='\t', usecols=['id', 'word_form'], low_memory=False)
df_5 = pd.read_csv(f5_name, sep='\t', usecols=['id', 'word_form'], low_memory=False)
df_6 = pd.read_csv(f6_name, sep='\t', usecols=['id', 'word_form'], low_memory=False)
df_7 = pd.read_csv(f7_name, sep='\t', usecols=['id', 'word_form'], low_memory=False)
df_8 = pd.read_csv(f8_name, sep='\t', usecols=['id', 'word_form'], low_memory=False)

df_m = pd.concat([df_1, df_2, df_3, df_4, df_5, df_6, df_7, df_8], ignore_index=True)

f_name_wf = 'wordforms_polish.tsv'

df_m = df_m.rename(columns={'word_form': 'wordform'})

df_mm = df_m.loc[df_m['wordform'] != 'NA']
#df_m.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)

df_m.to_csv(f_name_wf, columns=['wordform'], sep='\t', encoding='utf-8', index=False)







print("--- %s seconds ---" % (time.time() - start_time))
