from big_dataSP24.week6 import npi_reader, grants_reader, string_distance_features
from big_dataSP24.week5 import npi_classifier
import pandas as pd

grants_df = grants_reader.read_grants_year(2022)
npi_df = npi_reader.read('data/npidata_pfile_20240205-20240211.csv')

sdf = string_distance_features.StringDistanceFeatures()
train = pd.read_csv('data/toy_training.csv')
comb_df = sdf.combine_prediction_data(grants_df, npi_df)
features = sdf.features_from_pairs(train)
print(features)


nc = npi_classifier.NPIClassifier('Models')

nc.train(features,train['is_match'])
nc.predict()

nc.save('npi_classifier')