#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    s = list(map(float, input("Список: ").split()))
    if not s:
        print("Заданный список пуст", file=sys.stderr)
        exit(1)

    m_max = s[0]
    s_first = s_second = s[0]
    i_first = i_second = 0
    k_first = k_second = 0
    for i, item in enumerate(s):
        if m_max < item:
            m_max = item
        if (0 < item) and (k_first == 1) and (k_second == 0):
            k_second = 1
            i_second, s_second = i, item
        if (0 < item) and (k_first == 0):
            k_first = 1
            i_first, s_first = i, item

    summ = 0
    for item in s[i_first + 1:i_second]:
        summ += item

    s.sort(key=lambda x: x == 0)

    print("Упорядоченный список(элементы = 0, после всех остальных): ", s)
    print("Максимальный по модулю элемент списка = ", m_max)
    if (k_first == 0) or (k_second == 0):
        print("В списке нет двух положительных элементов.")
    else:
        print("Сумма элементов списка, рассположенных между первым и вторым положительными элементами = ", summ)
