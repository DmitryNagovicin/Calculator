# модуль для расчетов операций
import cmath

def Calc_block(data):
    x_value, oper, y_value = data
    if oper == '+':
        return sum(x_value, y_value)
    if oper == '-':
        return sub(x_value, y_value)
    if oper == '*':
        return mult(x_value, y_value)
    if (oper =='/') and (y_value != 0):
        return div(x_value, y_value)
    else:
        return 'Ошибка деления на 0!'

def sum(left_value, right_value):
    return left_value + right_value

def sub(left_value, right_value):
    return left_value - right_value

def mult(left_value, right_value):
    return left_value * right_value

def div(left_value, right_value):
    return left_value / right_value
