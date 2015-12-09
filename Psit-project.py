"""the data processing project PSIT 2015"""
from matplotlib import pyplot
from numpy import arange

colors = ["crimson", "lightcoral", "lightgreen", "tomato", "mediumaquamarine",\
          "chartreuse", "lightpink", "chocolate", "yellowgreen", "mediumorchid"]

def bar_graph(data, value, month, years):
    """create the bar graph form data"""
    bar_width = len(data)*0.5
    pos = arange(len(data))*10
    pyplot.xticks(pos+13, data)
    pyplot.bar(pos+len(data), value, bar_width, color=colors)
    pyplot.title("Electric consume in   "+ str(month)+" "+str(years)+"\n")
    pyplot.ylabel("Usage")
    pyplot.show()

def pie_chart(data, value, month, years):
    """create the pie chart from value"""
    value = tuple(value)
    pyplot.pie(value, labels=data, colors=colors, autopct="%1.1f%%", shadow = True)
    pyplot.title("Electric consume in   "+ str(month)+" "+str(years)+"\n\n")
    pyplot.axis("equal")
    pyplot.show()
    
def main():
    #choose file text that you want to see it between 2557 and 2558
    #see_year = int(input("Enter the years: "))
    choose_file = "Data-2557.txt"
    while True:
        see_year = 2558
        #see_year = int(input("Enter the year 2557 or year 2558: "))
        if see_year == 2557:
            choose_file = "Data-2557.txt"
            end = 12
            break
        elif see_year == 2558:
            choose_file = "Data-2558.txt"
            end = 10
            break
    #read file text
    data = dict()
    month = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN","JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
    with open(choose_file) as file:
        for line in file:
            keyword = ["HOME", "SMEs", "MediumEnterprise", "BigEnterprise",\
            "SpecificEnterprise", "Government", "TempElectric",\
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
    for i in month[:end]:
        count = 0
        temp = dict()
        for j in keyword:
            temp[j] = data[i][count]
            count += 1
        data[i] = temp
    for i in month[:end]:
        print(i, data[i])
        bar_graph(data[i].keys(), data[i].values(), i, see_year-543)
        pie_chart(sorted(data[i].keys(), key = len), data[i].values(), i, see_year-543)

main()
