import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
#matplotlib inline
gdf = pd.read_csv(r'''C:\Users\Anjana_Bytha\Desktop\mytrial\gene_data.csv''')
mdf = pd.read_csv(r'''C:\Users\Anjana_Bytha\Desktop\mytrial\meta_data.csv''')

def isnan(num):
	if num != num:
		return True
	else:
		return False 

for index, row in gdf.iterrows():
		v[index][row] = isnan(gdf[index][row])

for i in v.rows():
	for j in v.columns():
		if i == False:
			pass
		else:
			print(i)

gdf = pd.DataFrame(gdf)
#features = ['sepal length', 'sepal width', 'petal length', 'petal width']
x = gdf.iloc[:, 2:33].values
y = mdf.loc[:,['Time']].values
x = StandardScaler().fit_transform(x)
x = pd.DataFrame(data = x)
#print(x)
n = np.isnan(x).any()
#print(n)

pca = PCA(n_components=2)
principalComponents = pca.fit_transform(x)
principalDf = pd.DataFrame(data = principalComponents
             , columns = ['principal component 1', 'principal component 2'])
#print(principalDf.head(5))

finalDf = pd.concat([principalDf, mdf[['Time']]], axis = 1)
#print(finalDf.head(5))

'''fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(1,1,1) 
ax.set_xlabel('Principal Component 1', fontsize = 15)
ax.set_ylabel('Principal Component 2', fontsize = 15)
ax.set_title('2 Component PCA', fontsize = 20)

targets = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
colors = ['r', 'g', 'b']
for target, color in zip(targets,colors):
    indicesToKeep = finalDf['target'] == target
    ax.scatter(finalDf.loc[indicesToKeep, 'principal component 1']
               , finalDf.loc[indicesToKeep, 'principal component 2']
               , c = color
               , s = 50)
ax.legend(targets)
ax.grid()
plt.show()'''