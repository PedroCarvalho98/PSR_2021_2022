#!/usr/bin/python

def addComplex(x, y):
    return (x[0] + y[0], x[1] + y[1])
    # a = x[0]
    # b = x[1]
    # c = y[0]
    # d = y[1]
    # pass

def multiplyComplex(x, y):
    aux = (x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0])
    return aux
    # pass
    # a = x[0]
    # b = x[1]
    # c = y[0]
    # d = y[1]
    # result_real = a*c - b*d
    # result_im = a*d + b*c

def printComplex(x):
    print(str(x[0]) + ' + ' + str(x[1]) + 'i')
    # r = x[0]
    # i = x[1]
    # pass

def main():
    # ex2 a)

    # define two complex numbers as tuples of size two
    c1 = (5, 3)
    c2 = (-2, 7)

    # Test add
    c3 = addComplex(c1, c2)
    printComplex(c3)

    # test multiply
    printComplex(multiplyComplex(c1, c2))

if __name__ == '__main__':
    main()