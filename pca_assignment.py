import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

#loading data files
gdf = pd.read_csv(r'''C:\Users\Anjana_Bytha\Desktop\Assignment\gene_data.csv''') 
mdf = pd.read_csv(r'''C:\Users\Anjana_Bytha\Desktop\Assignment\meta_data.csv''')


def cleandata(gdf, mdf):
#checking if they are in numeric form
	r1=gdf.shape[0] #gives number of row count
	c1=gdf.shape[1] #gives number of col count
	r2=mdf.shape[0] #gives number of row count

	newlist=[] #creates blank list
	for i in range(r1,1):
		if gdf.iloc[i,1].dtype == np.float32:
			pass
		else:
			print(gdf.iloc[i,1])
			newlist.append(gdf.iloc[i,1])
			print(newlist)

	newlist1=[] #creates blank list
	for i in range(r2,1):
	    if mdf.iloc[i,1].dtype == np.int32:
	        pass
	    else:
	        print(mdf.iloc[i,1])
	        newlist1.append(mdf.iloc[i,1])
	        print(newlist1)


def PCAfunc(gdf, mdf):
	#removing the categorical values
	gdf = gdf.iloc[:, 2:33].values
	mdf = mdf.loc[:,['Time']].values

	gdf = gdf.iloc[:, 2:33].values
	mdf = mdf.loc[:,['Time']].values
	x = StandardScaler().fit_transform(gdf)
	x = pd.DataFrame(data = x)

	pca = PCA(n_components=2)
	principalComponents = pca.fit_transform(x)
	principalDf = pd.DataFrame(data = principalComponents
	             , columns = ['principal component 1', 'principal component 2'])
	mdf = pd.DataFrame(mdf)
	finalDf = pd.concat([principalDf, mdf], axis =1)
	print(finalDf.head(5))
	principalDf = principalDf.head(30)

	fig = plt.figure(figsize = (8,8))
	ax = fig.add_subplot(1,1,1) 
	ax.set_xlabel('Principal Component 1', fontsize = 10)
	ax.set_ylabel('Principal Component 2', fontsize = 10)
	ax.set_title('2 Component PCA', fontsize = 15)

	features = ['0','4','5','6','7','8','9','10','11','12']
	for feature in zip(features):
	    indicesToKeep = finalDf['mdf'] == feature
	    ax.scatter(finalDf.loc[indicesToKeep, 'principal component 1']
	               , finalDf.loc[indicesToKeep, 'principal component 2']
	               , c = color
	               , s = 50)
	plt.show()