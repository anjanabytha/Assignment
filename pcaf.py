import pca as p

#loading data files
gdf = pd.read_csv(r'''C:\Users\Anjana_Bytha\Desktop\Assignment\gene_data.csv''') 
mdf = pd.read_csv(r'''C:\Users\Anjana_Bytha\Desktop\Assignment\meta_data.csv''')

pca.cleandata(gdf,mdf) #function to clean data
pca.PCAfunc(gdf, mdf) #function to apply PCA