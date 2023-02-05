import console_ui as c_ui
from fractions import Fraction
import cmath
from c_calc import Calc_block as c_calc
import data_transformation as d_t


def data_formatting(data):
    data_type, x_value, oper, y_value = data

    if data_type == '1':

        x_value = complex(x_value)

        y_value = complex(y_value)

    elif data_type == '2':

        a = x_value
        x_value = Fraction(int(a[0: a.index(
            '/')]), int(a[a.index('/')+1:len(a)]))

        g = y_value
        y_value = Fraction(int(g[0: g.index(
            '/')]), int(g[g.index('/')+1:len(g)]))

    return (x_value, oper, y_value)