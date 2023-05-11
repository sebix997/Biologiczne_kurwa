import random
import math
n=input("podaj n: ")

pow=input("podaj ilosc powtorzen: ")
pow=int(pow)
# Losowa wartosc miedzy 45-55
x=[]
y=[]
g=[]

for i in range (0,int(n)):
    x.append(random.randrange(1, 31)) ##tworzenie tablicy z wartosciami od 1 do 31
    g.append(str(format(x[i],'b').zfill(5))) ## zamian na binarne
    y.append((x[i]/15)*(math.sin((math.pi*x[i])/8)+1)) ##wynik funkcji dla danej wartosci
###sprawdzenie tablic
print(x)
print(y)
print(g)
print("\n")
for i in range (0,pow):
    n=int(n)
    ##losowanie rodziców
    w=(random.randrange(0, n))
    r=(random.randrange(0, n))

    rodzic1=g[w]
    rodzic2=g[r]

    ### losowanie jak bedzą kżyzowanie rodzice
    dziel=random.randint(1, 4) # bit od którego będzie kżyżowane
    jak_dlugie=random.randint(1, 5-dziel) # długość ciągu bitów który będzie krzyżowany

    if(jak_dlugie+dziel<5):
        if(dziel==1):
            jak_dlugie=4
        if(dziel==2):
            jak_dlugie=3


    print("rodzic 1 : "+str(rodzic1)+" rodzic 2 : "+str(rodzic2))
    print("dziel "+str(dziel)+" jak dlugie "+str(jak_dlugie))
    #dziecko1=rodzic1[0]+rodzic1[1]+rodzic1[2]+rodzic2[3]+rodzic2[4]

    dziecko1=str(rodzic1)
    rodzic2=str(rodzic2)



    dziecko1 = dziecko1[0:dziel]                          ## tutaj tworzymy dziecko
    rodzic2 = rodzic2[dziel:dziel + jak_dlugie+1]          ## czyli rodzic1 daje gen poczatkowy
    dziecko1=dziecko1+rodzic2                             ## jest modyfikowany od wylosoaeno momentu dziel
                                                          ## od tego momentu dziecko to rodzic2
                                                            ## tak dlugo az wylosowane zmienna jak_dlugo

    dziecko1=str(dziecko1)

    g.append(dziecko1)
    e=int(dziecko1,2)
    y.append((e / 15) * (math.sin((math.pi * e) / 8)))
    x.append(e)

    print("dziecko : "+dziecko1)

    print(x)
    print(g)
    print(y)
    print("\n")
    n=n+1

maks=0
moje_i=0
for i in range (0,pow):
    if maks<y[i]:
        maks=y[i]
        moje_i=i

print("Maks to : "+str(y[moje_i])+" Prosze Pana")
print("Dla wartosci : "+str(x[moje_i])+" Prosze Pana")
print("Zero jedynkowo : "+str(g[moje_i])+" Prosze Pana")