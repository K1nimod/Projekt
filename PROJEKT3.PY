def mpbe(o ,p , mp):
    return mp + p*60 + o*60*60

f = open("hivas.txt", "rt", encoding="utf-8") 

hivasok = []

for sor in f:
    sor = sor.strip().split(" ")
    hivasok.append(sor)