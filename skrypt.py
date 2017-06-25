"""print("hello")
if 5>2:
    print("zgadza się")
else:
    print('jendak nie')
name='Sonja'
if name=="Ola":
    print('Hej Ola')
elif name=='Sonja':
    print ('Hej Sonja')
else:
    print('Hej kimkolwiek jestes')
def hej(imie):
    if imie == 'Ola':
        print('Hej Ola!')
    elif imie == 'Sonja':
        print('Hej Sonja!')
    else:
        print('Hej nieznajoma!')

hej('Aria')
def hej(imie):
    print('hej '+ imie +' !')
hej('Aria')"""
def hej(imie):
    print('Hej ' + imie + '!')

dziewczyny = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'Ty']
for imie in dziewczyny:
    hej(imie)
    print('Kolejna dziewczyna')
