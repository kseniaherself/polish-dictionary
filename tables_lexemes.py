import urllib.request
import re
import time
start_time = time.time()

# принтить пустые
def F_1(list):
    i = 0

    for elem in list:
        if elem != (i+0):
            if elem != (i+1):
                print(elem)

# запись в файл
def F_write_file_w(data, f_name):
    f = open(f_name, 'w')
    f.write(data)
    #print(data)
    f.close()

# дозапись в файл
def F_write_file_a(data, f_name):
    f = open(f_name, 'a')
    f.write(data)
    #print(data)
    f.close()

# чистка строки html
def F_clean_str(url_text):
    url_text_str = str(url_text)
    url_text_str = url_text_str[2:][:-1]
    # print(url_text_str)

    url_text_str = url_text_str.replace('"', '')
    url_text_str = url_text_str.replace(r'\n', '')
    url_text_str = url_text_str.replace('\\', '')
    url_text_str = url_text_str.replace('/', '')
    url_text_str = url_text_str.replace(' ', '')
    # url_text_str = re.sub('(  )*', '', url_text_str)
    # print(url_text_str)
    return url_text_str


# начальные формы
def M_3():
    f_name = 'lexemes_polish_55474.tsv'    # ОБНОВИТЬ ИМЯ

    my_table = 'url' + '\t' + 'id' + '\t' + 'lexeme'
    F_write_file_w(my_table, f_name)

    for i in range(55474, 1500000):  # ПОДСТАВИТЬ НУЖНОЕ
        print(i)
        my_url = 'http://sgjp.pl/edycja/ajax/inflection-tables/?lexeme_id=%i&variant=1' % i

        try:
            with urllib.request.urlopen(my_url) as url:
                url_text = url.read().decode('utf-8')
                #print(url_text)

            print('url: ', my_url)
            # print(url_text)

            if url_text == '{"result": "access denied"}':
                print('access denied')
                my_table_acd = '\n' + my_url + '\t' + str(i) + '\t' + 'NA'
                # print(my_table)
                F_write_file_a(my_table_acd, f_name)

            else:
                url_text_str = F_clean_str(str(url_text))
                #print(url_text_str)

                regex_1 = '<h1>(\w*?)<'
                res_1 = re.search(regex_1, url_text_str)

                #if res_1.group(1):
                #    print(res_1.group(1))

                my_table_w = '\n' + my_url + '\t' + str(i) + '\t' + res_1.group(1)
                F_write_file_a(my_table_w, f_name)

        except:
            time.sleep(10)
            print(i, 'ErRoR')




M_3()




print("--- %s seconds ---" % (time.time() - start_time))
