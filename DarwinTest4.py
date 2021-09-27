import random
from tkinter import *
import matplotlib.pyplot as plt

root = Tk()

def Invert(x):
    if (x == "Betrayed"):
        return("Cooperated")
    return("Betrayed")


class Pop:
    def __init__(self):
        self.cash = 0
        self.history = {}

class Podrazák(Pop):
    def __init__(self):
        super().__init__()

    def action(self, list, opakovanie, opponent):
        return("Betrayed")

class Kavka(Pop):
    def __init__(self):
        super().__init__()

    def action(self, list, opakovanie, opponent):
        return("Cooperated")

class Dobrý(Pop):
    def __init__(self):
        super().__init__()

    def action(self, list, opakovanie, opponent):
        x = random.randint(1, 4)
        if (x == 4):
            return("Betrayed")
        return("Cooperated")

class Zlý(Pop):
    def __init__(self):
        super().__init__()

    def action(self, list, opakovanie, opponent):
        x = random.randint(1, 4)
        if (x == 4):
            return("Cooperated")
        return("Betrayed")

class Amnesiac(Pop):
    def __init__(self):
        super().__init__()

    def action(self, list, opakovanie, opponent):
        if (random.randint(0, 1) == 1):
            return("Cooperated")
        else:
            return("Betrayed")

class TitForTat(Pop):
    def __init__(self):
        super().__init__()

    def action(self, list, opakovanie, opponent):
        for entity in list[opponent].history:
            if (str(self) in entity) and (entity.split()[0] == str(opakovanie - 1)) and (
                    list[opponent].history[entity] == "Betrayed"):
                return("Betrayed")
        return("Cooperated")

class Veľký_Pes(Pop):
    def __init__(self):
        super().__init__()

    def action(self, list, opakovanie, opponent):
        opponent_has_betrayed = 0
        have_betrayed = 0
        for entity in list[opponent].history:
            if (str(self) in entity) and (entity.split()[0] == str(opakovanie - 1)) and (
                    list[opponent].history[entity] == "Betrayed"):
                opponent_has_betrayed = 1
        for entity in self.history:
            if (str(list[opponent]) in entity) and (entity.split()[0] == str(opakovanie - 1)) and (
                    self.history[entity] == "Betrayed"):
                have_betrayed = 1
        if (opponent_has_betrayed == 1) and (have_betrayed == 1):
            return("Cooperated")
        elif (opponent_has_betrayed != 1) and (have_betrayed == 1):
            return("Betrayed")
        elif (opponent_has_betrayed == 1) and (have_betrayed != 1):
            return("Betrayed")
        return("Cooperated")

class Malý_Pes(Pop):
    def __init__(self):
        super().__init__()

    def action(self, list, opakovanie, opponent):
        opponent_has_betrayed = 0
        have_betrayed = 0
        if (list[opponent].history):
            for entity in list[opponent].history:
                if (str(self) in entity) and (entity.split()[0] == str(opakovanie - 1)) and (
                        list[opponent].history[entity] == "Betrayed"):
                    opponent_has_betrayed = 1
            for entity in self.history:
                if (str(list[opponent]) in entity) and (entity.split()[0] == str(opakovanie - 1)) and (
                        self.history[entity] == "Betrayed"):
                    have_betrayed = 1
            if (opponent_has_betrayed == 1) and (have_betrayed == 1):
                return("Cooperated")
            elif (opponent_has_betrayed != 1) and (have_betrayed == 1):
                return("Betrayed")
            elif (opponent_has_betrayed == 1) and (have_betrayed != 1):
                return("Betrayed")
            return("Cooperated")
        else:
            return("Betrayed")

class TitFor2Tat(Pop):
    def __init__(self):
        super().__init__()

    def action(self, list, opakovanie, opponent):
        if (list[opponent].history):
            actions_to_self = [entity for entity in list[opponent].history if str(self) in entity]
            if (len(actions_to_self) > 1):
                if (list[opponent].history[actions_to_self[-1]] == "Betrayed") and (
                        list[opponent].history[actions_to_self[-2]] == "Betrayed"):
                    return("Betrayed")
        return("Cooperated")

def Setup(e, bruh, e2, e3,sum):
    if (sum == ""):
        sum = 0
    global class_1_growth
    global class_2_growth
    class_1_growth = []
    class_2_growth = []
    PopList = [f"človek{i + 1}" for i in range(0, int(e))]
    type_list = (Amnesiac,TitFor2Tat,TitForTat,Kavka,Podrazák,Veľký_Pes,Malý_Pes,Dobrý,Zlý)

    class_1 = eval(e2)
    for i in range(0, int(len(PopList) / 2)):
        PopList[i] = class_1()

    class_2 = eval(e3)
    for i in range(int(len(PopList) / 2), len(PopList)):
        PopList[i] = class_2()
    class_1_growth.append(len(PopList)/2)
    class_2_growth.append(len(PopList)/2)
    TurnCycle(PopList, bruh, class_1,class_2,sum)


