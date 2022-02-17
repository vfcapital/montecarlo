import numpy as np
import matplotlib.pyplot as plt

plt.title("Monte-Carlo-Simulation")
plt.ylabel('[EUR]')
plt.xlabel('[Tage]')
plt.grid()

#Input
Number_of_years = 4
periods_per_year = 360
number_of_paths = 10
price_start = 100
risk_free_rate = 0
volatility = 0.15
dividend_yield = 0
path_matrix = np.empty((number_of_paths,Number_of_years*periods_per_year))

#Calculate risk-neutral probability
u = np.exp(volatility*np.sqrt(1/periods_per_year))
d = 1/u
p = (np.exp((risk_free_rate-dividend_yield)*(1/periods_per_year))-d)/(u-d)

for path in range(number_of_paths):
    for t in range(Number_of_years*periods_per_year):
        if t == 0:
            path_matrix[path, t] = price_start
        else: 
            path_matrix[path, t] = path_matrix[path, t-1]*np.random.choice((u,d), p=[p,1-p])

#Output
for path in range(number_of_paths):
    plt.plot(path_matrix[path,:])
plt.show()
