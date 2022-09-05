import json
from math import sqrt
dic = {
    "A":["12", "4", "17", "5", "3", "1", "8", "13", "18", "19"],
    "B":["8", "12","3"],
    "C":["9","16","10"],
    "D":["18", "11", "16"],
    "E":["2", "1", "4"],
    "F":["4", "16", "9"],
    "G":["6", "13", "9", "15", "19"],
    "H":["5", "4", "1", "8", "13"],
    "I":["4", "12", "16", "22", "3"],
    "J":["8", "10", "22", "11"],
    "K":["17", "9", "5", "10", "8", "4", "7", "18"],
    "L":["17", "8", "7", "19", "9", "1"],
    "M":["7", "4", "21"],
    "N":["8", "21", "18"],
    "O":["2", "3", "4"],
    "P":["20", "21", "17", "5"],
    "Q":["10", "9", "12", "7"],
    "R":["4", "21", "11", "8", "15", "19", "16"]
}

with open("data.json", mode="r", encoding="utf-8") as json_file:
    data = json.load(json_file)
    print("")
    tempdict = {}
    for letter in dic:
        print(letter,":")
        if len(dic[letter]) == 0:
            print("no data found\n")
            continue
        else:
            for nums in dic[letter]:
                if data[nums]["chosen"]:
                    continue
                elif letter in data[nums]["choices"]:
                    index14, index15 = int(dic[letter].index(nums)), int(data[nums]["choices"].index(letter))
                    tempdict[data[nums]["name"]] = (65 - index14 * 6.5) + (35 - index15 * 3.5)
                    # if ((65 - index14 * 6.5) + (35 - index15 * 3.5)) >= 85.0:
                    #     data[nums]["chosen"] = True
            [print("%s %5.2f"%(key, value)) for (key, value) in sorted(tempdict.items(), key=lambda x: x[1], reverse=True)]
            tempdict.clear()
            print("\n")