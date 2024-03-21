with open('vacancy.csv', encoding='utf-8') as line:
    arr = list(map(lambda x: x.strip().split(';'), line.readlines()))
    sort = sorted(arr, key=lambda x: x[2])
    # сортируем
    for s in arr:
        if s[3] == 'классный руководитель':
            print(f"В компании {s[4]} есть заданная профессия: {s[3]}, з/п в такой компании составит: {s[0]}")
            # находим подходящие
            
