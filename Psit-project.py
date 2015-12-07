"""the data processing project PSIT 2015"""
from matplotlib import pyplot
from numpy import arange

def bar_graph(data, value):
    """create the bar graph form data"""
    bar_width = 0.070
    pos = arange(len(data))
    pyplot.xticks(pos+0.25,data)
    pyplot.bar(pos,value, bar_width, color="lightgreen")
    pyplot.show()

def pie_chart(data, value):
    value = tuple(value)
    colors = ["grey", "gold", "lightskyblue", "lightcoral", "lightgreen"]
    pyplot.pie(value, labels=data, colors=colors, autopct="%1.1f%%", shadow = True)
    pyplot.axis("equal")
    pyplot.show()

def main():
    data = dict()
    month = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN","JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
    keyword = ["HOME", "SMEs", "MediumEnterprise", "BigEnterprise",\
            "SpecificEnterprise", "Government", "TemporarilyElectricity",\
            "UnitTem", "PublicElectricity", "UnitPub"]
    with open("Data-2557.txt") as text:
        for line in text:
            temp_dic = dict()
            sub_data = line.split(" ")
            sub_data[0] = sub_data[0].replace("ï»¿", "")
            sub_data[-1] = sub_data[-1].replace("\n", "")
            data[sub_data[0]] = sub_data[1:]
    for i in month:
        count = 0
        temp = dict()
        for j in keyword:
            temp[j] = data[i][count]
            count += 1
        data[i] = temp
    for i in month:
        print(i, data[i])
main()
