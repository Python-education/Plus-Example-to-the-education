# TASK: https://dload-oktatas.educatio.hu/erettsegi/feladatok_2022tavasz_emelt/e_inf_22maj_fl.pdf
# RESULT: https://dload-oktatas.educatio.hu/erettsegi/feladatok_2022tavasz_emelt/e_inf_22maj_ut.pdf
from typing import TextIO

# region 1
file: str = open("utca.txt", "r", encoding="utf-8")
#  print(file.read())
lines: str = file.readlines()

file.close()

#  for line in lines:
#      print(line)

# endregion

# region 2
datas: list = list(lines)
datasLength: int = datas.__len__()

datasList: list = []
index: int = 0

while index < datasLength - 1:
    datasList.append(datas[index].split(' '))
    index += 1

print(datasList)
print(f"2. feladat. A mintaban {datasLength - 1} telek szerepel")
# endregion

# region 3
adoszam: list = []

for element in datas:
    adoszam.append(element[0:5].split(" "))

print(adoszam[1])
userInput: str = input("3. feladat. Egy tulajdonos adoszama: ")
userInputIndex: int = 0
actOwnerDataIndex: int = 0
isExistInDatas: bool = False
owner: list = []

for adoszamElement in adoszam:
    #  print(f" act element: {type(str(adoszamElement))} + {str(adoszam[userInputIndex])}   --> user input: {type(userInput)} + {userInput} --> index{userInputIndex}")
    if str(adoszamElement).__contains__(userInput):
        print(f"{datasList[userInputIndex][1]} utca {datasList[userInputIndex][2]} ")
    else:
        pass
    userInputIndex += 1

# endregion

# region 4
def ado(adosav: str, alapterulet: int) -> int:

    fizetendoado: int = 0
    tempcalc: int = alapterulet * int(datasList[0][0])

    if adosav == 'A':
        if(tempcalc > 10000):
            fizetendoado = tempcalc
        else:
            print("nem kell adot fizetni")
    elif adosav == 'B':
        if (tempcalc > 10000):
            fizetendoado = tempcalc
        else:
            print("nem kell adot fizetni")
    else:
        if (tempcalc > 10000):
            fizetendoado = tempcalc
        else:
            print("nem kell adot fizetni")

    return fizetendoado

# print(ado(datasList[userInputIndex][3], int(datasList[userInputIndex][4])))

# endregion

#==================================
# HIBAS FELADAT, VAGY ROSSZ A FILE
#----------------------------------
"""
Az 'A' bersavbol egyel kevesebb
adatot szamol a program, mint a 
minta fajlban szerepel!!!!
"""
#==================================
# region 5

countA: int = 0
countB: int = 0
countC: int = 0

sumA: int = 0
sumB: int = 0
sumC: int = 0

index = 1

while index < datasLength - 1:
    if (str(datasList[index][3]).upper().__contains__('A')) and ((int(datasList[index][4]) * int(datasList[0][0])) > 10000):
        countA += 1
        sumA += int(datasList[index][4]) * 10000
    elif (str(datasList[index][3]).upper().__contains__('B')) and ((int(datasList[index][4]) * int(datasList[0][0])) > 10000):
        countB += 1
        sumB += int(datasList[index][4]) * 10000
    elif (str(datasList[index][3]).upper().__contains__('C')) and ((int(datasList[index][4]) * int(datasList[0][0])) > 10000):
        countC += 1
        sumC += int(datasList[index][4]) * 10000
    index += 1

print(f"A sávba {countA} telek esik, az adó {sumA} Ft.")
print(f"A sávba {countB} telek esik, az adó {sumB} Ft.")
print(f"A sávba {countC} telek esik, az adó {sumC} Ft.")

# endregion

# region 6
index = 1
notRepeatedElementList: list = []

while index < datasLength - 1:
    if str(datasList[index][1]) not in notRepeatedElementList:
        notRepeatedElementList.append(datasList[index][1])

    index += 1

notRepeatedElementListLength: int = notRepeatedElementList.__len__()

# print(notRepeatedElementList)

i: int = 0
j: int = 1

change: bool = False

while i < notRepeatedElementListLength - 1:
    if j < datasList.__len__() - 1:
        tempCat: str = str(datasList[j][3])
        while str(notRepeatedElementList[i]) == str(datasList[j][1]):
            if str(datasList[j][3]) == tempCat:
                pass
            else:
                change = True

            if change:
                print(notRepeatedElementList[i])
                change = False
                while str(notRepeatedElementList[i]) == str(datasList[j][1]):
                    j += 1
            else:
                j += 1
        i += 1

# endregion

# region 7

file: TextIO = open("fizetendo.txt", "w+", encoding="utf-8")

print(datasList)

for i in datasList:
    out: str = ' '
    tempCalc: int = 0
    for j in datasList:
        if str(j[0] != ' '):
            if str(i[1]) == str(j[1]):
                z = j[4]
                x = j[3]

                a = ado(j[3], j[4])
                tempCalc += ado(j[3], j[4])
                out = str(i[0] + " " + tempCalc)

    file.write(out)
    print(out)

file.close()
# endregion