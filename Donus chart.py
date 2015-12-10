'''
Plot DONUT CHART : place of electricity that you want to see in 2557-2558
Suggestion : Please download Plotly for Python
             and this code run on internet
'''
import plotly.plotly as py
import plotly.graph_objs as go
py.sign_in('VoradeeSantivarotai', 'xnznsvj4k1')

print("----------------------------------")
print("choose 1  :  home")
print("choose 2  :  SMEs")
print("choose 3  :  Medium Enterprise")
print("choose 4  :  Big Enterprise")
print("choose 5  :  Specific Enterprise")
print("choose 6  :  Government")
print("choose 7  :  Temporarily Electric")
print("choose 8  :  Unit Temporarily")
print("choose 9  :  Public Electricity")
print("choose 10 :  Unit Public")
print("----------------------------------")
type_place = int(input())

place2557 = []
place2558 = []

if type_place == 1:
    #data of home 2557
    lis2557 = [681.77, 787.30, 967.41, 1122.78, 1209.22, 1127.63,\
               1030.49, 1003.59, 986.90, 965.01, 971.29, 841.36]
    total2557 = sum(lis2557)
    for i in lis2557:
        place2557.append((i/total2557)*100)

    #data of home 2558
    lis2558 = [745.82, 853.60, 1017.89, 1100.93, 1216.77, 1178.44, 1091.09,\
               1091.64, 1040.53, 1000.14]
    total2558 = sum(lis2558)
    for i in lis2558:
        place2558.append((i/total2558)*100)

    name_title = "Home Electricity 2557-2558"
elif type_place == 2:
    #data of sme 2557
    lis2557 = [491.02, 535.84, 621.49, 654.45, 712.30, 682.69, 645.11,\
               643.32, 633.60, 618.73, 627.12, 563.13]
    total2557 = sum(lis2557)
    for i in lis2557:
        place2557.append((i/total2557)*100)

    #data of sme 2558
    lis2558 = [522.68, 570.17, 639.37, 645.17, 713.30, 702.89, 679.05,\
               672.93, 658.94, 636.90]
    total2558 = sum(lis2558)
    for i in lis2558:
        place2558.append((i/total2558)*100)

    name_title = "SMEs Electricity 2557-2558"
elif type_place == 3:
    #data of MediumEnterprise 2557
    lis2557 = [615.80, 639.17, 754.61, 690.34, 788.90, 767.21, 759.76,\
               746.12, 752.22, 740.31, 742.06, 672.496]
    total2557 = sum(lis2557)
    for i in lis2557:
        place2557.append((i/total2557)*100)

    #data of MediumEnterprise 2558
    lis2558 = [646.22, 673.85, 775.10, 702.60, 812.36, 784.33, 796.77,\
               759.55, 753.94, 744.68]
    total2558 = sum(lis2558)
    for i in lis2558:
        place2558.append((i/total2558)*100)

    name_title = "Medium Enterprise Electricity 2557-2558"

fig = {
  "data": [
    {
      "values": place2557,
      "labels": ["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG",\
                 "SEP","OCT","NOV","DEC",],
      "domain": {"x": [0, .48]},
      "name": "2557",
      "hoverinfo":"label+percent+name",
      "hole": .4,
      "type": "pie"
    },     
    {
      "values": place2558,
      "labels": ["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT",],
      "text":"2558",
      "textposition":"inside",
      "domain": {"x": [.52, 1]},
      "name": "2558",
      "hoverinfo":"label+percent+name",
      "hole": .4,
      "type": "pie"
    },     
  ],
  "layout": {
        "title":name_title,
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

url = py.plot(fig, filename=name_title)
