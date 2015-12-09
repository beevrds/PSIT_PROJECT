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
