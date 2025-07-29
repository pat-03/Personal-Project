lrt_line = input('What line of LRT will you ride?')

if str.lower(lrt_line) == 'lrt 1':
    type_of_ticket = input('Do you have a stored value BEEP in hand?')

    if str.lower(type_of_ticket) == 'no':
        origin = input('Origin:')
        destination = input('Destination:')
    
        if str.lower(origin) == 'baclaran' or str.lower(destination) == 'baclaran':
            if str.lower(destination) == 'edsa' or str.lower(origin) == 'edsa' or str.lower(destination) == 'libertad' or str.lower(origin) == 'libertad':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 15 pesos')
            elif str.lower(destination)  == 'gil puyat' or str.lower(origin) == 'gil puyat' or str.lower(destination) == 'vito cruz' or str.lower(origin) == 'vito cruz' or str.lower(destination) == 'quirino' or str.lower(origin) == 'quirino' or str.lower(destination) == 'pedro gil' or str.lower(origin) == 'pedro gil' or str.lower(destination) == 'un avenue' or str.lower(origin) == 'un avenue':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 20 pesos')
            elif str.lower(destination) == 'central' or str.lower(origin) == 'central' or str.lower(destination) == 'carriedo' or str.lower(origin) == 'carriedo' or str.lower(destination) == 'd. jose' or str.lower(origin) == 'd. jose' or str.lower(destination) == 'bambang' or str.lower(origin) == 'bambang' or str.lower(destination) == 'tayuman' or str.lower(origin) == 'tayuman':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 25 pesos')
            elif str.lower(destination) == 'blumentritt' or str.lower(origin) == 'blumentritt' or str.lower(destination) == 'abad santos' or str.lower(origin) == 'abad santos' or str.lower(destination) == 'r. papa' or str.lower(origin) == 'r. papa' or str.lower(destination) == '5th avenue' or str.lower(origin) == '5th avenue' or str.lower(destination) == 'monumento' or str.lower(origin) == 'monumento':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 30 pesos')
            elif str.lower(destination) == 'balintawak' or str.lower(origin) == 'balintawak' or str.lower(destination) == 'fpj' or str.lower(origin) == 'fpj':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 35 pesos')
            else:
                print('Invalid')
        elif str.lower(origin) == 'edsa' or str.lower(destination) == 'edsa':
            if str.lower(destination) == 'libertad' or str.lower(origin) == 'libertad' or str.lower(destination) == 'gil puyat' or str.lower(origin) == 'gil puyat':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 15 pesos')
            elif str.lower(destination) == 'vito cruz' or str.lower(origin) == 'vito cruz' or str.lower(destination) == 'quirino' or str.lower(origin) == 'quirino' or str.lower(destination) == 'pedro gil' or str.lower(origin) == 'pedro gil' or str.lower(destination) == 'un avenue' or str.lower(origin) == 'un avenue':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 20 pesos')
            elif str.lower(destination) == 'central' or str.lower(origin) == 'central' or str.lower(destination) == 'carriedo' or str.lower(origin) == 'carriedo' or str.lower(destination) == 'd. jose' or str.lower(origin) == 'd. jose' or str.lower(destination) == 'bambang' or str.lower(origin) == 'bambang' or str.lower(destination) == 'tayuman' or str.lower(origin) == 'tayuman' or str.lower(destination) == 'blumentritt' or str.lower(origin) == 'blumentritt':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 25 pesos')
            elif str.lower(destination) == 'abad santos' or str.lower(origin) == 'abad santos' or str.lower(destination) == 'r. papa' or str.lower(origin) == 'r. papa' or str.lower(destination) == '5th avenue' or str.lower(origin) == '5th avenue' or str.lower(destination) == 'monumento' or str.lower(origin) == 'monumento':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 30 pesos')
            elif str.lower(destination) == 'balintawak' or str.lower(origin) == 'balintawak' or str.lower(destination) == 'fpj' or str.lower(origin) == 'fpj':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 35 pesos')
            else:
                print('Invalid')
        elif str.lower(origin) == 'libertad' or str.lower(destination) == 'libertad':
            if str.lower(destination) == 'gil puyat' or str.lower(origin) == 'gil puyat' or str.lower(destination) == 'vito cruz' or str.lower(origin) == 'vito cruz':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 15 pesos')
            elif str.lower(destination) == 'quirino' or str.lower(origin) == 'quirino' or str.lower(destination) == 'pedro gil' or str.lower(origin) == 'pedro gil' or str.lower(destination) == 'un avenue' or str.lower(origin) == 'un avenue' or str.lower(destination) == 'central' or str.lower(origin) == 'central':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 20 pesos')
            elif str.lower(destination) == 'carriedo' or str.lower(origin) == 'carriedo' or str.lower(destination) == 'd. jose' or str.lower(origin) == 'd. jose' or str.lower(destination) == 'bambang' or str.lower(origin) == 'bambang' or str.lower(destination) == 'tayuman' or str.lower(origin) == 'tayuman' or str.lower(destination) == 'blumentritt' or str.lower(origin) == 'blumentritt' or str.lower(destination) == 'abad santos' or str.lower(origin) == 'abad santos':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 25 pesos')
            elif str.lower(destination) == 'r. papa' or str.lower(origin) == 'r. papa' or str.lower(destination) == '5th avenue' or str.lower(origin) == '5th avenue' or str.lower(destination) == 'monumento' or str.lower(origin) == 'monumento':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 30 pesos')
            elif str.lower(destination) == 'balintawak' or str.lower(origin) == 'balintawak' or str.lower(destination) == 'fpj' or str.lower(origin) == 'fpj':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 35 pesos')
            else:
                print('Invalid')
        elif str.lower(origin) == 'gil puyat' or str.lower(destination) == 'gil puyat':
            if str.lower(destination) == 'vito cruz' or str.lower(origin) == 'vito cruz':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 15 pesos')
            elif str.lower(destination) == 'quirino' or str.lower(origin) == 'quirino' or str.lower(destination) == 'pedro gil' or str.lower(origin) == 'pedro gil' or str.lower(destination) == 'un avenue' or str.lower(origin) == 'un avenue' or str.lower(destination) == 'central' or str.lower(origin) == 'central' or str.lower(destination) == 'carriedo' or str.lower(origin) == 'carriedo':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 20 pesos')
            elif str.lower(destination) == 'd. jose' or str.lower(origin) == 'd. jose' or str.lower(destination) == 'bambang' or str.lower(origin) == 'bambang' or str.lower(destination) == 'tayuman' or str.lower(origin) == 'tayuman' or str.lower(destination) == 'blumentritt' or str.lower(origin) == 'blumentritt' or str.lower(destination) == 'abad santos' or str.lower(origin) == 'abad santos' or str.lower(destination) == 'r. papa' or str.lower(origin) == 'r. papa':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 25 pesos')
            elif  str.lower(destination) == '5th avenue' or str.lower(origin) == '5th avenue' or str.lower(destination) == 'monumento' or str.lower(origin) == 'monumento' or str.lower(destination) == 'balintawak' or str.lower(origin) == 'balintawak':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 30 pesos')
            elif  str.lower(destination) == 'fpj' or str.lower(origin) == 'fpj':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 35 pesos')
            else:
                print('Invalid')
        elif str.lower(origin) == 'vito cruz' or str.lower(destination) == 'vito cruz':
            if str.lower(destination) == 'quirino' or str.lower(origin) == 'quirino' or str.lower(destination) == 'pedro gil' or str.lower(origin) == 'pedro gil':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 15 pesos')
            elif str.lower(destination) == 'un avenue' or str.lower(origin) == 'un avenue' or str.lower(destination) == 'central' or str.lower(origin) == 'central' or str.lower(destination) == 'carriedo' or str.lower(origin) == 'carriedo' or str.lower(destination) == 'd. jose' or str.lower(origin) == 'd. jose' or str.lower(destination) == 'bambang' or str.lower(origin) == 'bambang':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 20 pesos')
            elif str.lower(destination) == 'tayuman' or str.lower(origin) == 'tayuman' or str.lower(destination) == 'blumentritt' or str.lower(origin) == 'blumentritt' or str.lower(destination) == 'abad santos' or str.lower(origin) == 'abad santos' or str.lower(destination) == 'r. papa' or str.lower(origin) == 'r. papa' or str.lower(destination) == '5th avenue' or str.lower(origin) == '5th avenue':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 25 pesos')
            elif  str.lower(destination) == 'monumento' or str.lower(origin) == 'monumento' or str.lower(destination) == 'balintawak' or str.lower(origin) == 'balintawak':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 30 pesos')
            elif  str.lower(destination) == 'fpj' or str.lower(origin) == 'fpj':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 35 pesos')
            else:
                print('Invalid')
        elif str.lower(origin) == 'quirino' or str.lower(destination) == 'quirino':
            if str.lower(destination) == 'pedro gil' or str.lower(origin) == 'pedro gil' or str.lower(destination) == 'un avenue' or str.lower(origin) == 'un avenue':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 15 pesos')
            elif str.lower(destination) == 'central' or str.lower(origin) == 'central' or str.lower(destination) == 'carriedo' or str.lower(origin) == 'carriedo' or str.lower(destination) == 'd. jose' or str.lower(origin) == 'd. jose' or str.lower(destination) == 'bambang' or str.lower(origin) == 'bambang' or str.lower(destination) == 'tayuman' or str.lower(origin) == 'tayuman':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 20 pesos')
            elif str.lower(destination) == 'blumentritt' or str.lower(origin) == 'blumentritt' or str.lower(destination) == 'abad santos' or str.lower(origin) == 'abad santos' or str.lower(destination) == 'r. papa' or str.lower(origin) == 'r. papa' or str.lower(destination) == '5th avenue' or str.lower(origin) == '5th avenue' or str.lower(destination) == 'monumento' or str.lower(origin) == 'monumento':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 25 pesos')
            elif str.lower(destination) == 'balintawak' or str.lower(origin) == 'balintawak' or str.lower(destination) == 'fpj' or str.lower(origin) == 'fpj':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 30 pesos')
            else:
                print('Invalid')
        elif str.lower(origin) == 'pedro gil' or str.lower(destination) == 'pedro gil':
            if str.lower(destination) == 'un avenue' or str.lower(origin) == 'un avenue':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 15 pesos')
            elif str.lower(destination) == 'central' or str.lower(origin) == 'central' or str.lower(destination) == 'carriedo' or str.lower(origin) == 'carriedo' or str.lower(destination) == 'd. jose' or str.lower(origin) == 'd. jose' or str.lower(destination) == 'bambang' or str.lower(origin) == 'bambang' or str.lower(destination) == 'tayuman' or str.lower(origin) == 'tayuman' or str.lower(destination) == 'blumentritt' or str.lower(origin) == 'blumentritt':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 20 pesos')
            elif str.lower(destination) == 'abad santos' or str.lower(origin) == 'abad santos' or str.lower(destination) == 'r. papa' or str.lower(origin) == 'r. papa' or str.lower(destination) == '5th avenue' or str.lower(origin) == '5th avenue' or str.lower(destination) == 'monumento' or str.lower(origin) == 'monumento':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 25 pesos')
            elif str.lower(destination) == 'balintawak' or str.lower(origin) == 'balintawak' or str.lower(destination) == 'fpj' or str.lower(origin) == 'fpj':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 30 pesos')
            else:
                print('Invalid')
        elif str.lower(origin) == 'un avenue' or str.lower(destination) == 'un avenue':
            if str.lower(destination) == 'central' or str.lower(origin) == 'central':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 15 pesos')
            elif str.lower(destination) == 'carriedo' or str.lower(origin) == 'carriedo' or str.lower(destination) == 'd. jose' or str.lower(origin) == 'd. jose' or str.lower(destination) == 'bambang' or str.lower(origin) == 'bambang' or str.lower(destination) == 'tayuman' or str.lower(origin) == 'tayuman' or str.lower(destination) == 'blumentritt' or str.lower(origin) == 'blumentritt' or str.lower(destination) == 'abad santos' or str.lower(origin) == 'abad santos':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 20 pesos')
            elif str.lower(destination) == 'r. papa' or str.lower(origin) == 'r. papa' or str.lower(destination) == '5th avenue' or str.lower(origin) == '5th avenue' or str.lower(destination) == 'monumento' or str.lower(origin) == 'monumento':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 25 pesos')
            elif str.lower(destination) == 'balintawak' or str.lower(origin) == 'balintawak' or str.lower(destination) == 'fpj' or str.lower(origin) == 'fpj':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 30 pesos')
            else:
                print('Invalid')
        elif str.lower(origin) == 'central' or str.lower(destination) == 'central':
            if str.lower(destination) == 'carriedo' or str.lower(origin) == 'carriedo' or str.lower(destination) == 'd. jose' or str.lower(origin) == 'd. jose':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 15 pesos')
            elif str.lower(destination) == 'bambang' or str.lower(origin) == 'bambang' or str.lower(destination) == 'tayuman' or str.lower(origin) == 'tayuman' or str.lower(destination) == 'blumentritt' or str.lower(origin) == 'blumentritt' or str.lower(destination) == 'abad santos' or str.lower(origin) == 'abad santos' or str.lower(destination) == 'r. papa' or str.lower(origin) == 'r. papa' or str.lower(destination) == '5th avenue' or str.lower(origin) == '5th avenue':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 20 pesos')
            elif str.lower(destination) == 'monumento' or str.lower(origin) == 'monumento' or str.lower(destination) == 'balintawak' or str.lower(origin) == 'balintawak':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 25 pesos')
            elif str.lower(destination) == 'fpj' or str.lower(origin) == 'fpj':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 30 pesos')
            else:
                print('Invalid')
        elif str.lower(origin) == 'carriedo' or str.lower(destination) == 'carriedo':
            if str.lower(destination) == 'd. jose' or str.lower(origin) == 'd. jose' or str.lower(destination) == 'bambang' or str.lower(origin) == 'bambang':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 15 pesos')
            elif str.lower(destination) == 'tayuman' or str.lower(origin) == 'tayuman' or str.lower(destination) == 'blumentritt' or str.lower(origin) == 'blumentritt' or str.lower(destination) == 'abad santos' or str.lower(origin) == 'abad santos' or str.lower(destination) == 'r. papa' or str.lower(origin) == 'r. papa' or str.lower(destination) == '5th avenue' or str.lower(origin) == '5th avenue':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 20 pesos')
            elif str.lower(destination) == 'monumento' or str.lower(origin) == 'monumento' or str.lower(destination) == 'balintawak' or str.lower(origin) == 'balintawak':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 25 pesos')
            elif str.lower(destination) == 'fpj' or str.lower(origin) == 'fpj':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 30 pesos')
            else:
                print('Invalid')
        elif str.lower(origin) == 'd. jose' or str.lower(destination) == 'd. jose':
            if str.lower(destination) == 'bambang' or str.lower(origin) == 'bambang' or str.lower(destination) == 'tayuman' or str.lower(origin) == 'tayuman':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 15 pesos')
            elif str.lower(destination) == 'blumentritt' or str.lower(origin) == 'blumentritt' or str.lower(destination) == 'abad santos' or str.lower(origin) == 'abad santos' or str.lower(destination) == 'r. papa' or str.lower(origin) == 'r. papa' or str.lower(destination) == '5th avenue' or str.lower(origin) == '5th avenue' or str.lower(destination) == 'monumento' or str.lower(origin) == 'monumento':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 20 pesos')
            elif str.lower(destination) == 'balintawak' or str.lower(origin) == 'balintawak' or str.lower(destination) == 'fpj' or str.lower(origin) == 'fpj':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 25 pesos')
            else:
                print('Invalid')
        elif str.lower(origin) == 'bambang' or str.lower(destination) == 'bambang':
            if str.lower(destination) == 'tayuman' or str.lower(origin) == 'tayuman' or str.lower(destination) == 'blumentritt' or str.lower(origin) == 'blumentritt':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 15 pesos')
            elif str.lower(destination) == 'abad santos' or str.lower(origin) == 'abad santos' or str.lower(destination) == 'r. papa' or str.lower(origin) == 'r. papa' or str.lower(destination) == '5th avenue' or str.lower(origin) == '5th avenue' or str.lower(destination) == 'monumento' or str.lower(origin) == 'monumento':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 20 pesos')
            elif str.lower(destination) == 'balintawak' or str.lower(origin) == 'balintawak' or str.lower(destination) == 'fpj' or str.lower(origin) == 'fpj':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 25 pesos')
            else:
                print('Invalid')
        elif str.lower(origin) == 'tayuman' or str.lower(destination) == 'tayuman':
            if str.lower(destination) == 'blumentritt' or str.lower(origin) == 'blumentritt' or str.lower(destination) == 'abad santos' or str.lower(origin) == 'abad santos':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 15 pesos')
            elif str.lower(destination) == 'r. papa' or str.lower(origin) == 'r. papa' or str.lower(destination) == '5th avenue' or str.lower(origin) == '5th avenue' or str.lower(destination) == 'monumento' or str.lower(origin) == 'monumento':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 20 pesos')
            elif str.lower(destination) == 'balintawak' or str.lower(origin) == 'balintawak' or str.lower(destination) == 'fpj' or str.lower(origin) == 'fpj':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 25 pesos')
            else:
                print('Invalid')
        elif str.lower(origin) == 'blumentritt' or str.lower(destination) == 'blumentritt':
            if str.lower(destination) == 'abad santos' or str.lower(origin) == 'abad santos' or str.lower(destination) == 'r. papa' or str.lower(origin) == 'r. papa':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 15 pesos')
            elif str.lower(destination) == '5th avenue' or str.lower(origin) == '5th avenue' or str.lower(destination) == 'monumento' or str.lower(origin) == 'monumento' or str.lower(destination) == 'balintawak' or str.lower(origin) == 'balintawak':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 20 pesos')
            elif str.lower(destination) == 'fpj' or str.lower(origin) == 'fpj':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 25 pesos')
            else:
                print('Invalid')
        elif str.lower(origin) == 'abad santos' or str.lower(destination) == 'abad santos':
            if str.lower(destination) == 'r. papa' or str.lower(origin) == 'r. papa' or str.lower(destination) == '5th avenue' or str.lower(origin) == '5th avenue':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 15 pesos')
            elif str.lower(destination) == 'monumento' or str.lower(origin) == 'monumento' or str.lower(destination) == 'balintawak' or str.lower(origin) == 'balintawak':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 20 pesos')
            elif str.lower(destination) == 'fpj' or str.lower(origin) == 'fpj':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 25 pesos')
            else:
                print('Invalid')
        elif str.lower(origin) == 'r. papa' or str.lower(destination) == 'r. papa':
            if str.lower(destination) == '5th avenue' or str.lower(origin) == '5th avenue':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 15 pesos')
            elif str.lower(destination) == 'monumento' or str.lower(origin) == 'monumento' or str.lower(destination) == 'balintawak' or str.lower(origin) == 'balintawak':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 20 pesos')
            elif str.lower(destination) == 'fpj' or str.lower(origin) == 'fpj':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 25 pesos')
            else:
                print('Invalid')
        elif str.lower(origin) == '5th avenue' or str.lower(destination) == '5th avenue':
            if str.lower(destination) == 'monumento' or str.lower(origin) == 'monumento':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 15 pesos')
            elif str.lower(destination) == 'balintawak' or str.lower(origin) == 'balintawak' or str.lower(destination) == 'fpj' or str.lower(origin) == 'fpj':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 20 pesos')
            else:
                print('Invalid')
        elif str.lower(origin) == 'monumento' or str.lower(destination) == 'monumento':
            if str.lower(destination) == 'balintawak' or str.lower(origin) == 'balintawak' or str.lower(destination) == 'fpj' or str.lower(origin) == 'fpj':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 20 pesos')
            else:
                print('Invalid')
        elif str.lower(origin) == 'balintawak' or str.lower(destination) == 'balintawak':
            if str.lower(destination) == 'fpj' or str.lower(origin) == 'fpj':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 20 pesos')
            else:
                print('Invalid')
        else:
            print('Unavailable Route')


    elif str.lower(type_of_ticket) == 'yes':
        origin = input('Origin')
        destination = input('Destination')
    
        if str.lower(origin) == 'baclaran' or str.lower(destination) == 'baclaran':
            if str.lower(destination) == 'edsa' or str.lower(origin) == 'edsa':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 14 pesos')
            elif str.lower(destination)  == 'libertad' or str.lower(origin) == 'libertad':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 15 pesos')
            elif str.lower(destination)  == 'gil puyat' or str.lower(origin) == 'gil puyat':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 16 pesos')
            elif str.lower(destination)  == 'vito cruz' or str.lower(origin) == 'vito cruz':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 17 pesos')
            elif str.lower(destination)  == 'quirino' or str.lower(origin) == 'quirino':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 18 pesos')
            elif str.lower(destination)  == 'pedro gil' or str.lower(origin) == 'pedro gil':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 19 pesos')
            elif str.lower(destination)  == 'un avenue' or str.lower(origin) == 'un avenue':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 20 pesos')
            elif str.lower(destination)  == 'central' or str.lower(origin) == 'central':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 22 pesos')
            elif str.lower(destination)  == 'carriedo' or str.lower(origin) == 'carriedo' or str.lower(destination)  == 'd. jose' or str.lower(origin) == 'd. jose':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 23 pesos')
            elif str.lower(destination)  == 'bambang' or str.lower(origin) == 'bambang':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 24 pesos')
            elif str.lower(destination)  == 'tayuman' or str.lower(origin) == 'tayuman':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 25 pesos')
            elif str.lower(destination)  == 'blumentritt' or str.lower(origin) == 'blumentritt':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 26 pesos')
            elif str.lower(destination)  == 'abad santos' or str.lower(origin) == 'abad santos':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 27 pesos')
            elif str.lower(destination)  == 'r. papa' or str.lower(origin) == 'r. papa':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 28 pesos')
            elif str.lower(destination)  == '5th avenue' or str.lower(origin) == '5th avenue':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 29 pesos')
            elif str.lower(destination)  == 'monumento' or str.lower(origin) == 'monumento':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 30 pesos')
            elif str.lower(destination)  == 'balintawak' or str.lower(origin) == 'balintawak':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 33 pesos')
            elif str.lower(destination)  == 'fpj' or str.lower(origin) == 'fpj':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 35 pesos')
            else:
                print('Invalid')
        elif str.lower(origin) == 'edsa' or str.lower(destination) == 'edsa':
            if str.lower(destination)  == 'libertad' or str.lower(origin) == 'libertad' or str.lower(destination)  == 'gil puyat' or str.lower(origin) == 'gil puyat':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 15 pesos')
            elif str.lower(destination)  == 'vito cruz' or str.lower(origin) == 'vito cruz':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 17 pesos')
            elif str.lower(destination)  == 'quirino' or str.lower(origin) == 'quirino':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 18 pesos')
            elif str.lower(destination)  == 'pedro gil' or str.lower(origin) == 'pedro gil':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 19 pesos')
            elif str.lower(destination)  == 'un avenue' or str.lower(origin) == 'un avenue':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 20 pesos')
            elif str.lower(destination)  == 'central' or str.lower(origin) == 'central':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 21 pesos')
            elif str.lower(destination)  == 'carriedo' or str.lower(origin) == 'carriedo':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 22 pesos')
            elif str.lower(destination)  == 'd. jose' or str.lower(origin) == 'd. jose':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 23 pesos')
            elif str.lower(destination)  == 'bambang' or str.lower(origin) == 'bambang' or str.lower(destination)  == 'tayuman' or str.lower(origin) == 'tayuman':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 24 pesos')
            elif str.lower(destination)  == 'blumentritt' or str.lower(origin) == 'blumentritt':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 25 pesos')
            elif str.lower(destination)  == 'abad santos' or str.lower(origin) == 'abad santos':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 26 pesos')
            elif str.lower(destination)  == 'r. papa' or str.lower(origin) == 'r. papa':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 27 pesos')
            elif str.lower(destination)  == '5th avenue' or str.lower(origin) == '5th avenue':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 28 pesos')
            elif str.lower(destination)  == 'monumento' or str.lower(origin) == 'monumento':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 29 pesos')
            elif str.lower(destination)  == 'balintawak' or str.lower(origin) == 'balintawak':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 32 pesos')
            elif str.lower(destination)  == 'fpj' or str.lower(origin) == 'fpj':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 34 pesos')
            else:
                print('Invalid')
        elif str.lower(origin) == 'libertad' or str.lower(destination) == 'libertad':
            if str.lower(destination)  == 'gil puyat' or str.lower(origin) == 'gil puyat':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 14 pesos')
            elif str.lower(destination)  == 'vito cruz' or str.lower(origin) == 'vito cruz':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 15 pesos')
            elif str.lower(destination)  == 'quirino' or str.lower(origin) == 'quirino':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 16 pesos')
            elif str.lower(destination)  == 'pedro gil' or str.lower(origin) == 'pedro gil':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 17 pesos')
            elif str.lower(destination)  == 'un avenue' or str.lower(origin) == 'un avenue':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 18 pesos')
            elif str.lower(destination)  == 'central' or str.lower(origin) == 'central':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 20 pesos')
            elif str.lower(destination)  == 'carriedo' or str.lower(origin) == 'carriedo':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 21 pesos')
            elif str.lower(destination)  == 'd. jose' or str.lower(origin) == 'd. jose' or str.lower(destination)  == 'bambang' or str.lower(origin) == 'bambang':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 22 pesos')
            elif str.lower(destination)  == 'tayuman' or str.lower(origin) == 'tayuman':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 23 pesos')
            elif str.lower(destination)  == 'blumentritt' or str.lower(origin) == 'blumentritt':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 24 pesos')
            elif str.lower(destination)  == 'abad santos' or str.lower(origin) == 'abad santos':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 25 pesos')
            elif str.lower(destination)  == 'r. papa' or str.lower(origin) == 'r. papa':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 26 pesos')
            elif str.lower(destination)  == '5th avenue' or str.lower(origin) == '5th avenue':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 27 pesos')
            elif str.lower(destination)  == 'monumento' or str.lower(origin) == 'monumento':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 28 pesos')
            elif str.lower(destination)  == 'balintawak' or str.lower(origin) == 'balintawak':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 31 pesos')
            elif str.lower(destination)  == 'fpj' or str.lower(origin) == 'fpj':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 33 pesos')
            else:
                print('Invalid')
        elif str.lower(origin) == 'gil puyat' or str.lower(destination) == 'gil puyat':
            if str.lower(destination)  == 'vito cruz' or str.lower(origin) == 'vito cruz':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 15 pesos')
            elif str.lower(destination)  == 'quirino' or str.lower(origin) == 'quirino':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 16 pesos')
            elif str.lower(destination)  == 'pedro gil' or str.lower(origin) == 'pedro gil' or str.lower(destination)  == 'un avenue' or str.lower(origin) == 'un avenue':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 17 pesos')
            elif str.lower(destination)  == 'central' or str.lower(origin) == 'central':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 19 pesos')
            elif str.lower(destination)  == 'carriedo' or str.lower(origin) == 'carriedo':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 20 pesos')
            elif str.lower(destination)  == 'd. jose' or str.lower(origin) == 'd. jose' or str.lower(destination)  == 'bambang' or str.lower(origin) == 'bambang':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 21 pesos')
            elif str.lower(destination)  == 'tayuman' or str.lower(origin) == 'tayuman':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 22 pesos')
            elif str.lower(destination)  == 'blumentritt' or str.lower(origin) == 'blumentritt':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 23 pesos')
            elif str.lower(destination)  == 'abad santos' or str.lower(origin) == 'abad santos':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 24 pesos')
            elif str.lower(destination)  == 'r. papa' or str.lower(origin) == 'r. papa':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 25 pesos')
            elif str.lower(destination)  == '5th avenue' or str.lower(origin) == '5th avenue':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 26 pesos')
            elif str.lower(destination)  == 'monumento' or str.lower(origin) == 'monumento':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 27 pesos')
            elif str.lower(destination)  == 'balintawak' or str.lower(origin) == 'balintawak':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 30 pesos')
            elif str.lower(destination)  == 'fpj' or str.lower(origin) == 'fpj':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 32 pesos')
            else:
                print('Invalid')
        elif str.lower(origin) == 'vito cruz' or str.lower(destination) == 'vito cruz':
            if str.lower(destination) == 'quirino' or str.lower(origin) == 'quirino':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 14 pesos')
            elif str.lower(destination) == 'pedro gil' or str.lower(origin) == 'pedro gil':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 15 pesos')
            elif str.lower(destination) == 'un avenue' or str.lower(origin) == 'un avenue':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 16 pesos')
            elif str.lower(destination) == 'central' or str.lower(origin) == 'central':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 18 pesos')
            elif str.lower(destination) == 'carriedo' or str.lower(origin) == 'carriedo' or str.lower(destination) == 'd. jose' or str.lower(origin) == 'd. jose':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 19 pesos')
            elif str.lower(destination) == 'bambang' or str.lower(origin) == 'bambang':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 20 pesos')
            elif str.lower(destination) == 'tayuman' or str.lower(origin) == 'tayuman':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 21 pesos')
            elif str.lower(destination) == 'blumentritt' or str.lower(origin) == 'blumentritt':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 22 pesos')
            elif str.lower(destination) == 'abad santos' or str.lower(origin) == 'abad santos':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 23 pesos')
            elif str.lower(destination) == 'r. papa' or str.lower(origin) == 'r. papa':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 24 pesos')
            elif str.lower(destination) == '5th avenue' or str.lower(origin) == '5th avenue':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 25 pesos')
            elif str.lower(destination)  == 'monumento' or str.lower(origin) == 'monumento':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 26 pesos')
            elif str.lower(destination)  == 'balintawak' or str.lower(origin) == 'balintawak':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 29 pesos')
            elif str.lower(destination)  == 'fpj' or str.lower(origin) == 'fpj':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 31 pesos')
            else:
                print('Invalid')
        elif str.lower(origin) == 'quirino' or str.lower(destination) == 'quirino':
            if str.lower(destination) == 'pedro gil' or str.lower(origin) == 'pedro gil':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 14 pesos')
            elif str.lower(destination) == 'un avenue' or str.lower(origin) == 'un avenue':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 15 pesos')
            elif str.lower(destination) == 'central' or str.lower(origin) == 'central':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 17 pesos')
            elif str.lower(destination) == 'carriedo' or str.lower(origin) == 'carriedo' or str.lower(destination) == 'd. jose' or str.lower(origin) == 'd. jose':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 18 pesos')
            elif str.lower(destination) == 'bambang' or str.lower(origin) == 'bambang':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 19 pesos')
            elif str.lower(destination) == 'tayuman' or str.lower(origin) == 'tayuman':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 20 pesos')
            elif str.lower(destination) == 'blumentritt' or str.lower(origin) == 'blumentritt':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 21 pesos')
            elif str.lower(destination) == 'abad santos' or str.lower(origin) == 'abad santos':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 22 pesos')
            elif str.lower(destination) == 'r. papa' or str.lower(origin) == 'r. papa':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 23 pesos')
            elif str.lower(destination) == '5th avenue' or str.lower(origin) == '5th avenue':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 24 pesos')
            elif str.lower(destination)  == 'monumento' or str.lower(origin) == 'monumento':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 25 pesos')
            elif str.lower(destination)  == 'balintawak' or str.lower(origin) == 'balintawak':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 28 pesos')
            elif str.lower(destination)  == 'fpj' or str.lower(origin) == 'fpj':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 30 pesos')
            else:
                print('Invalid')
        elif str.lower(origin) == 'pedro gil' or str.lower(destination) == 'pedro gil':
            if str.lower(destination) == 'un avenue' or str.lower(origin) == 'un avenue':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 14 pesos')
            elif str.lower(destination) == 'central' or str.lower(origin) == 'central':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 16 pesos')
            elif str.lower(destination) == 'carriedo' or str.lower(origin) == 'carriedo' or str.lower(destination) == 'd. jose' or str.lower(origin) == 'd. jose':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 17 pesos')
            elif str.lower(destination) == 'bambang' or str.lower(origin) == 'bambang':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 18 pesos')
            elif str.lower(destination) == 'tayuman' or str.lower(origin) == 'tayuman':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 19 pesos')
            elif str.lower(destination) == 'blumentritt' or str.lower(origin) == 'blumentritt':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 20 pesos')
            elif str.lower(destination) == 'abad santos' or str.lower(origin) == 'abad santos':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 21 pesos')
            elif str.lower(destination) == 'r. papa' or str.lower(origin) == 'r. papa':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 22 pesos')
            elif str.lower(destination) == '5th avenue' or str.lower(origin) == '5th avenue':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 23 pesos')
            elif str.lower(destination)  == 'monumento' or str.lower(origin) == 'monumento':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 24 pesos')
            elif str.lower(destination)  == 'balintawak' or str.lower(origin) == 'balintawak':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 27 pesos')
            elif str.lower(destination)  == 'fpj' or str.lower(origin) == 'fpj':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 29 pesos')
            else:
                print('Invalid')
        elif str.lower(origin) == 'un avenue' or str.lower(destination) == 'un avenue':
            if str.lower(destination) == 'central' or str.lower(origin) == 'central':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 15 pesos')
            elif str.lower(destination) == 'carriedo' or str.lower(origin) == 'carriedo' or str.lower(destination) == 'd. jose' or str.lower(origin) == 'd. jose':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 16 pesos')
            elif str.lower(destination) == 'bambang' or str.lower(origin) == 'bambang':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 17 pesos')
            elif str.lower(destination) == 'tayuman' or str.lower(origin) == 'tayuman':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 18 pesos')
            elif str.lower(destination) == 'blumentritt' or str.lower(origin) == 'blumentritt':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 19 pesos')
            elif str.lower(destination) == 'abad santos' or str.lower(origin) == 'abad santos':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 20 pesos')
            elif str.lower(destination) == 'r. papa' or str.lower(origin) == 'r. papa':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 21 pesos')
            elif str.lower(destination) == '5th avenue' or str.lower(origin) == '5th avenue':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 22 pesos')
            elif str.lower(destination)  == 'monumento' or str.lower(origin) == 'monumento':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 23 pesos')
            elif str.lower(destination)  == 'balintawak' or str.lower(origin) == 'balintawak':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 26 pesos')
            elif str.lower(destination)  == 'fpj' or str.lower(origin) == 'fpj':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 28 pesos')
            else:
                print('Invalid')
        elif str.lower(origin) == 'central' or str.lower(destination) == 'central':
            if str.lower(destination) == 'carriedo' or str.lower(origin) == 'carriedo':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 14 pesos')
            elif str.lower(destination) == 'd. jose' or str.lower(origin) == 'd. jose':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 15 pesos')
            elif str.lower(destination) == 'bambang' or str.lower(origin) == 'bambang':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 16 pesos')
            elif str.lower(destination) == 'tayuman' or str.lower(origin) == 'tayuman' or str.lower(destination) == 'blumentritt' or str.lower(origin) == 'blumentritt':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 17 pesos')
            elif str.lower(destination) == 'abad santos' or str.lower(origin) == 'abad santos':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 18 pesos')
            elif str.lower(destination) == 'r. papa' or str.lower(origin) == 'r. papa':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 19 pesos')
            elif str.lower(destination) == '5th avenue' or str.lower(origin) == '5th avenue':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 20 pesos')
            elif str.lower(destination)  == 'monumento' or str.lower(origin) == 'monumento':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 22 pesos')
            elif str.lower(destination)  == 'balintawak' or str.lower(origin) == 'balintawak':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 24 pesos')
            elif str.lower(destination)  == 'fpj' or str.lower(origin) == 'fpj':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 27 pesos')
            else:
                print('Invalid')
        elif str.lower(origin) == 'carriedo' or str.lower(destination) == 'carriedo':
            if str.lower(destination) == 'd. jose' or str.lower(origin) == 'd. jose':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 14 pesos')
            elif str.lower(destination) == 'bambang' or str.lower(origin) == 'bambang':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 15 pesos')
            elif str.lower(destination) == 'tayuman' or str.lower(origin) == 'tayuman' or str.lower(destination) == 'blumentritt' or str.lower(origin) == 'blumentritt':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 16 pesos')
            elif str.lower(destination) == 'abad santos' or str.lower(origin) == 'abad santos' or str.lower(destination) == 'r. papa' or str.lower(origin) == 'r. papa':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 18 pesos')
            elif str.lower(destination) == '5th avenue' or str.lower(origin) == '5th avenue':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 20 pesos')
            elif str.lower(destination)  == 'monumento' or str.lower(origin) == 'monumento':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 21 pesos')
            elif str.lower(destination)  == 'balintawak' or str.lower(origin) == 'balintawak':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 24 pesos')
            elif str.lower(destination)  == 'fpj' or str.lower(origin) == 'fpj':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 26 pesos')
            else:
                print('Invalid')
        elif str.lower(origin) == 'd. jose' or str.lower(destination) == 'd. jose':
            if str.lower(destination) == 'bambang' or str.lower(origin) == 'bambang':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 14 pesos')
            elif str.lower(destination) == 'tayuman' or str.lower(origin) == 'tayuman':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 15 pesos')
            elif str.lower(destination) == 'blumentritt' or str.lower(origin) == 'blumentritt':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 16 pesos')
            elif str.lower(destination) == 'abad santos' or str.lower(origin) == 'abad santos':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 17 pesos')
            elif str.lower(destination) == 'r. papa' or str.lower(origin) == 'r. papa':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 18 pesos')
            elif str.lower(destination) == '5th avenue' or str.lower(origin) == '5th avenue':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 19 pesos')
            elif str.lower(destination)  == 'monumento' or str.lower(origin) == 'monumento':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 20 pesos')
            elif str.lower(destination)  == 'balintawak' or str.lower(origin) == 'balintawak':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 23 pesos')
            elif str.lower(destination)  == 'fpj' or str.lower(origin) == 'fpj':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 25 pesos')
            else:
                print('Invalid')
        elif str.lower(origin) == 'bambang' or str.lower(destination) == 'bambang':
            if str.lower(destination) == 'tayuman' or str.lower(origin) == 'tayuman':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 14 pesos')
            elif str.lower(destination) == 'blumentritt' or str.lower(origin) == 'blumentritt':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 15 pesos')
            elif str.lower(destination) == 'abad santos' or str.lower(origin) == 'abad santos':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 16 pesos')
            elif str.lower(destination) == 'r. papa' or str.lower(origin) == 'r. papa':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 17 pesos')
            elif str.lower(destination) == '5th avenue' or str.lower(origin) == '5th avenue':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 18 pesos')
            elif str.lower(destination)  == 'monumento' or str.lower(origin) == 'monumento':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 19 pesos')
            elif str.lower(destination)  == 'balintawak' or str.lower(origin) == 'balintawak':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 22 pesos')
            elif str.lower(destination)  == 'fpj' or str.lower(origin) == 'fpj':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 24 pesos')
            else:
                print('Invalid')
        elif str.lower(origin) == 'tayuman' or str.lower(destination) == 'tayuman':
            if str.lower(destination) == 'blumentritt' or str.lower(origin) == 'blumentritt':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 14 pesos')
            elif str.lower(destination) == 'abad santos' or str.lower(origin) == 'abad santos':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 15 pesos')
            elif str.lower(destination) == 'r. papa' or str.lower(origin) == 'r. papa':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 16 pesos')
            elif str.lower(destination) == '5th avenue' or str.lower(origin) == '5th avenue':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 17 pesos')
            elif str.lower(destination)  == 'monumento' or str.lower(origin) == 'monumento':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 18 pesos')
            elif str.lower(destination)  == 'balintawak' or str.lower(origin) == 'balintawak':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 21 pesos')
            elif str.lower(destination)  == 'fpj' or str.lower(origin) == 'fpj':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 23 pesos')
            else:
                print('Invalid')
        elif str.lower(origin) == 'blumentritt' or str.lower(destination) == 'blumentritt':
            if str.lower(destination) == 'abad santos' or str.lower(origin) == 'abad santos':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 14 pesos')
            elif str.lower(destination) == 'r. papa' or str.lower(origin) == 'r. papa':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 15 pesos')
            elif str.lower(destination) == '5th avenue' or str.lower(origin) == '5th avenue':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 16 pesos')
            elif str.lower(destination)  == 'monumento' or str.lower(origin) == 'monumento':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 18 pesos')
            elif str.lower(destination)  == 'balintawak' or str.lower(origin) == 'balintawak':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 20 pesos')
            elif str.lower(destination)  == 'fpj' or str.lower(origin) == 'fpj':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 23 pesos')
            else:
                print('Invalid')
        elif str.lower(origin) == 'abad santos' or str.lower(destination) == 'abad santos':
            if str.lower(destination) == 'r. papa' or str.lower(origin) == 'r. papa':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 14 pesos')
            elif str.lower(destination) == '5th avenue' or str.lower(origin) == '5th avenue':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 15 pesos')
            elif str.lower(destination)  == 'monumento' or str.lower(origin) == 'monumento':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 17 pesos')
            elif str.lower(destination)  == 'balintawak' or str.lower(origin) == 'balintawak':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 19 pesos')
            elif str.lower(destination)  == 'fpj' or str.lower(origin) == 'fpj':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 22 pesos')
            else:
                print('Invalid')
        elif str.lower(origin) == 'r. papa' or str.lower(destination) == 'r. papa':
            if str.lower(destination) == '5th avenue' or str.lower(origin) == '5th avenue':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 14 pesos')
            elif str.lower(destination)  == 'monumento' or str.lower(origin) == 'monumento':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 16 pesos')
            elif str.lower(destination)  == 'balintawak' or str.lower(origin) == 'balintawak':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 18 pesos')
            elif str.lower(destination)  == 'fpj' or str.lower(origin) == 'fpj':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 21 pesos')
            else:
                print('Invalid')
        elif str.lower(origin) == '5th avenue' or str.lower(destination) == '5th avenue':
            if str.lower(destination)  == 'monumento' or str.lower(origin) == 'monumento':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 15 pesos')
            elif str.lower(destination)  == 'balintawak' or str.lower(origin) == 'balintawak':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 17 pesos')
            elif str.lower(destination)  == 'fpj' or str.lower(origin) == 'fpj':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 20 pesos')
            else:
                print('Invalid')
        elif str.lower(origin) == 'monumento' or str.lower(destination) == 'monumento':
            if str.lower(destination)  == 'balintawak' or str.lower(origin) == 'balintawak':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 16 pesos')
            elif str.lower(destination)  == 'fpj' or str.lower(origin) == 'fpj':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 18 pesos')
            else:
                print('Invalid')
        elif str.lower(origin) == 'balintawak' or str.lower(destination) == 'balintawak':
            if str.lower(destination)  == 'fpj' or str.lower(origin) == 'fpj':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 16 pesos')
            else:
                print('Invalid')
        else:
            print('Unavailable Route')
        
    else:
        print('Invalid')
        
