#!/usr/bin/python

def add(x, y):
    real_x = x['r']
    imag_x = x['i']
    real_y = y['r']
    imag_y = y['i']
    real_part = real_y + real_x
    imag_part = imag_x + imag_y

    return {'r': real_part, 'i': imag_part}

def multiply(x,y):
    pass
def printComplex(x):
    pass

def main():
    complex_num_dict = {}
    complex_num_dict['c1'] = {'r': 5, 'i': 3}
    print(complex_num_dict)
    complex_num_dict['c2'] = {'i': 7, 'r': -2}
    print(complex_num_dict)
    print(complex_num_dict['c1'])
    print(complex_num_dict['c2'])
    complex_num_dict['c3'] = add(complex_num_dict['c1'], complex_num_dict['c2'])
    print(complex_num_dict['c3'])

    complex_num_dict['add'] = add
    complex_num_dict['c3'] = complex_num_dict['add'](complex_num_dict['c1'], complex_num_dict['c2'])
    print(complex_num_dict['c3'])

    complex_num_dict['add'] = lambda x, y: {'r': x['r'] + y['r'], 'i': x['i'] + y['i']}
    complex_num_dict['c3'] = complex_num_dict['add'](complex_num_dict['c1'], complex_num_dict['c2'])
    print(complex_num_dict)
if __name__ == '__main__':
    main()