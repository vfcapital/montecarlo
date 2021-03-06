import numpy as np
import matplotlib.pyplot as plt

# Set input variables
number_of_years = 4
periods_per_year = 360
number_of_paths = 10
price_start = 100
risk_free_rate = 0
volatility = 0.2
dividend_yield = 0

# Create empty path matrix
path_matrix = np.empty((number_of_paths,number_of_years*periods_per_year))

#Calculate risk-neutral probability
u = np.exp(volatility*np.sqrt(1/periods_per_year))
d = 1/u
p = (np.exp((risk_free_rate-dividend_yield)*(1/periods_per_year))-d)/(u-d)

# Fill path matrix with random walks
for path in range(number_of_paths):
    for t in range(number_of_years*periods_per_year):
        if t == 0:
            path_matrix[path, t] = price_start
        else: 
            path_matrix[path, t] = path_matrix[path, t-1]*np.random.choice((u,d), p=[p,1-p])

# Create plot
x_ticks = [0, 200, 560, 920, 1280]
x_labels = ['', 'Jahr 1', 'Jahr 2', 'Jahr 3', 'Jahr 4']            

f = plt.figure()
f.set_figwidth(16)
f.set_figheight(8)

for path in range(number_of_paths):
    plt.plot(path_matrix[path,:], linewidth = 0.9)   

plt.rc('font', size=17)
plt.style.use('seaborn-whitegrid')
plt.xlim((0,1500))
plt.xticks(ticks = x_ticks, labels = x_labels)
plt.grid(axis ="x")

plt.show()
