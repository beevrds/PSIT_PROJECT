"""the data processing project PSIT 2015"""
from matplotlib import pyplot
from numpy import arange
main_data = {"Resident":50 , "small company":300 , "medium company": 1000, "large company": 2345,"Government":200}

def bar_graph(data, value):
    """create the bar graph form data"""
    pos = arange(len(data))
    pyplot.xticks(pos+0.4,data)
    pyplot.bar(pos,value)
    pyplot.show()

bar_graph(main_data.keys(), main_data.values())