if str.lower(lrt_line) == 'lrt 2':
    type_of_ticket = input('Do you have a stored value BEEP card in hand?')

    if str.lower(type_of_ticket) == 'no':
        origin = input('Origin:')
        destination = input('Destination:')
        
        if str.lower(origin) == 'recto' or str.lower(destination) == 'recto':
            if str.lower(origin) == 'legarda' or str.lower(destination) == 'legarda':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 15 pesos')
            elif str.lower(origin) == 'pureza' or str.lower(destination) == 'pureza' or str.lower(origin) == 'v. mapa' or str.lower(destination) == 'v. mapa' or str.lower(origin) == 'j. ruiz' or str.lower(destination) == 'j. ruiz':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 20 pesos')
            elif str.lower(origin) == 'gilmore' or str.lower(destination) == 'gilmore' or str.lower(origin) == 'betty go' or str.lower(destination) == 'betty go' or str.lower(origin) == 'cubao' or str.lower(destination) == 'cubao' or str.lower(origin) == 'anonas' or str.lower(destination) == 'anonas':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 25 pesos')
            elif str.lower(origin) == 'katipunan' or str.lower(destination) == 'katipunan' or str.lower(origin) == 'santolan' or str.lower(destination) == 'santolan':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 30 pesos')
            elif str.lower(origin) == 'marikina' or str.lower(destination) == 'marikina' or str.lower(origin) == 'antipolo' or str.lower(destination) == 'antipolo':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 35 pesos')
        elif str.lower(origin) == 'legarda' or str.lower(destination) == 'legarda':
            if str.lower(origin) == 'pureza' or str.lower(destination) == 'pureza':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 15 pesos')
            elif str.lower(origin) == 'v. mapa' or str.lower(destination) == 'v. mapa' or str.lower(origin) == 'j. ruiz' or str.lower(destination) == 'j. ruiz' or str.lower(origin) == 'gilmore' or str.lower(destination) == 'gilmore':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 20 pesos')
            elif str.lower(origin) == 'betty go' or str.lower(destination) == 'betty go' or str.lower(origin) == 'cubao' or str.lower(destination) == 'cubao' or str.lower(origin) == 'anonas' or str.lower(destination) == 'anonas' or str.lower(origin) == 'katipunan' or str.lower(destination) == 'katipunan':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 25 pesos')
            elif str.lower(origin) == 'santolan' or str.lower(destination) == 'santolan' or str.lower(origin) == 'marikina' or str.lower(destination) == 'marikina':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 30 pesos')
            elif str.lower(origin) == 'antipolo' or str.lower(destination) == 'antipolo':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 35 pesos')
        elif str.lower(origin) == 'pureza' or str.lower(destination) == 'pureza':    
            if str.lower(origin) == 'v. mapa' or str.lower(destination) == 'v. mapa':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 15 pesos')
            elif str.lower(origin) == 'j. ruiz' or str.lower(destination) == 'j. ruiz' or str.lower(origin) == 'gilmore' or str.lower(destination) == 'gilmore' or str.lower(origin) == 'betty go' or str.lower(destination) == 'betty go' or str.lower(origin) == 'cubao' or str.lower(destination) == 'cubao':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 20 pesos')
            elif str.lower(origin) == 'anonas' or str.lower(destination) == 'anonas' or str.lower(origin) == 'katipunan' or str.lower(destination) == 'katipunan':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 25 pesos')
            elif str.lower(origin) == 'santolan' or str.lower(destination) == 'santolan' or str.lower(origin) == 'marikina' or str.lower(destination) == 'marikina' or str.lower(origin) == 'antipolo' or str.lower(destination) == 'antipolo':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 30 pesos')
        elif str.lower(origin) == 'v. mapa' or str.lower(destination) == 'v. mapa': 
            if str.lower(origin) == 'j. ruiz' or str.lower(destination) == 'j. ruiz':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 15 pesos')
            elif str.lower(origin) == 'gilmore' or str.lower(destination) == 'gilmore' or str.lower(origin) == 'betty go' or str.lower(destination) == 'betty go' or str.lower(origin) == 'cubao' or str.lower(destination) == 'cubao' or str.lower(origin) == 'anonas' or str.lower(destination) == 'anonas':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 20 pesos')
            elif str.lower(origin) == 'katipunan' or str.lower(destination) == 'katipunan' or str.lower(origin) == 'santolan' or str.lower(destination) == 'santolan':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 25 pesos')
            elif str.lower(origin) == 'marikina' or str.lower(destination) == 'marikina' or str.lower(origin) == 'antipolo' or str.lower(destination) == 'antipolo':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 30 pesos')
        elif str.lower(origin) == 'j. ruiz' or str.lower(destination) == 'j. ruiz': 
            if str.lower(origin) == 'gilmore' or str.lower(destination) == 'gilmore':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 15 pesos')
            elif str.lower(origin) == 'betty go' or str.lower(destination) == 'betty go' or str.lower(origin) == 'cubao' or str.lower(destination) == 'cubao' or str.lower(origin) == 'anonas' or str.lower(destination) == 'anonas' or str.lower(origin) == 'katipunan' or str.lower(destination) == 'katipunan':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 20 pesos')
            elif str.lower(origin) == 'santolan' or str.lower(destination) == 'santolan' or str.lower(origin) == 'marikina' or str.lower(destination) == 'marikina':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 25 pesos')
            elif str.lower(origin) == 'antipolo' or str.lower(destination) == 'antipolo':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 30 pesos')
        elif str.lower(origin) == 'gilmore' or str.lower(destination) == 'gilmore': 
            if str.lower(origin) == 'betty go' or str.lower(destination) == 'betty go':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 15 pesos')
            elif str.lower(origin) == 'cubao' or str.lower(destination) == 'cubao' or str.lower(origin) == 'anonas' or str.lower(destination) == 'anonas' or str.lower(origin) == 'katipunan' or str.lower(destination) == 'katipunan':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 20 pesos')
            elif str.lower(origin) == 'santolan' or str.lower(destination) == 'santolan' or str.lower(origin) == 'marikina' or str.lower(destination) == 'marikina':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 25 pesos')
            elif str.lower(origin) == 'antipolo' or str.lower(destination) == 'antipolo':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 30 pesos')
        elif str.lower(origin) == 'betty go' or str.lower(destination) == 'betty go': 
            if str.lower(origin) == 'cubao' or str.lower(destination) == 'cubao':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 15 pesos')
            elif str.lower(origin) == 'anonas' or str.lower(destination) == 'anonas' or str.lower(origin) == 'katipunan' or str.lower(destination) == 'katipunan' or str.lower(origin) == 'santolan' or str.lower(destination) == 'santolan':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 20 pesos')
            elif str.lower(origin) == 'marikina' or str.lower(destination) == 'marikina' or str.lower(origin) == 'antipolo' or str.lower(destination) == 'antipolo':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 25 pesos')
        elif str.lower(origin) == 'cubao' or str.lower(destination) == 'cubao': 
            if str.lower(origin) == 'anonas' or str.lower(destination) == 'anonas':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 15 pesos')
            elif str.lower(origin) == 'katipunan' or str.lower(destination) == 'katipunan' or str.lower(origin) == 'santolan' or str.lower(destination) == 'santolan':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 20 pesos')
            elif str.lower(origin) == 'marikina' or str.lower(destination) == 'marikina' or str.lower(origin) == 'antipolo' or str.lower(destination) == 'antipolo':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 25 pesos')
        elif str.lower(origin) == 'anonas' or str.lower(destination) == 'anonas': 
            if str.lower(origin) == 'katipunan' or str.lower(destination) == 'katipunan':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 15 pesos')
            elif str.lower(origin) == 'santolan' or str.lower(destination) == 'santolan' or str.lower(origin) == 'marikina' or str.lower(destination) == 'marikina':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 20 pesos')
            elif str.lower(origin) == 'antipolo' or str.lower(destination) == 'antipolo':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 25 pesos')
        elif str.lower(origin) == 'katipunan' or str.lower(destination) == 'katipunan': 
            if str.lower(origin) == 'santolan' or str.lower(destination) == 'santolan' or str.lower(origin) == 'marikina' or str.lower(destination) == 'marikina':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 20 pesos')
            elif str.lower(origin) == 'antipolo' or str.lower(destination) == 'antipolo':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 25 pesos')
        elif str.lower(origin) == 'santolan' or str.lower(destination) == 'santolan': 
            if str.lower(origin) == 'marikina' or str.lower(destination) == 'marikina':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 15 pesos')
            elif str.lower(origin) == 'antipolo' or str.lower(destination) == 'antipolo':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 20 pesos')
        elif str.lower(origin) == 'marikina' or str.lower(destination) == 'marikina': 
            if str.lower(origin) == 'antipolo' or str.lower(destination) == 'antipolo':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 20 pesos')
        else:
            print('Unavailable Route')
    
    elif str.lower(type_of_ticket) == 'yes':
        origin = input('Origin:')
        destination = input('Destination:')
        
        if str.lower(origin) == 'recto' or str.lower(destination) == 'recto':
            if str.lower(origin) == 'legarda' or str.lower(destination) == 'legarda':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 15 pesos')
            elif str.lower(origin) == 'pureza' or str.lower(destination) == 'pureza':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 16 pesos')
            elif str.lower(origin) == 'v. mapa' or str.lower(destination) == 'v. mapa':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 18 pesos')
            elif str.lower(origin) == 'j. ruiz' or str.lower(destination) == 'j. ruiz':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 19 pesos')
            elif str.lower(origin) == 'gilmore' or str.lower(destination) == 'gilmore':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 21 pesos')
            elif str.lower(origin) == 'betty go' or str.lower(destination) == 'betty go':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 22 pesos')
            elif str.lower(origin) == 'cubao' or str.lower(destination) == 'cubao':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 23 pesos')
            elif str.lower(origin) == 'anonas' or str.lower(destination) == 'anonas':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 25 pesos')
            elif str.lower(origin) == 'katipunan' or str.lower(destination) == 'katipunan':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 26 pesos')
            elif str.lower(origin) == 'santolan' or str.lower(destination) == 'santolan':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 28 pesos')
            elif str.lower(origin) == 'marikina' or str.lower(destination) == 'marikina':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 31 pesos')
            elif str.lower(origin) == 'antipolo' or str.lower(destination) == 'antipolo':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 33 pesos')
        elif str.lower(origin) == 'legarda' or str.lower(destination) == 'legarda':
            if str.lower(origin) == 'pureza' or str.lower(destination) == 'pureza':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 15 pesos')
            elif str.lower(origin) == 'v. mapa' or str.lower(destination) == 'v. mapa':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 17 pesos')
            elif str.lower(origin) == 'j. ruiz' or str.lower(destination) == 'j. ruiz':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 18 pesos')
            elif str.lower(origin) == 'gilmore' or str.lower(destination) == 'gilmore':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 19 pesos')
            elif str.lower(origin) == 'betty go' or str.lower(destination) == 'betty go':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 21 pesos')
            elif str.lower(origin) == 'cubao' or str.lower(destination) == 'cubao':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 22 pesos')
            elif str.lower(origin) == 'anonas' or str.lower(destination) == 'anonas':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 24 pesos')
            elif str.lower(origin) == 'katipunan' or str.lower(destination) == 'katipunan':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 25 pesos')
            elif str.lower(origin) == 'santolan' or str.lower(destination) == 'santolan':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 27 pesos')
            elif str.lower(origin) == 'marikina' or str.lower(destination) == 'marikina':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 29 pesos')
            elif str.lower(origin) == 'antipolo' or str.lower(destination) == 'antipolo':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 32 pesos')
        elif str.lower(origin) == 'v. mapa' or str.lower(destination) == 'v. mapa':
            if str.lower(origin) == 'v. mapa' or str.lower(destination) == 'v. mapa':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 15 pesos')
            elif str.lower(origin) == 'j. ruiz' or str.lower(destination) == 'j. ruiz':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 16 pesos')
            elif str.lower(origin) == 'gilmore' or str.lower(destination) == 'gilmore':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 18 pesos')
            elif str.lower(origin) == 'betty go' or str.lower(destination) == 'betty go':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 19 pesos')
            elif str.lower(origin) == 'cubao' or str.lower(destination) == 'cubao':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 20 pesos')
            elif str.lower(origin) == 'anonas' or str.lower(destination) == 'anonas':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 22 pesos')
            elif str.lower(origin) == 'katipunan' or str.lower(destination) == 'katipunan':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 23 pesos')
            elif str.lower(origin) == 'santolan' or str.lower(destination) == 'santolan':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 26 pesos')
            elif str.lower(origin) == 'marikina' or str.lower(destination) == 'marikina':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 28 pesos')
            elif str.lower(origin) == 'antipolo' or str.lower(destination) == 'antipolo':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 30 pesos')
        elif str.lower(origin) == 'pureza' or str.lower(destination) == 'pureza':
            if str.lower(origin) == 'j. ruiz' or str.lower(destination) == 'j. ruiz':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 15 pesos')
            elif str.lower(origin) == 'gilmore' or str.lower(destination) == 'gilmore':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 16 pesos')
            elif str.lower(origin) == 'betty go' or str.lower(destination) == 'betty go':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 17 pesos')
            elif str.lower(origin) == 'cubao' or str.lower(destination) == 'cubao':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 19 pesos')
            elif str.lower(origin) == 'anonas' or str.lower(destination) == 'anonas':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 20 pesos')
            elif str.lower(origin) == 'katipunan' or str.lower(destination) == 'katipunan':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 22 pesos')
            elif str.lower(origin) == 'santolan' or str.lower(destination) == 'santolan':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 24 pesos')
            elif str.lower(origin) == 'marikina' or str.lower(destination) == 'marikina':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 26 pesos')
            elif str.lower(origin) == 'antipolo' or str.lower(destination) == 'antipolo':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 29 pesos')
        elif str.lower(origin) == 'j. ruiz' or str.lower(destination) == 'j. ruiz':
            if str.lower(origin) == 'gilmore' or str.lower(destination) == 'gilmore':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 14 pesos')
            elif str.lower(origin) == 'betty go' or str.lower(destination) == 'betty go':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 16 pesos')
            elif str.lower(origin) == 'cubao' or str.lower(destination) == 'cubao':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 17 pesos')
            elif str.lower(origin) == 'anonas' or str.lower(destination) == 'anonas':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 19 pesos')
            elif str.lower(origin) == 'katipunan' or str.lower(destination) == 'katipunan':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 20 pesos')
            elif str.lower(origin) == 'santolan' or str.lower(destination) == 'santolan':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 22 pesos')
            elif str.lower(origin) == 'marikina' or str.lower(destination) == 'marikina':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 24 pesos')
            elif str.lower(origin) == 'antipolo' or str.lower(destination) == 'antipolo':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 27 pesos')
        elif str.lower(origin) == 'gilmore' or str.lower(destination) == 'gilmore':
            if str.lower(origin) == 'betty go' or str.lower(destination) == 'betty go':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 15 pesos')
            elif str.lower(origin) == 'cubao' or str.lower(destination) == 'cubao':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 16 pesos')
            elif str.lower(origin) == 'anonas' or str.lower(destination) == 'anonas':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 18 pesos')
            elif str.lower(origin) == 'katipunan' or str.lower(destination) == 'katipunan':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 19 pesos')
            elif str.lower(origin) == 'santolan' or str.lower(destination) == 'santolan':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 21 pesos')
            elif str.lower(origin) == 'marikina' or str.lower(destination) == 'marikina':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 23 pesos')
            elif str.lower(origin) == 'antipolo' or str.lower(destination) == 'antipolo':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 26 pesos')
        elif str.lower(origin) == 'betty go' or str.lower(destination) == 'betty go':
            if str.lower(origin) == 'cubao' or str.lower(destination) == 'cubao':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 15 pesos')
            elif str.lower(origin) == 'anonas' or str.lower(destination) == 'anonas':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 16 pesos')
            elif str.lower(origin) == 'katipunan' or str.lower(destination) == 'katipunan':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 18 pesos')
            elif str.lower(origin) == 'santolan' or str.lower(destination) == 'santolan':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 20 pesos')
            elif str.lower(origin) == 'marikina' or str.lower(destination) == 'marikina':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 22 pesos')
            elif str.lower(origin) == 'antipolo' or str.lower(destination) == 'antipolo':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 25 pesos')   
        elif str.lower(origin) == 'cubao' or str.lower(destination) == 'cubao':
            if str.lower(origin) == 'anonas' or str.lower(destination) == 'anonas':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 15 pesos')
            elif str.lower(origin) == 'katipunan' or str.lower(destination) == 'katipunan':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 16 pesos')
            elif str.lower(origin) == 'santolan' or str.lower(destination) == 'santolan':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 19 pesos')
            elif str.lower(origin) == 'marikina' or str.lower(destination) == 'marikina':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 21 pesos')
            elif str.lower(origin) == 'antipolo' or str.lower(destination) == 'antipolo':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 23 pesos')
        elif str.lower(origin) == 'anonas' or str.lower(destination) == 'anonas':
            if str.lower(origin) == 'katipunan' or str.lower(destination) == 'katipunan':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 14 pesos')
            elif str.lower(origin) == 'santolan' or str.lower(destination) == 'santolan':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 17 pesos')
            elif str.lower(origin) == 'marikina' or str.lower(destination) == 'marikina':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 19 pesos')
            elif str.lower(origin) == 'antipolo' or str.lower(destination) == 'antipolo':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 22 pesos')
        elif str.lower(origin) == 'katipunan' or str.lower(destination) == 'katipunan':
            if str.lower(origin) == 'santolan' or str.lower(destination) == 'santolan':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 16 pesos')
            elif str.lower(origin) == 'marikina' or str.lower(destination) == 'marikina':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 18 pesos')
            elif str.lower(origin) == 'antipolo' or str.lower(destination) == 'antipolo':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 21 pesos')
        elif str.lower(origin) == 'santolan' or str.lower(destination) == 'santolan':
            if str.lower(origin) == 'marikina' or str.lower(destination) == 'marikina':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 15 pesos')
            elif str.lower(origin) == 'antipolo' or str.lower(destination) == 'antipolo':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 18 pesos')
        elif str.lower(origin) == 'marikina' or str.lower(destination) == 'marikina':
            if str.lower(origin) == 'antipolo' or str.lower(destination) == 'antipolo':
                print('Fare from', str.title(origin), 'to', str.title(destination), ': 16 pesos')
        else:
            print('Unavailable Route')
    
    else:
        print('Invalid')
        
else:
    print ('Invalid LRT Line')

