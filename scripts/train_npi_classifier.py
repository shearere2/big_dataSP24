from big_dataSP24.week5 import npi_reader, npi_classifier, combine_dfs, distances
from big_dataSP24.week4 import read_data

model = distances.NameDistance()
df1 = npi_reader.read('data/npidata_pfile_20240205-20240211.csv')
df2 = read_data.read_grants_year(2022)
df = combine_dfs.combine_dfs(df1,df2)

train = model.training_data(df)

nc = npi_classifier.NPIClassifier('Models')

nc.train()

nc.save('npi_classifier')