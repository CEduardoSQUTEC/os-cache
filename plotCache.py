import csv
import matplotlib.pyplot as plt

x = []
cache = []
TLB = []
Page = []
with open('cacheData.csv') as File:
	reader = csv.reader(File, delimiter=';', quotechar=';', quoting=csv.QUOTE_MINIMAL)
	i = 0
	for row in reader:
		if (i == 0):
			i += 1
			continue
		if (300 < i): 
			break
		if ((i - 1) % 3 == 0): 
			cache.append(int(row[1]))
		elif ((i - 2) % 3 == 0):
			TLB.append(int(row[1]))
		elif ((i - 3) % 3 == 0): 
			Page.append(int(row[1]))
			x.append(int(float(row[0])))
		i += 1
print(x)
print(cache)
print(TLB)
print(Page)

plt.plot(x, cache, x, TLB, x, Page)
plt.show()
