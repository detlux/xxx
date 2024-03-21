with open('vacancy.csv', encoding='utf-8') as line, open('vacancy_new.csv', 'w', encoding='utf-8') as lene:
    arr = list(map(lambda x: x.strip().split(';'), line.readlines()))[1:]
    arr.sort(key=lambda p: p[0], reverse=True)
    lene.write('company,role,Salary' + '\n')
    for j in arr:
        lene.write(f"{j[4]},{j[3]},{j[0]}" + '\n')
    for i in range(3):
        print(arr[i][4], arr[i][3], arr[i][0], sep=' - ')