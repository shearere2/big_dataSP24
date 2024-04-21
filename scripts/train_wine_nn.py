from big_dataSP24.tensortango import mlp,layer,train_nn
if __name__ == "__main__":
    features = 0
    labels = 0
    neural_net = mlp.MLP([layer.Tanh(2,2),
                          layer.Tanh(2,2)])
    train_nn(neural_net,features,labels)
    print(neural_net.forward(features))