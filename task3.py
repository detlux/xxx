with open('vacancy.csv', encoding='utf-8') as line:
    arr = list(map(lambda x: x.strip().split(';'), line.readlines()))
    aff = {}
    cnt = 0
    while True:
        a = input()
        if a == 'None':
            break
        else:
            for j in arr:
                if j[4] == a:
                    cnt += 1
            if cnt > 0:
                for i in arr:
                    if i[4] == a:
                        print(f"В {i[4]} найдена вакансия: {i[3]}. З/п составит: {i[0]}")
            else:
                print("К сожалению ничего не удалось найти")
            cnt = 0