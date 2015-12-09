'''Plot DONUT CHART : Home Electricity 2557-2558'''
#Please download Plotly for Python
import plotly.plotly as py
import plotly.graph_objs as go
py.sign_in('VoradeeSantivarotai', 'xnznsvj4k1')
fig = {
  "data": [
    {
      "values": [5.829709912567605, 6.732080634472733,\
                 8.272173411146026, 9.600718271019048,\
                 10.339853353000278, 9.642189871523547, 8.81156074306847,\
                 8.438829389255863, 8.251651382030397, 8.305350691549625,\
                 7.194339340302272],
      "labels": ["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG",\
                 "SEP","OCT","NOV","DEC",],
      "domain": {"x": [0, .48]},
      "name": "Home(2557)",
      "hoverinfo":"label+percent+name",
      "hole": .4,
      "type": "pie"
    },     
    {
      "values": [7.215157422232112, 8.2578348336292, 9.847197163545953,\
                 10.650536672197044, 11.771187547463684, 11.400378258366912,\
                 10.555343262212375, 10.560664032079407, 10.066219399526934,\
                 9.675481408746379],
      "labels": ["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT",],
      "text":"Home(2558)",
      "textposition":"inside",
      "domain": {"x": [.52, 1]},
      "name": "Home(2558)",
      "hoverinfo":"label+percent+name",
      "hole": .4,
      "type": "pie"
    },     
  ],
  "layout": {
        "title":"Home Electricity 2557-2558",
        "annotations": [
            {
                "font": {
                    "size": 20
                },
                "showarrow": False,
                "text": "2557",
                "x": 0.20,
                "y": 0.5
            },
            {
                "font": {
                    "size": 20
                },
                "showarrow": False,
                "text": "2558",
                "x": 0.8,
                "y": 0.5
            }
        ]
    }
}

url = py.plot(fig, filename='Home Electricity 2557-2558')

def data_home():
    ##data of home 2557
    lis2557 = [681.77, 787.30, 967.41, 1122.78, 1209.22, 1127.63,\
           1030.49, 1003.59, 986.90, 965.01, 971.29, 841.36]
    percent2557 = []
    total2557 = sum(lis2557)
    for i in lis2557:
        percent2557.append((i/total2557)*100)
    #print(percent2557)

    ##data of home 2558
    lis2558 = [745.82, 853.60, 1017.89, 1100.93, 1216.77, 1178.44, 1091.09,\
               1091.64, 1040.53, 1000.14]
    percent2558 = []
    total2558 = sum(lis2558)
    for i in lis2558:
        percent2558.append((i/total2558)*100)
    #print(percent2558)
data_home()
