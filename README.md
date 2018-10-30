# Assignment
Running Principal Component Analysis on Gene data using Python

The very first thing I did was to analyze the data that was given to me. It consisted of two files, the gene_data.csv consisting of 32 features and 22,412 rows of which 30 were numeric. The first two columns were not considered because categorial attributes have no effect in Principal Component Analysis. The second dataset was meta_data.csv, a meta data file which consisted of three columns and 30 rows. 

Upon running initial cleaning methods on the data, I first checked if all of them were numeric values and did not contain other data types. I found that some of the records contained string values in place for numeric values which I replaced with 0 for this instant in time, fully being aware of the effect it could have on the result. This ensured that the given data was of the desired type.  

After which I scaled the data using StandardScalar from sklearn which makes the mean of the data 0 and a variance of 1. Scaling is important while applying functions such as PCA to not let the higher values dominate the function and produce wrong results. Then, I applied the PCA function in sklearn to obtain the two  principal components PC! and PC2. And then, used that to plot a graph between them.

The Principal Component Analysis is used to to reduce the number of dimensions of data when it has high dimensionality. PCA is essentially useful is understanding and minimizing the number of dimensions to analyze the data and gain the main essence. In this case it reduces the features of the gene data to determine how they behave. 

