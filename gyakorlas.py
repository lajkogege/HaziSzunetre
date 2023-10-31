#1.	Kérj be egy [200, 920] intervallumban lévő egész számot (ha nem ebben az intervallumban van, jelezz hibát!), majd írasd ki az első számjegyét!
import math


def elso():
    print("1.feldat")
    szam:int=int(input("Kérek egy számot 200 és 900 közötti intervalumban: "))
    if 200 < szam <900:
        elso_szamjegy = int(str(szam)[0])
        print(f"A {szam} szám első számjegye: {elso_szamjegy}")
    else:
        print(f"A megadott szám: {szam} nincs a [200, 900] intervallumban")

#2.	Írj metódust, mely a paraméterében kapott számról megmondja, hogy hány 1-es, 10-es, 100 - as, 1000 - es, stb van benne! használd hozzá az egész osztás operátorát - // !
#pl: 123//10 =12  123%10=3
def masodik():
    szam:int=126610015
    egyes: int = 2
    tizes: int = 0
    szazsas: int = 0
    ezres: int = 0
    while szam > 0:
        maradek:int=szam %10
        if maradek == 1:
            egyes +=1
        elif maradek== 10:
            tizes+=10
        elif maradek== 100:
            szazsas+=100
        elif maradek== 1000:
            ezres +=1000
        szam //= 10
    print(f"Egyesek: {egyes}")
    print(f"Tízesek: {tizes}")
    print(f"Százasok: {szazsas}")
    print(f"Ezresek: {ezres}")

#3.	+++ Írj eljárást, mely paraméterében kap egy számot, majd összeadja a számjegyeket és kiírja a számjegyek összegét a képernyőre.
#PL. 324 -> „324 számjegyeinek összege: 9”
def harmadik():
    szam:int=66
    osszeg:int=0
    while szam >0 :
        szamjegy= szam %10
        osszeg += szamjegy
        szam //= 10
    print(osszeg)

#4.	Egy hétfői napon az 1-es csoportnak 9 órája van. Az első órában a teljesítményük 90%-át képesek nyújtani. A 2-3. órában már kissé éhesek, és csupán 60%-os a munkabírásuk. A 4-7. órában szerencsére programozást tanulnak, így némiképp javul a hatékonyságuk (70%), a 8-9. órában azonban már újra lecsökken (50%).
#Írj metódust, mely paraméterében kap egy egész számot 1 és 9 között (melyik órán vannak; jelezz hibát, ha nem ebben az intervallumban lévő számot kapsz, pl. “Ez már tényleg túlzás.”). Példa egy esetre: Be: 3, Ki: “Még bírjuk (60%).”    -  nem kell tesztfüggvényeket írni, de az alábbi táblázat alapján ellenőrizzétek a munkátokat!
def negyedik():
    ora_szam_be:int=int(input("Adj meg 1 és 9 között egy óraszámot: "))
    if ora_szam_be == 0:
        print("Be se jövök")
    elif 1 <= ora_szam_be <= 9:
        if ora_szam_be == 1:
            print("Még 90% on vagyunk!")
        elif ora_szam_be == 2 or ora_szam_be == 3:
            print("Még bírjuk (60%)!")
        elif 4 <= ora_szam_be <= 7:
            print("Progit tanulunk, töltödünk! 70%")
        elif ora_szam_be == 8 or ora_szam_be == 9:
            print("Lassan nem bírjuk tovább! 50%")
    else:
        print("Ez már tényleg túlzás!")

#5.	Az egyik diák (legyen Márti a neve) az alábbi algoritmus alapján tevékenykedik az órákon:
def otodik():
    be_nap:str=str(input("Kérem a napot: "))
    be_ora:str=str(input("Kérem az órát:"))
    if be_nap== "hétfő":
        print(f"{be_nap} {be_ora} alszik")
    elif be_nap=="kedd" and be_ora=="hittan":
        print(f"{be_nap} {be_ora} figyel")
    elif be_nap=="kedd":
        print(f"{be_nap} {be_ora} alszik")
    elif be_nap== "szerda" and be_ora=="programozás":
        print(f"{be_nap} {be_ora} dolgozik")
    elif be_nap=="szerda":
        print(f"{be_nap} {be_ora} nincs info")
    elif be_nap== "csütörtök" :
        print(f"{be_nap} {be_ora} figyel")
    elif be_nap=="péntek":
        print(f"{be_nap} {be_ora} félig jelen van")

