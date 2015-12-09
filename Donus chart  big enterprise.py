'''Plot DONUT CHART : Big enterprise Electricity 2557-2558'''
#Please download Plotly for Python
import plotly.plotly as py
import plotly.graph_objs as go
py.sign_in('VoradeeSantivarotai', 'xnznsvj4k1')
fig = {
  "data": [
    {
      "values": [6.609681240577212, 7.213008830497522, 8.365954124488475,\
                 8.809632780529828, 9.588358819728622, 9.189774930002153,\
                 8.683905879819081, 8.659810467370233, 8.528968339435709,\
                 8.328801421494722, 8.441740254146026, 7.5803629119104015],
      "labels": ["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC",],
      "domain": {"x": [0, .48]},
      "name": "Big enterprise(2557)",
      "hoverinfo":"label+percent+name",
      "hole": .4,
      "type": "pie"
    },     
    {
      "values": [8.114385071568291, 8.851647157450243, 9.925947775328344,\
                 10.015990312664949, 11.073679634861987, 10.912068804918187,\
                 10.541962927313937, 10.446952525848417, 10.22976371596237,\
                 9.887602074083274],
      "labels": [
        "JAN",
        "FEB",
        "MAR",
        "APR",
        "MAY",
        "JUN",
        "JUL",
        "AUG",
        "SEP",
        "OCT",
      ],
      "text":"Big enterprise(2558)",
      "textposition":"inside",
      "domain": {"x": [.52, 1]},
      "name": "Big enterprise(2558)",
      "hoverinfo":"label+percent+name",
      "hole": .4,
      "type": "pie"
    },     
  ],
  "layout": {
        "title":"Big enterprise Electricity 2557-2558",
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

url = py.plot(fig, filename='Big enterprise Electricity 2557-2558')

def data_bigenterprise():
    ##data of big enterprise 2557
    lis2557 = [1337.23, 1323.12, 1533.09, 1553.09, 1551.17, 1516.10,\
               1513.70, 1510.29, 1505.16, 1511.56, 1471.36, 1376.17]
    percent2557 = []
    total2557 = sum(lis2557)
    for i in lis2557:
        percent2557.append((i/total2557)*100)
    #print(percent2557)

    ##data of big enterprise 2558
    lis2558 = [1368.14, 1351.87, 1538.35, 1382.69, 1551.41, 1519.24,\
               1528.01, 1491.74, 1504.40, 1524.45]
    percent2558 = []
    total2558 = sum(lis2558)
    for i in lis2558:
        percent2558.append((i/total2558)*100)
    #print(percent2558)
data_bigenterprise()
