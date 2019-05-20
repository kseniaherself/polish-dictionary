# вот тут должна быть прога
import pandas as pd
import time
start_time = time.time()

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



print("--- %s seconds ---" % (time.time() - start_time))
