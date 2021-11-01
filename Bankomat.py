sum = int(input('Введите сумму которую хотите снять '))

while sum >= 1000:
    print('1000')
    sum -= 1000
    if sum < 1000:
        break
while sum >= 500:
    print('500')
    sum -= 500
    if sum < 500:
        break
while sum >= 200:
    print('200')
    sum -= 200
    if sum < 200:
        break
while sum >= 100:
    print('100')
    sum -= 100
    if sum < 100:
        break
while sum >= 50:
    print ('50')
    sum -= 50
    if sum < 50:
        break
while sum >= 20:
    print (20)
    sum -= 20
    if sum < 20:
        break
while sum >= 5:
    print(5)
    sum -=5
    if sum < 5:
        break
while sum >= 2:
    print('2')
    sum -= 2
    if sum < 2:
        break
while sum == 1:
    print('1')
    break