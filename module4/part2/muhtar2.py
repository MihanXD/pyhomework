sharik = input().split()
muhtar = 0
drujok = 0
tuzik = 0
for bobik in sharik:
    if int(bobik) > 0:
        muhtar += 1
    elif int(bobik) < 0:
        drujok += 1
    elif int(bobik) == 0:
        tuzik += 1
print(muhtar, drujok, tuzik)
