# polish-dictionary

.py and .r files — different versions of crawler for online Polish dictionary http://sgjp.pl/ 

### crawler_sgjp_to_table_v2.py 

The program generates files: 

+ sgjp_pages_N-1500000.tsv
  - n and m could vary, but the total interval is **1** and **1500000** respectively (0 page is empty) 
+ error(s) 
  - errors_368311.txt 
    — closes and writes in **only** after the whole cycle 
  - error_368311.txt 
    — writes in every error case immediately after detection 


length.py: outputs the last line 
