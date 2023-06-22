#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    s = list(map(int, input("Список: ").split()))
    k = 0
    s1 = []

    for i in range(len(s)):
        if s[i] == 0:
            s1.append(i + 1)
            k += 1

    if k == 0:
        print("В списке нет нулевых элементов.")
    else:
        print("Нулевых элементов: {0}.".format(k))
        print("Список их индексов: ", s1)
