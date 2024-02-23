from big_dataSP24.week4 import read_wine_data, wine_classifier

df = read_wine_data.read()
wc = wine_classifier.WineClassifier('Models')
wc.train(df.drop(columns=['quality']), df['quality'])
wc.save('wine_classifier')