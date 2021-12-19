import math
import sys

coefs = {
    'A': 0,
    'B': 0,
    'C': 0
}

i = 0

try:
    coefs['A'] = int(sys.argv[1])
    coefs['B'] = int(sys.argv[2])
    coefs['C'] = int(sys.argv[3])
except:
    while i < 3:
        key = list(coefs.keys())[i]
        try:
            coefs[key] = float(input('Введите коэффициент %s: ' % key))
            i += 1
        except ValueError:
            print('Ошибка! Повторите ввод.')


def get_qr_roots(a, b, c):
    result = []
    D = b * b - 4 * a * c
    if D == 0.0:
        root = -b / (2.0 * a)
        result.append(root)
    elif D > 0.0:
        sqD = math.sqrt(D)
        root1 = (-b + sqD) / (2.0 * a)
        root2 = (-b - sqD) / (2.0 * a)
        result.append(root1)
        result.append(root2)
    return result


def get_bqr_roots(a=-1, b=-1):
    result = []
    if (a > 0):
        result.append(math.sqrt(a))
        result.append(math.sqrt(a) * -1)
    elif (a == 0):
        result.append(0)
    if (b > 0):
        result.append(math.sqrt(b))
        result.append(math.sqrt(b) * -1)
    elif (b == 0):
        result.append(0)
    return result


qr_roots = get_qr_roots(coefs['A'], coefs['B'], coefs['C'])

roots = []

if (len(qr_roots) == 2):
    print(get_bqr_roots(qr_roots[0], qr_roots[1]))
elif (len(qr_roots) == 1):
    print(get_bqr_roots(qr_roots[0]))
else:
    print('Корней нет')
