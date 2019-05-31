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
    all_indexes = []

    f_n_or = 'wordforms_polish_bez_pustot.tsv'
    f_read = open(f_n_or, 'r', encoding = 'utf-8')
    f_inp = f_read.readlines()
    f_read.close()

    print('прочитано (1)') 
    
    f_inp_2 = f_inp[750768:]  # РАБОЧАЯ ВЕРСИЯ ДЛЯ нужных СЛОВ

    f_inp_3 = [] # здусь будут все строки со всеми элементами
    for line in f_inp_2:
        line = line.split('\t')
        f_inp_3.append(line)

    print('переведено в строки (2)') 

    f_name = 'lexemes_55473_4.tsv'    # ОБНОВИТЬ ИМЯ

    my_table = 'url' + '\t' + 'id' + '\t' + 'lexeme'
    F_write_file_w(my_table, f_name)

    wrong_lines = []
    errori = []
    error_file = open('errors_55473.txt','w')  # ОБНОВИТЬ ИМЯ
    
    for line in f_inp_3:
        i = int(line[1])

        if i not in all_indexes:
            my_url = 'http://sgjp.pl/edycja/ajax/inflection-tables/?lexeme_id=%i&variant=1' % i
            
            try:
                with urllib.request.urlopen(my_url) as url:
                    url_text = url.read().decode('Windows-1250') #('utf-8')
                    #print(url_text)

                print('url: ', my_url)
                # print(url_text)

                if url_text == '{"result": "access denied"}':
                    print('access denied')
                    my_table_acd = '\n' + my_url + '\t' + str(i) + '\t' + 'NA'
                    # print(my_table)
                    F_write_file_a(my_table_acd, f_name)

                    print('А-А-А-А-А-А-А-ОШИБКА')
                    wrong_lines.append(i)
                    all_indexes.append(i)

                else:
                    url_text_str = F_clean_str(str(url_text))
                    #print(url_text_str)

                    regex_1 = '<h1>(\w*?)<'
                    res_1 = re.search(regex_1, url_text_str)

                    #if res_1.group(1):
                    #    print(res_1.group(1))

                    my_table_w = '\n' + my_url + '\t' + str(i) + '\t' + res_1.group(1)
                    F_write_file_a(my_table_w, f_name)

                    all_indexes.append(i)

            except:
                time.sleep(10)
                print(i, 'ErRoR')
                error_file.write(str(i)+'\n')

                errori.append(i)
                all_indexes.append(i)

    error_file.close()
    
    # наверно нужно прописать что потом закрыть
    print(wrong_lines)
    print(errori)


M_3()


print("--- %s seconds ---" % (time.time() - start_time))
