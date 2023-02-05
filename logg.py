from datetime import datetime as dt
from time import time


def result_logger(data, result):
    x_value, oper, y_value = data
    data_str = f'{str(x_value)} {oper} {str(y_value)}'
    time = dt.now().strftime('%H:%M')
    # print('{}; операция : {} результат : {}\n'.format(time, data_str, data))
    with open('log.csv', 'a', encoding='UTF-8') as file:
        file.write('{}; операция : {} результат :{}\n'.format(
            time, data_str, result))