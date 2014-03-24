'''
transform data to train LR
'''
from numpy import *

# change 0 to [1 0 0 0]
# change 1 to [0 1 0 0]
# change 2 to [0 0 1 0]
# change 3 to [0 0 0 1]
def parse_action(action):
    features = []
    if action == 0:
        features = ['1','0','0','0']
    elif action == 1:
        features = ['0','1','0','0']
    elif action == 2:
        features = ['0','0','1','0']
    elif action == 3:
        features = ['0','0','0','1']
    return features
    

def perpareTrainData(train_file, train_label):
    lrTrain_file = open('data/lrTrain.txt', "w")
    for line in train_file.readlines():
        entry = line.split(',')
        actions = parse_action(int(entry[2]))
        lrTrain_file.write(entry[0] + "," + entry[1] + "," + ",".join(actions) + "," + entry[3])
    lrTrain_file.close()

##########main#############
train_file = open('data/train.csv')
train_label = open('data/validation.csv')
perpareTrainData(train_file,train_label)
