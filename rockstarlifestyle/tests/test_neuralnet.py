from rockstarlifestyle import neuralnet as nn
from rockstarlifestyle import imcrop as iC
import skimage.io as sio
import warnings


def test_save_objects():
    testin_saving_obj = nn.TestObj((1234567, 8910))
    nn.save_objects([testin_saving_obj], name='save_test.dat')
    testout_saving_obj = nn.load_objects(name='save_test.dat')
    assert testin_saving_obj.res == testout_saving_obj[0].res, "Something went wrong with saving"


    return

def test_load_objects():
    testin_load_obj = nn.TestObj((8675, 309))
    nn.save_objects([testin_load_obj], name='load_test.dat')
    testout_load_obj = nn.load_objects(name='load_test.dat')
    assert testin_load_obj.res == testout_load_obj[0].res, "Something went wrong with loading"


    return

def test_create_train_set():
    test1, test2 = nn.create_train_set(numb_sets=1)
    assert test1 == test2, "New training set case failed"
    assert len(test1) == 1, "Length incorrect"
    assert test1[0].res == (256, 256), "New training value is not right size"
    test1, test2 = nn.create_train_set(numb_sets=1, prev_set=test1)
    assert len(test1) == 2, "Length incorrect"

    return

def test_accuracy():

    training_set, _ = nn.create_train_set(numb_sets=1)
    dataset = training_set
    train_x = None
    train_y = None
    value = None
    lrn_dataset = None
    lrn_cnt = None
    train_x = []
    train_y = []
    value = []
    lrn_dataset = []
    lrn_cnt = []
    nn.neuralnet(training_set,
                 train=True,
                 save_settings=True,
                 print_acc=False)
    classifier = nn.load_objects('classifier_info.dat')[0]
    for k in range(len(dataset)):
        value.append([])
        for i in range(len(dataset[k].heights)//3):
            value[k].append(dataset[k].heights[i*3])

    for k in range(len(dataset)):
        lrn_dataset.append([])
        lrn_cnt.append(dataset[k].count)
        for ht_val in value[k]:
            lrn_dataset[k].append(ht_val[0])
    train_x = lrn_dataset
    train_y = lrn_cnt
    assert nn.accuracy(train_x,
                       train_y,
                       classifier,
                       output=False)['success'][0], "Accuracy didn't happen"

    return

def test_neuralnet():

    training_set, _ = nn.create_train_set(numb_sets=1)
    nn.neuralnet(training_set,
                 train=True,
                 save_settings=True,
                 print_acc=False)
    classifier = nn.load_objects('classifier_info.dat')[0]
    assert classifier.solver == 'lbfgs', "Wrong solver"
    assert classifier.hidden_layer_sizes == (100,), "Wrong # of hidden layers"
    assert classifier.activation == 'tanh', "Wrong activation"
    cnt = nn.neuralnet(training_set,
                       nn_settings=classifier,
                       train=False,
                       save_settings=False,
                       print_acc=False)
    assert cnt[0] == training_set[0].count, "Bad fitting"

    return

