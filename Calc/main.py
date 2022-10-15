from ui import get_data, out_result
from mathematics import make_calc
exit_calc = False
while not exit_calc:
    data = get_data()
    if data[0] == '0':
        exit_calc = True
    else:
        result = make_calc(data)
        out_result(result)
