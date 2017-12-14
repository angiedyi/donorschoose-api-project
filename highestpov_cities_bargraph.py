import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
 
objects = ('Mountain View', 'San Leandro', 'San Jose', 'Vallejo', 'Santa Rosa', 'Antioch', 'San Rafael', 'San Francisco', 'Concord', 'Fairfield', 'Richmond', 'San Pablo', 'East Palo Alto', 'Oakland', 'Menlo Park')

y_pos = np.arange(len(objects))

cost = [2, 4, 4, 5, 7, 8, 8, 13, 13, 15, 17, 19, 23, 25, 29]

barlist = plt.bar(y_pos, cost, align='center', alpha=0.5, color="orange")
plt.xticks(y_pos, objects, rotation='vertical')
plt.tick_params(labelsize=4)
ax=plt.gca()
ax.tick_params(axis='x', colors='black')

sns.set_style("whitegrid")
tips = sns.load_dataset("tips")
axis = sns.barplot(x=objects, y=cost, data=tips)

plt.xlabel('Cities')
plt.title('Total # of Highest Poverty Projects By City')

plt.savefig("highestpov_cities_bargraph")
plt.show()