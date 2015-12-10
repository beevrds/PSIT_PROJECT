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
    #data of SMEs 2557
    lis2557 = [491.02, 535.84, 621.49, 654.45, 712.30, 682.69, 645.11,\
               643.32, 633.60, 618.73, 627.12, 563.13]
    total2557 = sum(lis2557)
    for i in lis2557:
        place2557.append((i/total2557)*100)

    #data of SMEs 2558
    lis2558 = [522.68, 570.17, 639.37, 645.17, 713.30, 702.89, 679.05,\
               672.93, 658.94, 636.90]
    total2558 = sum(lis2558)
    for i in lis2558:
        place2558.append((i/total2558)*100)

    name_title = "SMEs Electricity 2557-2558"
elif type_place == 3:
    #data of Medium Enterprise 2557
    lis2557 = [615.80, 639.17, 754.61, 690.34, 788.90, 767.21, 759.76,\
               746.12, 752.22, 740.31, 742.06, 672.496]
    total2557 = sum(lis2557)
    for i in lis2557:
        place2557.append((i/total2557)*100)

    #data of Medium Enterprise 2558
    lis2558 = [646.22, 673.85, 775.10, 702.60, 812.36, 784.33, 796.77,\
               759.55, 753.94, 744.68]
    total2558 = sum(lis2558)
    for i in lis2558:
        place2558.append((i/total2558)*100)

    name_title = "Medium Enterprise Electricity 2557-2558"
elif type_place == 4:
    #data of Big Enterprise 2557
    lis2557 = [1337.23, 1323.12, 1533.09, 1553.09, 1551.17, 1516.10,\
               1513.70, 1510.29, 1505.16, 1511.56, 1471.36, 1376.17]
    total2557 = sum(lis2557)
    for i in lis2557:
        place2557.append((i/total2557)*100)

    #data of Big Enterprise 2558
    lis2558 = [1368.14, 1351.87, 1538.35, 1382.69, 1551.41, 1519.24,\
               1528.01, 1491.74, 1504.40, 1524.45]
    total2558 = sum(lis2558)
    for i in lis2558:
        place2558.append((i/total2558)*100)

    name_title = "Big Enterprise Electricity 2557-2558"
elif type_place == 5:
    #data of Specific Enterprise 2557
    lis2557 = [132.37, 138.51, 175.76, 179.76, 189.83, 172.77,\
               175.35, 176.04, 170.21, 171.59, 173.62, 158.86]
    total2557 = sum(lis2557)
    for i in lis2557:
        place2557.append((i/total2557)*100)

    #data of Specific Enterprise 2558
    lis2558 = [150.13, 153.14, 188.05, 180.69, 200.08, 185.03,\
               186.42, 184.63, 172.68, 173.37]
    total2558 = sum(lis2558)
    for i in lis2558:
        place2558.append((i/total2558)*100)

    name_title = "Specific Enterprise Electricity 2557-2558"
elif type_place == 6:
    #data of Government 2557
    lis2557 = [6.30, 6.69, 7.88, 8.19, 9.61, 8.74,\
               8.52, 8.47, 7.99, 8.16, 8.21, 7.37]
    total2557 = sum(lis2557)
    for i in lis2557:
        place2557.append((i/total2557)*100)

    #data of Government 2558
    lis2558 = [6.79, 7.25, 5.68, 11.79, 10.07, 9.42,\
               9.94, 9.52, 9.42, 9.47]
    total2558 = sum(lis2558)
    for i in lis2558:
        place2558.append((i/total2558)*100)

    name_title = "Government Electricity 2557-2558"
elif type_place == 7:
    #data of Temporarily Electric 2557
    lis2557 = [29.24, 30.31, 34.02, 32.55, 37.21, 35.77,\
               35.87, 37.43, 36.48, 36.64, 35.84, 32.86]
    total2557 = sum(lis2557)
    for i in lis2557:
        place2557.append((i/total2557)*100)

    #data of Temporarily Electric 2558
    lis2558 = [29.71, 31.07, 34.69, 32.94, 36.62, 36.31,\
               35.34, 36.23, 34.45, 36.81]
    total2558 = sum(lis2558)
    for i in lis2558:
        place2558.append((i/total2558)*100)

    name_title = "Temporarily Electricity 2557-2558"
elif type_place == 8:
    #data of Unit Temporarily 2557
    lis2557 = [3293.73, 3460.94, 4094.26, 4078.03, 4498.23, 4310.91,\
               4168.80, 4125.26, 4092.56, 4052.00, 4029.50, 3652.20]
    total2557 = sum(lis2557)
    for i in lis2557:
        place2557.append((i/total2557)*100)

    #data of Unit Temporarily 2558
    lis2558 = [3469.49, 3641.22, 4199.13, 4056.81, 4540.61, 4415.66,\
               4326.62, 4246.24, 4174.36, 4125.82]
    total2558 = sum(lis2558)
    for i in lis2558:
        place2558.append((i/total2558)*100)

    name_title = "Unit Temporarily Electricity 2557-2558"
elif type_place == 9:
    #data of Public Electricity 2557
    lis2557 = [33.68, 30.89, 34.22, 33.19, 34.31, 33.69,\
               34.97, 35.03, 34.17, 35.49, 34.47, 35.70]
    total2557 = sum(lis2557)
    for i in lis2557:
        place2557.append((i/total2557)*100)

    #data of Public Electricity 2558
    lis2558 = [30.20, 27.53, 48.52, 36.57, 36.88, 35.80,\
               37.11, 37.29, 36.19, 36.85]
    total2558 = sum(lis2558)
    for i in lis2558:
        place2558.append((i/total2558)*100)

    name_title = "Public Electricity 2557-2558"
elif type_place == 10:
    #data of Unit Public 2557
    lis2557 = [3327.41, 3491.83, 4128.48, 4111.22, 4532.54, 4344.60,\
               4203.77, 4160.29, 4126.73, 4087.49, 4063.97, 3687.90]
    total2557 = sum(lis2557)
    for i in lis2557:
        place2557.append((i/total2557)*100)

    #data of Unit Public 2558
    lis2558 = [3499.69, 3668.75, 4247.62, 4092.48, 4577.49, 4451.46,\
               4363.73, 4283.53, 4210.55, 4162.67]
    total2558 = sum(lis2558)
    for i in lis2558:
        place2558.append((i/total2558)*100)

    name_title = "Unit Public Electricity 2557-2558"

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
