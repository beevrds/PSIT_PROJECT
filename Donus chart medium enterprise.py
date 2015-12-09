'''Plot DONUT CHART : Medium Enterprise Electricity 2557-2558'''
#Please download Plotly for Python
import plotly.plotly as py
import plotly.graph_objs as go
py.sign_in('VoradeeSantivarotai', 'xnznsvj4k1')
fig = {
  "data": [
    {
      "values": [7.103475419760258, 7.373056810731024, 8.704698906309336,\
                 7.963321242736761, 9.100246441456427, 8.85004445728202,\
                 8.764106016429125, 8.606763689820598, 8.67712939306928,\
                 8.539743241316526, 8.559930123396066, 7.757484257692587],
      "labels": ["JAN","FEB","MAR","APR","MAY", "JUN", "JUL", "AUG",\
                 "SEP", "OCT", "NOV", "DEC" ],
      "domain": {"x": [0, .48]},
      "name": "Medium Enterprise(2557)",
      "hoverinfo":"label+percent+name",
      "hole": .4,
      "type": "pie"
    },     
    {
      "values": [8.67479260074637, 9.045694955298414, 10.404864821327893,\
                 9.431632077751228, 10.90503933202674, 10.528767417510137,\
                 10.69576073240798, 10.196123177705587, 10.120815099202622,\
                 9.996509786023035],
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
      "text":"Medium Enterprise(2558)",
      "textposition":"inside",
      "domain": {"x": [.52, 1]},
      "name": "Medium Enterprise(2558)",
      "hoverinfo":"label+percent+name",
      "hole": .4,
      "type": "pie"
    },     
  ],
  "layout": {
        "title":"Medium Enterprise Electricity 2557-2558",
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

url = py.plot(fig, filename='Medium Enterprise Electricity 2557-2558')


def data_MediumEnterprise():
    ##data of MediumEnterprise 2557
    lis2557 = [615.80, 639.17, 754.61, 690.34, 788.90, 767.21, 759.76,\
               746.12, 752.22, 740.31, 742.06, 672.496]
    percent2557 = []
    total2557 = sum(lis2557)
    for i in lis2557:
        percent2557.append((i/total2557)*100)
    #print(percent2557)

    ##data of MediumEnterprise 2558
    lis2558 = [646.22, 673.85, 775.10, 702.60, 812.36, 784.33, 796.77,\
               759.55, 753.94, 744.68]
    percent2558 = []
    total2558 = sum(lis2558)
    for i in lis2558:
        percent2558.append((i/total2558)*100)
    #print(percent2558)
data_MediumEnterprise()
