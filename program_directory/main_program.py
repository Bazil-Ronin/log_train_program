import re



# user_file = re.sub(r'^[^A-Z]*', '', (input('Укажите путь и имя файла .txt : ').replace('\\', '/')))


def railway_log(name_file_log):
    with open(name_file_log, 'r', encoding='u8') as file:
        counter = 0 # счетчик денег
        counter_point = 0 # счетчик заказов
        for row in file.readlines():
            if row[:3] == ' — ':
                print(row.rstrip()) # показание даты и времени
            total = (re.search(r'получил : \d{1,4}', row))
            if total != None:
                counter_point += 1
                print((int(total.group().split(' ')[-1])),'\n' ) # показание суммы за заказ
                counter += (int(total.group().split(' ')[-1])) # преобразуем в инт и суммируем. Итог за все логи

    print(f"Заказов выполнено: {counter_point} штук")
    print(f"\nИтого по данным логов, сумма составила: {counter}")
    print()
    # input('\n\n\nДля закрытия программы нажмите Enter')
    start()

def start():
    try:
        railway_log(re.sub(r'^[^A-Z]*', '', (input('Укажите путь и имя файла .txt : ').replace('\\', '/'))))
    except FileNotFoundError:
        print('Файла с таким путем или именем не существует. Попробуйте еще раз.')
        start()

start()

