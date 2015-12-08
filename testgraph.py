'''test plot graph by pull data from december'''
import pylab as pl
import numpy as np

d = {'SMEs': 563.13, 'TemporarilyElectricity': 32.86,\
     'SpecificEnterprise': 158.86, 'MediumEnterprise': 672.496,\
     'HOME': 841.36, 'BigEnterprise': 1376.17, 'Government': 7.37,\
     'PublicElectricity': 35.70, 'UnitPub': 3687.90, 'UnitTem': 3652.20}
X = np.arange(len(d))
pl.bar(X, d.values(), align='center', width=0.5)
pl.xticks(X-5, d.keys())
ymax = max(d.values()) + 1
pl.ylim(0, ymax)
pl.show()

