"""the data processing project PSIT 2015"""
from matplotlib import pyplot
from numpy import arange

def bar_graph(data, value):
    """create the bar graph form data"""
    bar_width = 0.5
    pos = arange(len(data))
    pyplot.xticks(pos+2,data)
    pyplot.bar(pos+len(data), value, bar_width, color="lightskyblue")
    pyplot.show()

def pie_chart(data, value):
    value = tuple(value)
    colors = ["lightskyblue", "lightcoral", "lightgreen", "purple", "lightpink", "lightgrey", "cyan", "chocolate", "deeppink", "magenta"]
    pyplot.pie(value, labels=data, colors=colors, autopct="%1.1f%%", shadow = True)
    pyplot.axis("equal")
    pyplot.show()


def main():
    #choose file text that you want to see it between 2557 and 2558
    see_year = input()
    choose_file = "Data-2557.txt"
    if see_year == 2557:
        choose_file == "Data-2557.txt"
    else:
        choose_file == "Data-2558.txt"
    #read file text
    data = dict()
    month = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN","JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
    word = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    with open(choose_file) as file:
        for line in file:
            keyword = ["HOME", "SMEs", "MediumEnterprise", "BigEnterprise",\
            "SpecificEnterprise", "Government", "TemporarilyElectricity",\
            "UnitTem", "PublicElectricity", "UnitPub"]
    with open(choose_file) as text:
        for line in text:
            temp_dic = dict()
            sub_data = line.split(" ")
            sub_data[0] = sub_data[0].replace("ï»¿", "")
            sub_data[-1] = sub_data[-1].replace("\n", "")
            temp_key = sub_data[0]
            sub_data =  list(map(float, sub_data[1:]))
            data[temp_key] = sub_data[0:]
    for i in month:
        count = 0
        temp = dict()
        for j in keyword:

            temp[j] = data[i][count]
            count += 1
        data[i] = temp
    for i in month:
        bar_graph(data[i].keys(), data[i].values())
        #pie_chart(sorted(data[i].keys(), key = len), data[i].values())
        print(i, data[i])
main()
