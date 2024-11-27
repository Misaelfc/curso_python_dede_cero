### Dates ###
# Las fechas son representaciones de momentos en el tiempo. Se pueden manejar mediante módulos como datetime o time, que permiten trabajar con fechas y horas de manera fácil y precisa. Estos módulos proporcionan clases y funciones para crear, manipular, y formatear fechas y horas.

# Date time

from datetime import timedelta
from datetime import date
from datetime import time
from datetime import datetime

now = datetime.now()

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp()) # es un número flotante que representa la cantidad de segundos transcurridos desde el 1 de enero de 1970 a las 00:00:00 UTC
    
print_date(now)

year_2025 = datetime(2025, 1, 1)

print_date(year_2025)

# Time

current_time = time(21, 6, 0)

print(current_time.hour)
print(current_time.minute)
print(current_time.second)

# Date

current_date = date.today()

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(2022, 10, 6)

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(current_date.year, current_date.month + 1, current_date.day)

print(current_date.month)

# Operaciones con fechas

diff = year_2025 - now
print(diff)

diff = year_2025.date() - current_date
print(diff)

# Timedelta

start_timedelta = timedelta(200, 100, 100, weeks=10)
end_timedelta = timedelta(300, 100, 100, weeks=13)

print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)