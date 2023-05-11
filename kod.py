import random
import math
n=input("podaj n: ")

pow=input("podaj ilosc powtorzen: ")
pow=int(pow)
# Losowa wartosc miedzy 45-55
x=[]
y=[]
g=[]


def float_bin(number, places):
    # split() separates whole number and decimal
    # part and stores it in two separate variables
    whole, dec = str(number).split(".")

    # Convert both whole number and decimal
    # part from string type to integer type
    whole = int(whole)
    dec = int(dec)

    # Convert the whole number part to it's
    # respective binary form and remove the
    # "0b" from it.
    res = bin(whole).lstrip("0b") + "."

    # Iterate the number of times, we want
    # the number of decimal places to be
    for x in range(places):
        # Multiply the decimal value by 2
        # and separate the whole number part
        # and decimal part
        whole, dec = str((decimal_converter(dec)) * 2).split(".")

        # Convert the decimal part
        # to integer again
        dec = int(dec)

        # Keep adding the integer parts
        # receive to the result variable
        res += whole

    return res


# Function converts the value passed as
# parameter to it's decimal representation
def decimal_converter(num):
    while num > 1:
        num /= 10
    return num





for i in range (0,int(n)):
    x.append(random.randrange(1, 31)+random.random()) ##tworzenie tablicy z wartosciami od 1 do 31
    g.append(float_bin(x[i],2)) ## zamian na binarne
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
    dziecko1=int(dziecko1,2)


    e=float_bin(dziecko1,2)
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