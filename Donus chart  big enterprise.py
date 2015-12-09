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
