import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
 
objects = ('Cupertino', 'Orinda', 'Rohnert Park', 'Los Altos', 'Saratoga', 'Fairfax', 'Sausalito', 'Sebastopol', 'South San Francisco', 'Vacaville', 'Emeryville', 'Rio Vista', 'Burlingame', 'Dixon', 'Petaluma', 'Piedmont', 'Sonoma', 'Cotati', 'San Carlos', 'Morgan Hill', 'Redwood City', 'Albany', 'Mountain View', 'Pacifica', 'Suisun City', 'Santa Clara', 'Milpitas', 'Novato', 'Vallejo', 'Belmont', 'Sunnyvale', 'San Bruno', 'Benicia', 'Newark', 'Daly City', 'Gilroy', 'Pinole', 'El Cerrito', 'Napa', 'San Mateo', 'Brentwood', 'Alameda', 'Clayton', 'Pittsburg', 'Dublin', 'Hercules', 'San Rafael', 'Berkeley', 'Santa Rosa', 'Pleasant Hill', 'East Palo Alto', 'Martinez', 'San Pablo', 'Concord', 'Fairfield', 'Antioch', 'San Francisco', 'San Jose', 'San Leandro', 'Danville', 'Oakland', 'Menlo Park', 'Union City', 'Hayward', 'Fremont', 'Livermore', 'Richmond', 'Pleasanton', 'Oakley', 'Walnut Creek', 'San Ramon')

y_pos = np.arange(len(objects))

cost = [100, 127, 173, 233, 366, 455, 573, 622, 873, 910, 995, 1047, 1083, 1096, 1135, 1305, 1449, 1463, 2021, 2070, 2628, 3385, 3488, 3554, 3788, 4952, 4967, 5267, 5431, 5438, 5865, 6750, 7151, 7330, 8267, 9406, 9484, 9935, 10790, 11394, 11524, 12302, 14777, 15809, 16170, 16211, 17091, 18144, 18434, 19151, 21437, 21527, 23074, 26611, 27024, 27140, 27881, 28065, 28936, 30718, 31096, 31500, 33317, 34050, 34198, 38010, 39235, 41440, 44467, 48571, 48804]

barlist = plt.bar(y_pos, cost, align='center', alpha=0.5, color="orange")
plt.xticks(y_pos, objects, rotation='vertical')
plt.tick_params(labelsize=4)
ax=plt.gca()
ax.tick_params(axis='x', colors='black')

sns.set_style("whitegrid")
tips = sns.load_dataset("tips")
axis = sns.barplot(x=objects, y=cost, data=tips)

plt.xlabel('Cities')
plt.title('Total Cost to Complete School Projects')

plt.savefig("costtocomplete_all")
plt.show()