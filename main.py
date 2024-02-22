print('c = celsius\nf = fahrenheit\nk = kelvin')
print('-----------------')
cov1 = input('oque deseja converter? ')
cov2 = input('em deseja converter? ')
n1 = int(input('temperatura: '))

#c/5 = (f-32)/9 = (k-273)/5

#celsius
if cov1 == 'c':
    #fahrenheit
    if cov2 == 'f':
        res = (n1*9/5)+32 
    #kelvin
    if cov2 == 'k':
        res = n1+273

#fahrenheit
if cov1 == 'f':
    #celsius
    if cov2 == 'c':
        res = (n1-32)*5/9
    #kelvin
    if cov2 == 'k':
        res = (n1-32)*5/9+273

#kelvin
if cov1 == 'k':
    #celsius
    if cov2 == 'c':
        res = n1 - 273
    #fharenheit
    if cov2 == 'f':
        res = (n1-273)*9/5+32

print(int(res))
