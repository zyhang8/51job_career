def cut(str):
    information = {}
    f = open(str, 'r', encoding='UTF-8')
    for line in f.read().splitlines(False):
        a, b = line.split(':', 1)
        information [a] = b
    f.close()
    return information


if __name__ == '__main__':
    print(cut('header'))
