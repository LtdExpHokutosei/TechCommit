while True:

    temp = input('Number? > ')

    if temp == 'exit':
        break

    try:
        num = int(temp)        

    except:
        print('1から100までの半角アラビア数字を入れてください。\n')
        continue


    if 1 <= num <= 100:

        result = ''

        if num % 3 == 0:
            result += 'Fizz'
        if num % 5 == 0:
            result += 'Buzz'
        
        if result == '':
            result = str(num) +' （3の倍数でも5の倍数でもありませんでした。）'
        
        print(result + '\n')

    else:
        print('1から100までの半角アラビア数字を入れてください。\n')
    
