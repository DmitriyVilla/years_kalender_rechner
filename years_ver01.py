import colorama
from colorama import Fore, Back, Style
colorama.init()
print(Fore.CYAN + 'Das Programm berechnet die Jahre, deren Kalender identisch ist')
def year_kalender():
    year = input('Geben Sie Jahr ein: ')
    while year == 'x':
        exit()

    while type(year) != int:
        try:
            year = int(year)
        except ValueError:
            print(Fore.RED + "Das ist kein Jahr")
            year = input('Schreiben Sie ein Jahr (z.B.: 2007, 1700):')

    visokos = int(year) % 4 == 0 or (int(year) % 100 != 0 and int(year) % 400 == 0)

    year1 = int(year - 1) % 4 == 0 or (int(year - 1) % 100 != 0 and int(year - 1) % 400 == 0)
    year2 = int(year - 2) % 4 == 0 or (int(year - 2) % 100 != 0 and int(year - 2) % 400 == 0)
    year3 = int(year - 3) % 4 == 0 or (int(year - 3) % 100 != 0 and int(year - 3) % 400 == 0)
    if visokos == True:
        print(Fore.GREEN + '{0} Das ist Schaltjahr.'.format(year))
        print(Fore.CYAN + 'Kalender sind identisch bei ', year - 28 * 3, ',', year - 28 * 2, ',', year - 28,
          '\n gleich Kalender wird bei ', year + 28, 'und', year + 28 * 2, 'Jahren')

    if year1 == True:
        print(Fore.CYAN + 'Für dieses Jahr wird ein Kalender von', year - 11, ', und es ist auch geeignet für', year + 6)
    elif year2 == True:
        print(Fore.CYAN + 'Für dieses Jahr wird ein Kalender von', year - 11, ', und es ist auch geeignet für', year + 11)
    elif year3 == True:
        print(Fore.CYAN + 'Für dieses Jahr wird ein Kalender von', year - 6, ', und es ist auch geeignet für', year + 11)

year_kalendar()
while True:
    print(Fore.RED + 'um das Programm zu schließen  - x')
    year_kalendar()












