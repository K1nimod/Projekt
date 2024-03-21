def mpbe( o, p , mp):
    return mp + p*60 + o*60*60

f = open("hivas.txt", "rt", encoding="utf-8") 

hivasok = []

for sor in f:
    sor = sor.strip().split(" ")
    sor = list(map(int, sor))
    hivasok.append(sor)

print("3. feladat")
ido = {}

for hivas in hivasok:
    if hivas[0] not in ido.keys():
        ido[hivas[0]] = 0

for hivas in hivasok:
    ido[hivas[0]] += 1

for ora, hszam in ido.items():
    print(f"{ora} ora  {hszam} hivas")


leghossz = 0
leghosszsr = 0
sorszam = 1

for hivas in hivasok:
    hossz = mpbe( hivas[3], hivas[4], hivas[5]) - mpbe( hivas[0], hivas[1], hivas[2])
    if hossz > leghossz:
        leghossz = hossz
        leghosszsr = sorszam
    sorszam += 1

print("4. feladat")
print(f"A leghosszabb ideig vonalban levo hivo {leghosszsr}. sorban szerepel, a hivas hossza: {leghossz} masodperc.")

print("5. feladat")
idopont = input("Adja meg az idopontot! (ora, perc, masodperc): ")
idopont = list(map(int, idopont.strip().split(" ")))
mp = mpbe(idopont[0],idopont[1],idopont[2])

sorsz = 0
while sorsz < len(hivasok) and not (mp >= mpbe(hivasok[sorsz][0],hivasok[sorsz][1],hivasok[sorsz][2],) and mp < mpbe(hivasok[sorsz][3],hivasok[sorsz][4],hivasok[sorsz][5])):
    sorsz += 1


if sorsz < len(hivasok):
    aktual = sorsz + 1
else:
    aktual = 0

if not (aktual == 0):
    varakozo = -1
    for hivas in hivasok:
        if mpbe(hivas[0], hivas[1], hivas[2]) <= mp and mp < mpbe(hivas[3], hivas[4], hivas[5]) :
            varakozo += 1
    print(f"A varakozok szama: {varakozo} a beszelo a {aktual}. hivo")
else:
    print("Nincs varakozo")

print("6.feladat")

utolsoi = 0
utolsoei= 0
index = 0
muszakveg = mpbe(12,0,0)

for hivas in hivasok:
    kezd = mpbe(hivas[0], hivas[1], hivas[2])
    veg =  mpbe(hivas[3], hivas[4], hivas[5])
    if kezd <= muszakveg and veg > mpbe(hivasok[utolsoi][3],hivasok[utolsoi][4],hivasok[utolsoi][5]):
        utolsoei = utolsoi
        utolsoi = index
    index += 1

utolsoeveg = mpbe(hivasok[utolsoei][3],hivasok[utolsoei][4],hivasok[utolsoei][5])
utolsokezd = mpbe(hivasok[utolsoi][0],hivasok[utolsoi][1],hivasok[utolsoi][2])
varas = utolsoeveg - utolsokezd
if varas < 0 :
    varas = 0 

print(f"Az utolso telefonalo adatai a {utolsoi + 1 }. sorban talalhatok, {varas} masodpercig vart")


bekapcsolt = []
elotte = 0
muszakkezdet = mpbe(8,0,0)
i = 0 
for hivas in hivasok:
    if muszakkezdet < hivas[7] and hivasok[elotte][7] < hivas[7] and hivas[6] <= muszakveg:
        bekapcsolt.append(i)
        elotte = i
    i += i

f = open("sikeres.txt", "w", encoding="utf-8")

if hivasok[bekapcsolt[0][6]] < muszakkezdet:
    kezdet = "08 00 00"
else:
    kezdet = str(hivasok[bekapcsolt[0][0]])+" "+str(hivasok[bekapcsolt[0][1]])+" "+str(hivasok[bekapcsolt[0][2]])
vege =   str(hivasok[bekapcsolt[0][3]])+" "+str(hivasok[bekapcsolt[0][4]])+" "+str(hivasok[bekapcsolt[0][5]])

f.write("%d %s %s\n" %( bekapcsolt[0], kezdet, vege))

for i in range(1, len(bekapcsolt-1)):
    if hivasok[bekapcsolt[i-1][7]] < hivasok[bekapcsolt[i][6]]:
         kezdet = str(hivasok[bekapcsolt[i][0]])+" "+str(hivasok[bekapcsolt[i][1]])+" "+str(hivasok[bekapcsolt[i][2]])
    else:
        kezdet = str(hivasok[bekapcsolt[i-1][3]])+" "+str(hivasok[bekapcsolt[i-1][4]])+" "+str(hivasok[bekapcsolt[i-1][5]])
    vege =   str(hivasok[bekapcsolt[i][3]])+" "+str(hivasok[bekapcsolt[i][4]])+" "+str(hivasok[bekapcsolt[i][5]])
    f.write("%d %s %s\n" %( bekapcsolt[1], kezdet, vege))
