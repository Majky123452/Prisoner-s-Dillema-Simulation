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

class Traitor(Pop):
    def __init__(self):
        super().__init__()

    def action(self, list, repeat, opponent):
        return("Betrayed")

class Saint(Pop):
    def __init__(self):
        super().__init__()

    def action(self, list, repeat, opponent):
        return("Cooperated")

class Good(Pop):
    def __init__(self):
        super().__init__()

    def action(self, list, repeat, opponent):
        x = random.randint(1, 4)
        if (x == 4):
            return("Betrayed")
        return("Cooperated")

class Bad(Pop):
    def __init__(self):
        super().__init__()

    def action(self, list, repeat, opponent):
        x = random.randint(1, 4)
        if (x == 4):
            return("Cooperated")
        return("Betrayed")

class Amnesiac(Pop):
    def __init__(self):
        super().__init__()

    def action(self, list, repeat, opponent):
        if (random.randint(0, 1) == 1):
            return("Cooperated")
        else:
            return("Betrayed")

class TFT(Pop):
    def __init__(self):
        super().__init__()

    def action(self, list, repeat, opponent):
        for entity in list[opponent].history:
            if (str(self) in entity) and (entity.split()[0] == str(repeat - 1)) and (
                    list[opponent].history[entity] == "Betrayed"):
                return("Betrayed")
        return("Cooperated")

class Big_Dog(Pop):
    def __init__(self):
        super().__init__()

    def action(self, list, repeat, opponent):
        opponent_has_betrayed = 0
        have_betrayed = 0
        for entity in list[opponent].history:
            if (str(self) in entity) and (entity.split()[0] == str(repeat - 1)) and (
                    list[opponent].history[entity] == "Betrayed"):
                opponent_has_betrayed = 1
        for entity in self.history:
            if (str(list[opponent]) in entity) and (entity.split()[0] == str(repeat - 1)) and (
                    self.history[entity] == "Betrayed"):
                have_betrayed = 1
        if (opponent_has_betrayed == 1) and (have_betrayed == 1):
            return("Cooperated")
        elif (opponent_has_betrayed != 1) and (have_betrayed == 1):
            return("Betrayed")
        elif (opponent_has_betrayed == 1) and (have_betrayed != 1):
            return("Betrayed")
        return("Cooperated")

