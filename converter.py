def convert():
    print('1. kg to lbs')
    print('2. lbs to kg')
    choice = input('select 1 or 2: ')
    if choice == '1':
        kg = float(input('Enter kg: '))
        lbs = round(kg *  2.205,2) 
        print(f'{kg} kg ≈ {lbs} lbs')

    elif choice == '2':
        lbs = float(input('Enter lbs: '))
        kg = round(lbs /  2.205,2)
        print(f'{lbs} lbs ≈ {kg} kg')
    else:
        print(f'there is no {choice} in choices')

convert()