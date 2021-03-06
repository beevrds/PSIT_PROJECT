"""the data processing project PSIT 2015
Electric sale in year 2557and year 2558 by
57070006 Kijtana Chayangsu
57070015 Jakkraphatara Kaewthong
57070101 Voradee Santivarotai
57070121 Siamrath Supavakul
"""

from matplotlib import pyplot
from numpy import arange
from random import randrange
colors = ["crimson", "lightcoral", "lightgreen", "tomato", "mediumaquamarine",\
          "chartreuse", "lightpink", "chocolate", "yellowgreen", "mediumorchid",\
          "peru", "lime", "olive", "mistyrose", "slategrat"]

def autolabel(rects):
    """set label for campare graph"""
    # attach some text labels
    for rect in rects:
        height = rect.get_height()

def compare_bar(data, num_month, year):
    """show graph of compare data upto 11 month in the same year"""
    num_month = int(num_month)
    save_data = [0]*num_month#all value
    this_data = dict()
    text_month = ""#title of graph
    ##set title graph
    if year == 2558:
        temp_str = "Enter the month(JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT)"
    else:
        temp_str = "Enter the month(JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC)"
        
    for i in range(num_month):
        choose_month = input(temp_str).upper()
        if choose_month == "DEC":
            temp_str = temp_str.replace(choose_month, "")
        if choose_month == "OCT":
            temp_str = temp_str.replace(choose_month, "")
        temp_str = temp_str.replace(choose_month+", ", "")
        if i+1 == num_month:
            text_month += choose_month +" "
        else:
            text_month += choose_month +", "
        this_data[choose_month] = data[choose_month]
        
    temp_ind = 0
    for i in this_data:
        save_data[temp_ind] = list(this_data[i].values())
        temp_ind += 1
    width = 0.75/num_month
    ind = arange(len(save_data[0]))
    fig, ax = pyplot.subplots()
    ax.set_ylabel("MEA's Energy Sales (Million Unit)")
    ax.set_title("Compare month "+ text_month)
    ax.set_xticks(ind + width)
    ax.set_xticklabels(tuple(data[choose_month].keys()))
    val_for_plot = [0]*num_month
    used_col= list()
    for i in range(num_month):
        col_ind = randrange(0, len(colors))
        while col_ind in used_col:
            col_ind = randrange(0, len(colors))
        used_col.append(col_ind)
        
        val_for_plot[i] = ax.bar(ind, save_data[i], width, color=colors[col_ind])
        ax.bar(ind, save_data[i], width, color=colors[col_ind])
        ind = ind+width
        
    ax.legend(val_for_plot, tuple(this_data.keys()))
    pyplot.show()

def bar_graph(data, value, month, years):
    """create the bar graph form data"""
    bar_width = len(data)*0.5
    pos = arange(len(data))*10
    pyplot.xticks(pos+13, data)
    pyplot.bar(pos+len(data), value, bar_width, color=colors[:10])
    pyplot.title("Electric Sale in   "+ str(month)+" "+str(years)+"\n")
    pyplot.ylabel("MEA's Energy Sales (Million Unit)")
    pyplot.show()

def pie_chart(data, value, month, years):
    """create the pie chart from value"""
    value = tuple(value)
    pyplot.pie(value, labels=data, colors=colors, autopct="%1.1f%%", shadow = True)
    pyplot.title("Electric Sale in   "+ str(month)+" "+str(years)+"\n\n")
    pyplot.axis("equal")
    pyplot.show()

def choose_month(data, see_year):
    """show the data in one month"""
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
    """main of this program read data from txt file and use data for plot graph"""
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
    #read file text and save to dict
    data = dict()
    month = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN","JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
    with open(choose_file) as file:
        for line in file:
            keyword = ["HOME", "SMEs", "MediumEnterprise", "BigEnterprise",\
            "SpecificEnterprise", "Government", "TempElectric",\
            "TOTAL", "PublicElectricity", "UnitPub"]
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
        compare_bar(data, number, see_year)
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
