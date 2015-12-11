"""the data processing project PSIT 2015"""
from matplotlib import pyplot
from numpy import arange

colors = ["crimson", "lightcoral", "lightgreen", "tomato", "mediumaquamarine",\
          "chartreuse", "lightpink", "chocolate", "yellowgreen", "mediumorchid"]

def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()

def compare_bar(data, num_month):
    num_month = int(num_month)
    save_data = [0]*num_month#all value
    this_data = dict()
    text_month = ""#title of graph
    
    ##set title graph
    for i in range(num_month):
        choose_month = input("Enter month: ").upper()
        if i+1 == num_month:
            text_month += choose_month +" "
        else:
            text_month += choose_month +", "
        this_data[choose_month] = data[choose_month]
        
##    print(this_data)
    temp_ind = 0
    for i in this_data:
        save_data[temp_ind] = list(this_data[i].values())
        temp_ind += 1
    print("save", save_data)
    print("this", this_data)
    width = 0.35
    ind = arange(len(save_data[0]))
    fig, ax = pyplot.subplots()
    ax.set_ylabel("Usage")
    ax.set_title("Compare month "+ text_month)
    ax.set_xticks(ind + width)
    ax.set_xticklabels(tuple(data[choose_month].keys()))
    
    #for i in range(num_month):
    rect1 = ax.bar(ind, save_data[0], width, color=colors[0])
    rect2 = ax.bar(ind+width, save_data[1], width, color=colors[1])
    rect3 = ax.bar(ind+width, save_data[0], width, color=colors[2])
    rect4 = ax.bar(ind+width, save_data[0], width, color=colors[3])
    rect5 = ax.bar(ind+width, save_data[0], width, color=colors[4])
    rect6 = ax.bar(ind+width, save_data[0], width, color=colors[5])
    rect7 = ax.bar(ind+width, save_data[0], width, color=colors[6])
    rect8 = ax.bar(ind+width, save_data[0], width, color=colors[7])
    rect9 = ax.bar(ind+width, save_data[0], width, color=colors[8])
    rect10 = ax.bar(ind+width, save_data[0], width, color=colors[9])
    ax.legend((rect1[0], rect2[0], rect3[0], rect4[0], rect5[0], rect6[0], rect7[0], rect8[0], rect9[0], rect10[0]),tuple(data[choose_month].keys()))
    autolabel(rect1)
    autolabel(rect2)
    autolabel(rect3)
    autolabel(rect4)
    autolabel(rect5)
    autolabel(rect6)
    autolabel(rect7)
    autolabel(rect8)
    autolabel(rect9)
    autolabel(rect10)
    pyplot.show()

def bar_graph(data, value, month, years):
    """create the bar graph form data"""
    bar_width = len(data)*0.5
    pos = arange(len(data))*10
    pyplot.xticks(pos+13, data)
    pyplot.bar(pos+len(data), value, bar_width, color=colors)
    pyplot.title("Electric usage in   "+ str(month)+" "+str(years)+"\n")
    pyplot.ylabel("Usage (Million Unit)")
    pyplot.show()

def pie_chart(data, value, month, years):
    """create the pie chart from value"""
    value = tuple(value)
    pyplot.pie(value, labels=data, colors=colors, autopct="%1.1f%%", shadow = True)
    pyplot.title("Electric usage in   "+ str(month)+" "+str(years)+"\n\n")
    pyplot.axis("equal")
    pyplot.show()

def choose_month(data, see_year):
    ## show graph do you want with input
    if see_year == 2558:
        inp_month = input("Enter the month(JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT): ").upper()
    else:
        inp_month = input("Enter the month(JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC): ").upper()
    show_graph = input("What graph do you want to see pie chart(PIE) or bargraph(BAR): ").upper()
    if show_graph == "BAR":
        bar_graph(data[inp_month].keys(), data[inp_month].values(), inp_month, see_year-543)
    else:
        pie_chart(sorted(data[inp_month].keys(), key = len), data[inp_month].values(), inp_month, see_year-543)
    
def main():
    #choose file text that you want to see it between 2557 and 2558
    #see_year = int(input("Enter the years: "))
    choose_file = "Data-2557.txt"
    while True:
        see_year = int(input("Enter the year 2557 or year 2558: "))
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
    ##save data in dic
    for i in month[:end]:
        count = 0
        temp = dict()
        for j in keyword:
            temp[j] = data[i][count]
            count += 1
        data[i] = temp
    ## check compare or show
    temp = input("Compare(C) data or show data(S)").upper()
    if temp == "C":
        number = input("Enter number of month: ")
        compare_bar(data, number)
    else:
        ##check that show graph in month or years
        month_year_chk = input("Show graph in month type M or show in years type Y: ").upper()
        if month_year_chk == "M":
            choose_month(data, see_year)
        elif month_year_chk == "Y":
            ## show all graph in the years
            show_graph = input("What graph do you want to see pie chart(PIE) or bargraph(BAR): ").upper()
            if show_graph == "BAR":
                for i in month[:end]:
                    bar_graph(data[i].keys(), data[i].values(), i, see_year-543)
            else:
                for i in month[:end]:
                    pie_chart(sorted(data[i].keys()), data[i].values(), i, see_year-543)

main()
