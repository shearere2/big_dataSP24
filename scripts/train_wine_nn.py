from big_dataSP24.tensortango import mlp,layer,train_nn
from big_dataSP24.week4 import read_wine_data
import pandas as pd
if __name__ == "__main__":
    df = read_wine_data.read()
    features = pd.read_csv('data/dimensionality_reduced_wine_5.csv')
    print()
    labels = df['quality']
    neural_net = mlp.MLP([layer.Tanh(2,2),
                          layer.Tanh(2,2)])
    train_nn.train(neural_net,features,labels)
    print(neural_net.forward(features))