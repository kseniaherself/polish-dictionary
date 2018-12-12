import urllib.request
import time
start_time = time.time()

# запись в файл
def F_write_in_file(data, f_name):
    f = open(f_name, 'w')
    f.write(data)
    #print(data)
    f.close()

# функция которая скачивает страницы
def M_f():
    error_file = open('errors.txt','w')

    for i in range(32684, 33000):
        my_url = 'http://sgjp.pl/edycja/ajax/inflection-tables/?lexeme_id=%i&variant=1' % i
        f_name = 'html_pages/sgjp_page_' + str(i) + '.html'

        try:
            with urllib.request.urlopen(my_url) as url:
                url_text = url.read().decode('utf-8')

            #print(url_text)
            F_write_in_file(url_text, f_name)

        except:
            error_file.write(str(i) + '\n')
            time.sleep(10)
            print(i, 'ErRoR')

    error_file.close()

M_f()

print('--- %s seconds ---' % (time.time() - start_time))
