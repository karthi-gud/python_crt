import pandas as pd
calories ={"day1":230,"day2":240,"day3":250,"day4":260,}
lolly=pd.Series(calories,index=['day1','day2','day3','day4'])
print(lolly)