#6.	A program számítsa ki egy beolvasott valós szám négyzetgyökét! A program adjon hibaüzenetet, ha a felhasználó negatív számból akar gyököt vonni!
def hatodik():
    szam_be:int=int(input("Kérek egy számot: "))
    if szam_be > 0:
        print(math.sqrt(szam_be))
    else:
        print("Negatív számmal nem tudsz gyököt vonni!!!")

#7.	A program olvasson be a konzolról két valós számot! Ha mindkét szám pozitív, akkor legyenek a beolvasott számok egy téglalap oldalai. A program számítsa ki a téglalap kerületét, területét, és írja ki két tizedesre kerekítve az eredményeket a konzolra! Hiba esetén írja ki: "Hiba: a téglalap oldalai nem pozitívak!"!
def hetedik():
    a:int=int(input("Kérek egy számot:"))
    b:int=int(input("Kérek még egy számot: "))
    kerulet:int=0
    terulet:int=0
    if a > 0 and b > 0:
        kerulet= 2*(a+b)
        terulet= a*b
    else:
        print("Hiba: a téglalap oldalai nem pozitívak!")
    print(f"A téglalap kerülete: {kerulet} és területe: {terulet}")

#1.feladat:	Egy a természettel  Vadászati és Természeti Világkiállításon téged bíztak meg, hogy egy kihelyezett információs tábla részműködését leprogramozd!
def vadaszat():
    szektor:str=str(input("Kérem adja meg a szektor nevét: "))
    if szektor == "A" or "a":
        print(f"{szektor}:Nemzetközi Csarnok, World Conservation Forum 2021 ")
    elif szektor=="B" or "b" or "E" or "e":
        print(f"{szektor}:Kereskedelmi Csarnok  ")
    elif szektor=="C" or "c":
        print(f"{szektor}:Konferencia-központ Innovációs Showroom ")
    elif szektor=="D" or "d":
        print(f"{szektor}:Hagyományos Vadászati Módok Csarnoka")
    elif szektor== "G" or "g":
        print(f"{szektor}:Hazai és nemzetközi Trófeakiállítás, 12. Nyílt Európai Taxiderma-bajnokság, Vadászat 21.században kiállítás ")
    elif szektor=="H" or "h":
        print(f"{szektor}:Központi Magyar Kiállítás ")
    else:
        print("HIBA: Adjon meg egy betűt A-H-ig!")

#8.	Írj programot, ami kiírja a 10x10-es alapú szorzótáblát! 10-esével egymás alá! használj hozzá formázott kiiratást!
def nyolcadik():
    i = 1
    while i <= 10:
        j = 1
        while j <= 100:
            eredmeny = i * j
            print(f"{i:2d} x {j:2d} = {eredmeny:3d}", end="   ")
            j += 1
        print()
        i += 10

#9.	Írj metódust, mely neveket kér a felhasználótól addig amíg a „@” jelet nem kapja.
#Hány nevet adott meg a felhasználó?
#Van-e benne A betűvel kezdődő név?
#Melyik a leghosszabb név?

def kilencedik():
    szam = 0
    tartalmaz_A = False
    leghosszabb = ""

    while True:
        nev = input("Kérek nevet (vagy írj be '@' karaktert a befejezéshez): ")
        if nev == "@":
            break
        szam += 1
        if "A" in nev:
            tartalmaz_A = True
        if len(nev) > len(leghosszabb):
            leghosszabb = nev

    print("Vége.")
    print(f"Ennyi nevet adtál meg: {szam}")

    if tartalmaz_A:
        print("Legalább egy név tartalmaz 'A' betűt.")
    else:
        print("A nevek között nincs 'A' betű.")

    if leghosszabb:
        print(f"A leghosszabb név: {leghosszabb}")
    else:
        print("Nem adtál meg neveket.")
