import urllib.request
import re
import time
start_time = time.time()

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

# основная функция которая делает таблицу и записывает её в файл
def M_create_table():
    t_s = '\t'      # tab separator
    n_l = '\n'      # new line

    f_name = 'sgjp_pages_1390496-1500000.tsv'    # ОБНОВИТЬ ИМЯ
    my_table = 'url' + t_s + 'id' + t_s + 'word_form' + t_s + 'p_pp_codes'
    F_write_file_w(my_table, f_name)
    error_file = open('errors_1390496.txt','w')  # ОБНОВИТЬ ИМЯ
    F_write_file_w('errors', 'error_1390496.txt')    # ОБНОВИТЬ ИМЯ 

    for i in range(1390496, 1500000):   # ПОДСТАВИТЬ НУЖНОЕ
        print(i)
        my_url = 'http://sgjp.pl/edycja/ajax/inflection-tables/?lexeme_id=%i&variant=1' %i

        try:
            with urllib.request.urlopen(my_url) as url:
                url_text = url.read().decode('utf-8')

            print('url: ', my_url)
            # print(url_text)
            if url_text == '{"result": "access denied"}':
                print('access denied')
                my_table_acd =  n_l + my_url + t_s + str(i) + t_s + 'NA' + t_s + 'NA'
                #print(my_table)
                F_write_file_a(my_table_acd, f_name)

            else:
                url_text_str = F_clean_str(str(url_text))

                regex_1 = '<spanclass=formp\d*?>(\w*?)<span>'
                res_1 = re.findall(regex_1, url_text_str)
               #print('итог_1: ', res_1)

                regex_p = '<spanclass=formp(\d*?)>'
                res_p = re.findall(regex_p, url_text_str)
                for p in res_p:
                    p = p

                for elem in res_1:
                    wordform = elem #str(elem)
                    #print(wordform)

                    my_table_p =n_l + my_url + t_s + str(i) + t_s + wordform + t_s + p
                    F_write_file_a(my_table_p, f_name)


# на случай двух p p
                regex_2 = '<spanclass=formp\d*?p\d*?>(\w*?)<span>'
                res_2 = re.findall(regex_2, url_text_str)
                # print('итог_2: ', re_2)

                if res_2:

                    regex_pp = '<spanclass=formp(\d*?)p(\d*?)>'
                    res_pp = re.findall(regex_pp, url_text_str)
                    #print(res_pp)

                    for pp in res_pp:
                        pp_tr = pp[0] + ', ' + pp[1]
                        #print('pp_tr: ', pp_tr)

                    for element in res_2:
                        wordform = element  # str(elem)
                        #print(wordform)

                        my_table_pp = n_l + my_url + t_s + str(i) + t_s + wordform + t_s + pp_tr
                        F_write_file_a(my_table_pp, f_name)


        except:
            
            error_file.write(str(i)+'\n')
            F_write_file_a(('\n'+str(i)+'\t'+my_url), 'error_1390496.txt') # ОБНОВИТЬ ИМЯ
            time.sleep(10)
            print(i, 'ErRoR')

    error_file.close()


M_create_table()

print('--- %s seconds ---' % (time.time() - start_time))
