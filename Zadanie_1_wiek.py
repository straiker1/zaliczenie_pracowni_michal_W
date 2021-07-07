#!/usr/bin/python3

import datetime

currentDate = datetime.date.today()
aktRok = currentDate.year
rokur = None
wiek = None


rokur = int(input('w ktorym roku sie urodziles? '))

if rokur > aktRok:
    print('podales bledny rok urodzenia')
else:
    wiek = aktRok - rokur
    print( 'masz', wiek, 'lat' )
