for i in range(1,18):
    sufix = {
        1:'st',
        2:'nd',
        3:'rd'
    }.get(i,'th')
    print(f'This my {i}-{sufix} line of python')
