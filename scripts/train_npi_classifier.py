from big_dataSP24.week5 import npi_reader, npi_classifier

df = npi_reader.read('data/npidata_pfile_20240205-20240211.csv')
nc = npi_classifier.NPIClassifier('Models')
#             these columns                to predict this
nc.train(df.drop(columns=['last_name']), df['last_name']) # Not sure what columns to train on?

nc.save('npi_classifier')