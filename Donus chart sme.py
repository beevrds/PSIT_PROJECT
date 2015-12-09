'''Plot DONUT CHART : Home Electricity 2557-2558'''
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
        "NOV",
        "DEC",
      ],
      "domain": {"x": [0, .48]},
      "name": "SME(2557)",
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
      "text":"SME(2558)",
      "textposition":"inside",
      "domain": {"x": [.52, 1]},
      "name": "SME(2558)",
      "hoverinfo":"label+percent+name",
      "hole": .4,
      "type": "pie"
    },     
  ],
  "layout": {
        "title":"SME Electricity 2557-2558",
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

url = py.plot(fig, filename='SME Electricity 2557-2558')

def data_sme():
    ##data of sme 2557
    lis2557 = [491.02, 535.84, 621.49, 654.45, 712.30, 682.69, 645.11,\
               643.32, 633.60, 618.73, 627.12, 563.13]
    percent2557 = []
    total2557 = sum(lis2557)
    for i in lis2557:
        percent2557.append((i/total2557)*100)
    print(percent2557)

    ##data of sme 2558
    lis2558 = [522.68, 570.17, 639.37, 645.17, 713.30, 702.89, 679.05,\
               672.93, 658.94, 636.90]
    percent2558 = []
    total2558 = sum(lis2558)
    for i in lis2558:
        percent2558.append((i/total2558)*100)
    print(percent2558)
data_sme()
