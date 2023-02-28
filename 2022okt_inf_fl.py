import math
import time

# TASK : https://dload-oktatas.educatio.hu/erettsegi/feladatok_2022osz_emelt/e_inf_22okt_fl.pdf
# RESULT: https://dload-oktatas.educatio.hu/erettsegi/feladatok_2022osz_emelt/e_inf_22okt_ut.pdf

#region 1
file: str = open("jel.txt", "r", encoding="utf-8")
#check file reading
#print(file.read())
#------------------
lines: str = file.readlines()

#check file reading (other way)
#for line in lines:
#    print(line, end="\n")
#------------------------------
file.close()
#endregion 1

#region 2
print("2.feladat")
numberFromUser: int = int(input("Kerem a sor szamat: "))
dataFromList: list = list(lines[numberFromUser - 1].split(" "))

print(f"x={dataFromList[-2]}, y={dataFromList[-1]}")
#endregion

#region 3
def eltelt(hour1: int, minute1: int, milsec1: int, hour2: int, minute2: int, milsec2: int):
    hour: int = (int(hour2) - int(hour1)) * 60 * 60
    minute: int = (int(minute2) - int(minute1)) * 60
    milisec: int = (int(milsec2) - int(milsec1))

    return (hour + minute + milisec)
#endregion

#region 4
print("4.feladat")
datas: list = list(lines)
datasLength: int = datas.__len__();

firstDataFromSource: str = list(datas[0].split(" "))
lastDataFromSource: str = list(datas[datasLength - 1].split(" "))

#check first and last datas
print(f"FIRST = {firstDataFromSource}")
print(f"LAST = {lastDataFromSource}")
#--------------------------
time: int = eltelt(
    firstDataFromSource[0],
    firstDataFromSource[1],
    firstDataFromSource[2],
    lastDataFromSource[0],
    lastDataFromSource[1],
    lastDataFromSource[2])


hour: int = math.floor(time/3600)
minute: int = math.floor((time - hour * 3600) / 60)
minsec: int = ((time - hour * 3600)) - minute * 60
print(f"Idotartam: {hour}:{minute}:{minsec}")
#endregion

#region 5
print("5.feladat")

maxx: int = 99999
maxy: int = 99999
minx: int = 0
miny: int = 0
xlist: list = []
ylist: list = []
detailList: list = []
i: int = 0
while i < datasLength:
    detailList.append(datas[i].split(" "))
    i += 1

for i in detailList:
    xlist.append(int(i[-2]))
    ylist.append(int(i[-1]))

print(f"bal also: {min(xlist), min(ylist)}, jobb felso: {max(xlist), max(ylist)}")
#endregion

#region 6
print("6. feladat")

displacement: int = 0
index: int = 0

for i,e in enumerate(detailList):
    if (index < datasLength - 1):
        under: int = math.pow((int(e[3]) - int(detailList[index + 1][3])), 2) + math.pow((int(e[4]) - int(detailList[index + 1][4])), 2)
        displacement += math.sqrt(under)
    index += 1

displacement: int = round(displacement, 3)
print(f"Elmozdulas: {displacement} egyseg")

#endregion

#region 7
file=open("kimaradt.txt","w+")
index = 0
diff: int = 0

while index < detailList.__len__() - 1:

    tempHour1: int = detailList[index][0]
    tempMin1: int = detailList[index][1]
    tempMilSec1: int = detailList[index][2]

    tempHour2: int = detailList[index + 1][0]
    tempMin2: int = detailList[index + 1][1]
    tempMilSec2: int = detailList[index + 1][2]

    tempOne = int(tempHour1) * 3600 + int(tempMin1) * 60 + int(tempMilSec1)
    tempTwo = int(tempHour2) * 3600 + int(tempMin2) * 60 + int(tempMilSec2)

    sum = tempTwo - tempOne

    print(f" {index}. Act Time: {tempHour1}:{tempMin1}:{tempMilSec1}\nNext Time: {tempHour2}:{tempMin2}:{tempMilSec2}")

    if (sum > 300):
        file.write(f"{detailList[index][0]} {detailList[index][1]} {detailList[index][2]} idoelteresi hiba {round(sum / 300) + 1}\n")

    index += 1

file.close()

#endregion