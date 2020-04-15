import csv
import sys
import matplotlib.pyplot as plt

years = {}
first_close = {}

with open(sys.argv[1], 'r') as f:
	reader = csv.reader(f)
	for row in reader:
		year = int(row[0][:4])
		close = float(row[5])
		if year in years:
			years[year].append((close - first_close[year]) / first_close[year] * 100)
		else:
			years[year] = [0]
                        first_close[year] = close
for year in years:
	plt.plot(years[year], label=year)
plt.legend()
plt.show()
