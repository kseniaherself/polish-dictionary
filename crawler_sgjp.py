import urllib.request
import re
import time
start_time = time.time()

# запись в файл
def F_write_in_file(data, f_name):
    f = open(f_name, 'w')
    f.write(data)
    #print(data)
    f.close()

# дозапись в файл
def F_write_file(data, f_name):
    f = open(f_name, 'a')
    f.write(data)
    #print(data)
    f.close()

# открытие и извлечение данных из файла
def F_extract_data(f_name):
    f = open(f_name, 'r')
    data = f.read()
    #print(data)
    f.close()
    return data

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
def M_create_table(n, m):
    t_s = '\t'      # tab separator
    n_l = '\n'      # new line
    p_list = []     # список с p-кодами
    pp_list = []    # список с pp-кодами

# это то как файл должен был начинаться, но я не хочу далее читать по строчкам, а просто склеиваю файлы
    my_table = '' #'url' + t_s + 'id' + t_s + 'word_form'
    error_file = open('errors.txt','w')
    for i in range(n, m):   # переменные которые генерируются в M_create_files
        my_url = 'http://sgjp.pl/edycja/ajax/inflection-tables/?lexeme_id=%i&variant=1' %i

        try:
            with urllib.request.urlopen(my_url) as url:
                url_text = url.read().decode('utf-8')

            #print(url_text)
            if url_text == '{"result": "access denied"}':
                #print('отказано')
                my_table = my_table + n_l + my_url + t_s + str(i) + t_s + 'NA' + t_s + 'NA'
                #print(my_table)

            else:
                url_text_str = F_clean_str(str(url_text))

                regex_1 = '<spanclass=formp\d*?>(\w*?)<span>'
                res_1 = re.findall(regex_1, url_text_str)
                #print('итог_1: ', res_1)

                regex_p = '<spanclass=formp(\d*?)>'
                res_p = re.findall(regex_p, url_text_str)
                for p in res_p:
                    if p not in p_list:
                        p_list.append(p)

                for elem in res_1:
                    wordform = elem #str(elem)
                    #print(wordform)

                    my_table = my_table + n_l + my_url + t_s + str(i) + t_s + wordform + t_s + p

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

                        if pp_tr not in pp_list:
                            pp_list.append(pp_tr)

                    for element in res_2:
                        wordform = element  # str(elem)
                        # print(wordform)

                        my_table = my_table + n_l + my_url + t_s + str(i) + t_s + wordform + t_s + pp_tr

                #print(i) — i это номер страницы
            #print(my_table)
            f_name = 'sgjp_pages_' + str(n) + '-' + str(m) + '.tsv'
            F_write_in_file(my_table, f_name)

        except:
            error_file.write(str(i)+'\n')
            time.sleep(10)
            print(i, 'ErRoR')

    error_file.close()
    #print('создан файл: ', f_name)
    return f_name, p_list, pp_list

# функция которая обходит страницы и записывает для них файлы с номерами
def M_create_files():
    f_names = []
    p_list_M = []
    pp_list_M = []

    # здесь нужно выставлять ограничения на диапазон и шаг страниц
    for j in range(0, 200, 10): # end = 2 000 000 # поправить ограничения
        #print(j)
        k = j + 10 # поправить ограничения
        # print('j: ', j, 'k: ', k)
        f_name, p_list, pp_list = M_create_table(j, k)
        f_names.append(f_name)

        for element in p_list:
            if element not in p_list_M:
                p_list_M.append(element)

        for elem in pp_list:
            if elem not in pp_list_M:
                pp_list_M.append(elem)

    #print(p_list_M)
    p_M = 'p_codes'
    for e in p_list_M:
        p_M = p_M + '\n' + str(e)
    F_write_in_file(p_M, 'p_codes.txt') # ПОСТАВИТЬ МЕТКУ: p_codes_1

    #print(pp_list_M)
    pp_M = 'pp_codes'
    for el in pp_list_M:
        pp_M = pp_M + '\n' + str(el)
    F_write_in_file(pp_M, 'pp_codes.txt')

    #print(f_names)
    return f_names #, p_list_M, pp_list_M

# функция объединяет файлы
def M_merging_files():
    f_names = M_create_files()

    #print('создание одного файла')

    f_name = 'dictionary_sgjp.tsv'
    F_write_in_file(('url' + '\t' + 'id' + '\t' + 'word_form' + '\t' + 'p_or_pp_code'), f_name)

    for name in f_names:
        data = F_extract_data(name)
        F_write_file(data, f_name)


M_merging_files()

print("--- %s seconds ---" % (time.time() - start_time))