def TurnCycle(PopList, bruh, class_1,class_2,sum):
    for opakovanie in range(0, int(bruh)):
        i = 0
        for cycle in range(len(PopList) - 1):
            temp = 0
            while (temp != len(PopList) - 1 - cycle):
                x = random.randint(1,100)
                if (x <= int(sum)):
                    value_1 = Invert(PopList[i].action(PopList, opakovanie, temp + 1 + i))
                else:
                    value_1 = PopList[i].action(PopList, opakovanie, temp + 1 + i)
                x = random.randint(1,100)
                if (x <= int(sum)):
                    value_2 = Invert(PopList[temp + 1 + i].action(PopList, opakovanie, i))
                else:
                    value_2 = PopList[temp + 1 + i].action(PopList, opakovanie, i)
                if (value_1 == "Betrayed") and (value_2 == "Betrayed"):
                    PopList[i].cash += 1
                    PopList[i].history[f"{opakovanie} {PopList[temp + 1 + i]}"] = "Betrayed"
                    PopList[temp + 1 + i].cash += 1
                    PopList[temp + 1 + i].history[f"{opakovanie} {PopList[i]}"] = "Betrayed"

                elif ((value_1 == "Betrayed")) and (value_2 == "Cooperated"):
                    PopList[temp + 1 + i].history[f"{opakovanie} {PopList[i]}"] = "Cooperated"
                    PopList[i].cash += 7
                    PopList[i].history[f"{opakovanie} {PopList[temp + 1 + i]}"] = "Betrayed"

                elif (value_1 == "Cooperated") and (value_2 == "Betrayed"):
                    PopList[temp + 1 + i].cash += 7
                    PopList[temp + 1 + i].history[f"{opakovanie} {PopList[i]}"] = "Betrayed"
                    PopList[i].history[f"{opakovanie} {PopList[temp + 1 + i]}"] = "Cooperated"

                elif (value_1 == "Cooperated") and (value_2 == "Cooperated"):
                    PopList[i].cash += 5
                    PopList[temp + 1 + i].cash += 5
                    PopList[i].history[f"{opakovanie} {PopList[temp + 1 + i]}"] = "Cooperated"
                    PopList[temp + 1 + i].history[f"{opakovanie} {PopList[i]}"] = "Cooperated"
                else:
                    temp -= 1
                temp += 1
            i += 1

        group_1_cash = 0
        group_2_cash = 0
        for sex in PopList:
            if isinstance(sex,class_1):
                group_1_cash += sex.cash
            else:
                group_2_cash += sex.cash

        for pop in range(0,group_1_cash):
            temp = "filler"
            PopList.insert(0,temp)
            PopList[0] = class_1()
        class_1_growth.append(group_1_cash + class_1_growth[0])

        for pop in range(0,group_2_cash):
            temp = "filler"
            PopList.insert(len(PopList),temp)
            PopList[-1] = class_2()
        class_2_growth.append(group_2_cash + class_2_growth[0])

    turns = [i for i in range(0,int(bruh)+1)]
    #print(turns)
    #print(class_1_growth)
    #print(class_2_growth)
    #print(group_1_cash)
    #print(group_2_cash)

    fig, axs = plt.subplots(1,2)
    fig.suptitle('Vývin jednotlivých tried')
    axs[0].plot(class_1_growth,turns)
    axs[1].plot(class_2_growth,turns)
    axs[0].set(xlabel = "Počet jednotiek triedy", ylabel='Počet kôl', title="Trieda " + (str(class_1)).split(".")[1].split("'")[0])
    axs[1].set(xlabel = "Počet jednotiek triedy", title="Trieda " + (str(class_2)).split(".")[1].split("'")[0])
    plt.show()

bruhma = Label(root, text="Sem zadaj počet požadovaných ľudí")
bruhma.grid(row=0, column=0)
e = Entry(root)
e.grid(row=1, column=0)
temp = Button(root, text="confirm", command=lambda: Setup(e.get(), e2.get(),e3.get(), e4.get(),sum.get()))
temp.grid(row=3, column=1)

bruhma = Label(root, text="Sem zadaj počet požadovaných kôl")
bruhma.grid(row=0, column=2)
e2 = Entry(root)
e2.grid(row=1, column=2)

bruhma = Label(root, text="Sem zadaj požadovaný šum (Nič = 0%)")
bruhma.grid(row=0, column=1)
sum = Entry(root)
sum.grid(row=1, column=1)

bruhma = Label(root, text="Sem zadaj triedu 1")
bruhma.grid(row=2, column=0)
e3 = Entry(root)
e3.grid(row=3, column=0)

bruhma = Label(root, text="Sem zadaj triedu 2")
bruhma.grid(row=2, column=2)
e4 = Entry(root)
e4.grid(row=3, column=2)

bruhma = Label(root, text="")
bruhma.grid(row=4, column=1)
bruhma = Label(root, text="Možnosti")
bruhma.grid(row=5, column=1)
bruhma = Label(root, text="Amnesiac,TitFor2Tat,TitForTat,Kavka,Podrazák,Veľký_Pes,Malý_Pes,Dobrý,Zlý")
bruhma.grid(row=6, column=1)

root.mainloop()