class Small_Dog(Pop):
    def __init__(self):
        super().__init__()

    def action(self, list, repeat, opponent):
        opponent_has_betrayed = 0
        have_betrayed = 0
        if (list[opponent].history):
            for entity in list[opponent].history:
                if (str(self) in entity) and (entity.split()[0] == str(repeat - 1)) and (
                        list[opponent].history[entity] == "Betrayed"):
                    opponent_has_betrayed = 1
            for entity in self.history:
                if (str(list[opponent]) in entity) and (entity.split()[0] == str(repeat - 1)) and (
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

class TF2T(Pop):
    def __init__(self):
        super().__init__()

    def action(self, list, repeat, opponent):
        if (list[opponent].history):
            actions_to_self = [entity for entity in list[opponent].history if str(self) in entity]
            if (len(actions_to_self) > 1):
                if (list[opponent].history[actions_to_self[-1]] == "Betrayed") and (
                        list[opponent].history[actions_to_self[-2]] == "Betrayed"):
                    return("Betrayed")
        return("Cooperated")


def Setup(e, tunr_temp, turns, class1_temp,mishap):
    if (mishap == ""):
        mishap = 0
    global class_1_growth
    global class_2_growth
    class_1_growth = []
    class_2_growth = []
    PopList = [f"človek{i + 1}" for i in range(0, int(e))]

    class_1 = eval(turns)
    for i in range(0, int(len(PopList) / 2)):
        PopList[i] = class_1()

    class_2 = eval(class1_temp)
    for i in range(int(len(PopList) / 2), len(PopList)):
        PopList[i] = class_2()
    class_1_growth.append(len(PopList)/2)
    class_2_growth.append(len(PopList)/2)
    TurnCycle(PopList, tunr_temp, class_1,class_2,mishap)

def TurnCycle(PopList, tunr_temp, class_1,class_2,mishap):
    for repeat in range(0, int(tunr_temp)):
        i = 0
        for cycle in range(len(PopList) - 1):
            temp = 0
            while (temp != len(PopList) - 1 - cycle):
                x = random.randint(1,100)
                if (x <= int(mishap)):
                    value_1 = Invert(PopList[i].action(PopList, repeat, temp + 1 + i))
                else:
                    value_1 = PopList[i].action(PopList, repeat, temp + 1 + i)
                x = random.randint(1,100)
                if (x <= int(mishap)):
                    value_2 = Invert(PopList[temp + 1 + i].action(PopList, repeat, i))
                else:
                    value_2 = PopList[temp + 1 + i].action(PopList, repeat, i)
                if (value_1 == "Betrayed") and (value_2 == "Betrayed"):
                    PopList[i].cash += 0
                    PopList[i].history[f"{repeat} {PopList[temp + 1 + i]}"] = "Betrayed"
                    PopList[temp + 1 + i].cash += 1
                    PopList[temp + 1 + i].history[f"{repeat} {PopList[i]}"] = "Betrayed"

                elif ((value_1 == "Betrayed")) and (value_2 == "Cooperated"):
                    PopList[temp + 1 + i].history[f"{repeat} {PopList[i]}"] = "Cooperated"
                    PopList[i].cash += 2
                    PopList[i].history[f"{repeat} {PopList[temp + 1 + i]}"] = "Betrayed"

                elif (value_1 == "Cooperated") and (value_2 == "Betrayed"):
                    PopList[temp + 1 + i].cash += 3
                    PopList[temp + 1 + i].history[f"{repeat} {PopList[i]}"] = "Betrayed"
                    PopList[i].history[f"{repeat} {PopList[temp + 1 + i]}"] = "Cooperated"

                elif (value_1 == "Cooperated") and (value_2 == "Cooperated"):
                    PopList[i].cash += 1
                    PopList[temp + 1 + i].cash += 1
                    PopList[i].history[f"{repeat} {PopList[temp + 1 + i]}"] = "Cooperated"
                    PopList[temp + 1 + i].history[f"{repeat} {PopList[i]}"] = "Cooperated"
                else:
                    temp -= 1
                temp += 1
            i += 1

        group_1_cash = 0
        group_2_cash = 0

        if (str(class_1) == str(class_2)):
            filler = 0
            for temp in PopList:
                filler += temp.cash
            group_1_cash = int(filler / 2)
            group_2_cash = int(filler / 2)
        else:
            for temp_var in PopList:
                if isinstance(temp_var,class_1):
                    group_1_cash += temp_var.cash
                else:
                    group_2_cash += temp_var.cash
        print(group_1_cash)
        print(group_2_cash)
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

    turns = [i for i in range(0,int(tunr_temp)+1)]

    fig, axs = plt.subplots(1,2)
    fig.suptitle('Evolution of classes')
    axs[0].plot(class_1_growth,turns)
    axs[1].plot(class_2_growth,turns)
    axs[0].set(xlabel = "Number of units", ylabel='Number of turns', title="Class " + (str(class_1)).split(".")[1].split("'")[0])
    axs[1].set(xlabel = "Number of units", title="Class " + (str(class_2)).split(".")[1].split("'")[0])
    plt.show()

Grid_Temp = Label(root, text="Number of units at start")
Grid_Temp.grid(row=0, column=0)
e = Entry(root)
e.grid(row=1, column=0)
temp = Button(root, text="Confirm", command=lambda: Setup(e.get(), turns.get(),class1_temp.get(), class2_temp.get(),mishap.get()))
temp.grid(row=3, column=1)

Grid_Temp = Label(root, text="Number of simulated turns")
Grid_Temp.grid(row=0, column=2)
turns = Entry(root)
turns.grid(row=1, column=2)

Grid_Temp = Label(root, text="Mishap chance (0 = None)")
Grid_Temp.grid(row=0, column=1)
mishap = Entry(root)
mishap.grid(row=1, column=1)

Grid_Temp = Label(root, text="Insert class 1 here")
Grid_Temp.grid(row=2, column=0)
class1_temp = Entry(root)
class1_temp.grid(row=3, column=0)

Grid_Temp = Label(root, text="Insert class 2 here")
Grid_Temp.grid(row=2, column=2)
class2_temp = Entry(root)
class2_temp.grid(row=3, column=2)

Grid_Temp = Label(root, text="")
Grid_Temp.grid(row=4, column=1)
Grid_Temp = Label(root, text="Available classes:")
Grid_Temp.grid(row=5, column=1)
Grid_Temp = Label(root, text="Amnesiac,TF2T,TFT,Saint,Traitor,Big_Dog,Small_Dog,Good,Bad")
Grid_Temp.grid(row=6, column=1)

root.mainloop()
