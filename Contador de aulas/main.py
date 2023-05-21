import datetime as dt
import pandas as pd
data = dt.datetime
today = data.now().date()
date = dt.date(year=2023,month=5,day=22)

per_day = {}
n = 0

for i in range(45,99):

    a = i
    b = i+1
    c = i+2
    day = today + dt.timedelta(days=n)
    day_s = f'{day}'
    per_day[day_s] = (a,b,c)
    i += 3
    n += 1

data = pd.DataFrame(per_day)
print(data['2023-05-04'])

#contador de aulas
#obj: digitar a data de inicio, o numero de aulas que quer fazer por dia, retornar a data de fim
#op2 digitar o dia e retoranar quais as aulas de hoje
#op3 fallow up se fez as aulas