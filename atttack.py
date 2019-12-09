m = [[1, 1, 1, 1, 1, 0.5, 1, 0, 0.5, 1, 1, 1, 1, 1, 1, 1, 1, 1], [2, 1, 0.5, 0.5, 1, 2, 0.5, 0, 2, 1, 1, 1, 1, 0.5, 2, 1, 2, 0.5], [1, 2, 1, 1, 1, 0.5, 2, 1, 0.5, 1, 1, 2, 0.5, 1, 1, 1, 1, 1], [1, 1, 1, 0.5, 0.5, 0.5, 1, 0.5, 0, 1, 1, 2, 1, 1, 1, 1, 1, 2], [1, 1, 0, 2, 1, 2, 0.5, 1, 2, 2, 1, 0.5, 2, 1, 1, 1, 1, 1], [1, 0.5, 2, 1, 0.5, 1, 2, 1, 0.5, 2, 1, 1, 1, 1, 2, 1, 1, 1], [1, 0.5, 0.5, 0.5, 1, 1, 1, 0.5, 0.5, 0.5, 1, 2, 1, 2, 1, 1, 2, 0.5], [0, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 0.5, 1], [1, 1, 1, 1, 1, 2, 1, 1, 0.5, 0.5, 0.5, 1, 0.5, 1, 2, 1, 1, 2], [1, 1, 1, 1, 1, 0.5, 2, 1, 2, 0.5, 0.5, 2, 1, 1, 2, 0.5, 1, 1], [1, 1, 1, 1, 2, 2, 1, 1, 1, 2, 0.5, 0.5, 1, 1, 1, 0.5, 1, 1], [1, 1, 0.5, 0.5, 2, 2, 0.5, 1, 0.5, 0.5, 2, 0.5, 1, 1, 1, 0.5, 1, 1], [1, 1, 2, 1, 0, 1, 1, 1, 1, 1, 2, 0.5, 0.5, 1, 1, 0.5, 1, 1], [1, 2, 1, 2, 1, 1, 1, 1, 0.5, 1, 1, 1, 1, 0.5, 1, 1, 0, 1], [1, 1, 2, 1, 2, 1, 1, 1, 0.5, 0.5, 0.5, 2, 1, 1, 0.5, 2, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 0.5, 1, 1, 1, 1, 1, 1, 2, 1, 0], [1, 0.5, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 0.5, 0.5], [1, 2, 1, 0.5, 1, 1, 1, 1, 0.5, 0.5, 1, 1, 1, 1, 1, 2, 2, 1]]
titles = ['一般',
    '格斗',
    '飞行',
    '毒',
    '地面',
    '岩石',
    '虫',
    '幽灵',
    '钢',
    '火',
    '水',
    '草',
    '电',
    '超能力',
    '冰',
    '龙',
    '恶',
    '妖精'
]


def attack(attrs):
    base = None
    for attr in attrs:
        index = titles.index(attr)
        if not base:
            base = m[index]
        else:
            temp = []
            for v1, v2 in zip(base, m[index]):
                temp.append(max(v1, v2))
            base = temp
    return base


def defend(attrs):
    base = None
    for attr in attrs:
        index = titles.index(attr)
        temp = []
        for l in m:
            temp.append(l[index])
        if not base:
            base = temp
        else:
            base = [v1 * v2 for v1, v2 in zip(base, temp)]
    return base


def b_print(result):
    # for title, v in zip(titles, result):
    #     print(title, v)
    max = 10
    s_titles = ''
    for title in titles:
        s_titles += title.rjust(max)
    print(s_titles)

    s_v = ''
    for i in result:
        i = str(i)
        s_v += i.rjust(max+1)
    print(s_v)

    print('*' * 200)

    big = []
    small = []

    for i, v in enumerate(result):
        if v > 1:
            big.append(titles[i])
        if v < 1:
            small.append(titles[i])

    print(f'打击面: {len(big)}个 {",".join(big)}')
    print(f'打不动: {len(small)}个 {",".join(small)}')


def b_print2(result):
    # for title, v in zip(titles, result):
    #     print(title, v)
    max = 10
    s_titles = ''
    for title in titles:
        s_titles += title.rjust(max)
    print(s_titles)

    s_v = ''
    for i in result:
        i = str(i)
        s_v += i.rjust(max+1)
    print(s_v)

    print('*' * 200)

    big = []
    small = []

    for i, v in enumerate(result):
        if v > 1:
            big.append(titles[i])
        if v < 1:
            small.append(titles[i])

    print(f'弱点: {len(big)}个 {",".join(big)}')
    print(f'抗性: {len(small)}个 {",".join(small)}')

attrs = ('地面', '冰', '格斗', '火')
b_print(attack(attrs))
print('\n\n')
b_print2(defend(attrs))
