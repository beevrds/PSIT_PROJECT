"""the data processing project PSIT 2015"""
from matplotlib import pyplot
from numpy import arange
main_data = {"Resident":50 , "small company":300 , "medium company": 1000, "large company": 2345,"Government":200}

def bar_graph(data, value):
    """create the bar graph form data"""
    bar_width = 0.45
    pos = arange(len(data))
    pyplot.xticks(pos+0.25,data)
    pyplot.bar(pos,value, bar_width, color="lightgreen")
    pyplot.show()

def pie_chart(data, value):
    value = tuple(value)
    colors = ["grey", "gold", "lightskyblue", "lightcoral", "lightgreen"]
    pyplot.pie(value, labels=data, colors=colors,
            autopct="%1.1f%%", shadow=True, startangle=90)
    pyplot.axis("equal")
    pyplot.show()
    
#bar_graph(main_data.keys(), main_data.values())
pie_chart(main_data.keys(), main_data.values())
