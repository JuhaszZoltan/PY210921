# nev = input('írd be a neved: ')
# print(f'Szia {nev}! Milyen szép napunk van!')
# print(100 * nev)

# nev = input('írd be a neved: ')
# szerecc = input(f'Szia {nev} szeretsz programozni? ')
# if szerecc == 'igen':
#     print('akkor még sokra viheted! :*')
# else: print('akkor fogadj CS:GO meccsekre inkább!')

# iranyitoszam = input('irányítószám: ')
# varos = input('város: ')
# kozteruletNeve = input('közterület neve: ')
# kozteruletJellege = input('közterület jellege: ')
# hazSzam = input('házszám: ')

# print(f'{iranyitoszam} {varos}, {kozteruletNeve} {kozteruletJellege}, {hazSzam}.')

# vezetekNev1 = input('első vezetéknév: ')
# vezetekNev2 = input('második vezetéknév: ')
# keresztNev1 = input('első keresztnév: ')
# keresztNev2 = input('második keresztnév: ')

# print(f'{vezetekNev1} {keresztNev1}')
# print(f'{vezetekNev1} {keresztNev2}')
# print(f'{vezetekNev2} {keresztNev1}')
# print(f'{vezetekNev2} {keresztNev2}')

# haviFizetes = int(input('havi fizetés: '))
# print(f'éves fizetés: {haviFizetes * 12}')

tomeg = float(input("tömeged(Kg): "))
magassag = float(input('magasságod(cm): ')) / 100

tti = tomeg / (magassag * magassag)

if (tti < 16): print('súlyos soványság')
elif (tti < 17): print('mérsékelt soványság')
elif (tti < 19.5): print('enyhe soványság')
elif (tti < 25): print('normális testsúly')
elif (tti < 30): print('túlsúlyos')
elif (tti < 35): print('I. fokú elhízás')
elif (tti < 40): print('II. fokú elhízás')
else: print('III. fokú (súlyos) elhízás') 