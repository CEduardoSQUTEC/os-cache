import csv
import matplotlib.pyplot as plt

x = []
cache = []
TLB = []
Page = []
with open('../cacheData.csv') as File:
	reader = csv.reader(File, delimiter=';', quotechar=';', quoting=csv.QUOTE_MINIMAL)
	i = 0
	for row in reader:
		if (i == 0):
			i += 1
			continue
		if (900 < i): # Get the first 5 min 
			break
		if ((i - 1) % 3 == 0): 
			cache.append(int(row[1]))
		elif ((i - 2) % 3 == 0):
			TLB.append(int(row[1]))
		elif ((i - 3) % 3 == 0): 
			Page.append(int(row[1]))
			x.append(int(float(row[0])))
		i += 1

fig, (cachePlot, TLBPlot, PagePlot) = plt.subplots(3,1)
fig.suptitle('Memory misses')

cachePlot.plot(x, cache, 'r-')
cachePlot.set_ylabel('Cache misses')

TLBPlot.plot(x, TLB, 'o-')
TLBPlot.set_ylabel('TLB misses')

PagePlot.plot(x, Page, 'y-')
PagePlot.set_xlabel('Time (s)')
PagePlot.set_ylabel('Page misses')

plt.show()
