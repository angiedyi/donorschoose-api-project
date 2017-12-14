import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
 
objects = ('Orinda', 'Pacifica', 'Piedmont', 'Vallejo', 'Union City', 'Richmond', 'Newark', 'Novato', 'Sunnyvale', 'South San Francisco', 'Cupertino', 'Daly City', 'Sebastopol', 'Fairfax', 'Santa Clara', 'San Rafael', 'Los Altos', 'San Carlos', 'Milpitas', 'Alameda', 'Santa Rosa', 'Saratoga', 'Burlingame', 'Albany', 'Benicia', 'San Jose', 'El Cerrito', 'Napa', 'Brentwood', 'Martinez', 'Concord', 'Pleasant Hill', 'Belmont', 'Clayton', 'Dublin', 'Danville', 'Livermore', 'Pleasanton', 'Fremont', 'San Ramon', 'Walnut Creek')

y_pos = np.arange(len(objects))

cost = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 5, 6, 7, 7, 9, 10, 19, 19, 20, 26, 39, 41, 46, 50]

barlist = plt.bar(y_pos, cost, align='center', alpha=0.5, color="orange")
plt.xticks(y_pos, objects, rotation='vertical')
plt.tick_params(labelsize=4)
ax=plt.gca()
ax.tick_params(axis='x', colors='black')

sns.set_style("whitegrid")
tips = sns.load_dataset("tips")
axis = sns.barplot(x=objects, y=cost, data=tips)

plt.xlabel('Cities')
plt.title('Total # of Lowest Poverty Projects By City')

plt.savefig("lowpov_cities_bargraph")
plt.show()