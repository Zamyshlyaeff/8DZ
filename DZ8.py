
def interface():
    mode=input('Введите режим работы: импорт или экспорт? ')
    mode1=mode.lower()
    if mode1=='импорт':
        data_directory=''
        FIO=input('Введите ФИО: ')
        data_directory+=FIO
        year=input('Введите год рождения: ')
        data_directory+=year
        phone_number=input('Введите номер телефона: ')
        data_directory+=phone_number
        data_import(data_directory)
    elif mode1=='экспорт':
        data_directory=input('Введите фамилию для поиска: ')
        export(data_directory)

def data_import(data_directory):
    with open('directory.txt','a',encoding='utf8') as file:
        file.write('\n'+ data_directory)

def export(data_directory):
    with open('directory.txt','r',encoding='utf8') as file:
        list1=file.read().split('\n')
        for i in range(len(list1)):
            if data_directory in list1[i]:
                export_file=(list1[i])
                print(export_file)

interface()
