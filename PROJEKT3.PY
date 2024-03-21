def mpbe(o ,p , mp):
    return mp + p*60 + o*60*60

f = open("hivas.txt", "rt", encoding="utf-8") 

hivasok = []

for sor in f:
    sor = sor.strip().split(" ")
    hivasok.append(sor)

print("3. feladat")
ido = {}

for hivas in hivasok:
    if hivas[0] not in ido.keys():
        ido[hivas[0]] = 0

for hivas in hivasok:
    ido[hivas[0]] += 1

for ora, hszam in ido.items():
    print(ora,"óra  hivasok száma:", hszam)


