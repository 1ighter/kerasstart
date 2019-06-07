from keras.datasets import mnist

(train_image,train_labels),(test_image,test_labels) = mnist.load_data()

print(train_image.shape)