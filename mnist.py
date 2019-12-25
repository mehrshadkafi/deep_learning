# Loading the mnist dataset in keras
from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
print(train_images.shape)
print(len(train_labels))
print(train_labels)
print(test_images.shape)
print(len(test_labels))
print(test_labels)

# The network architecture
network = models.Sequential()
network.add(layers.Dense(512, activation='relu', input_shape=(28 * 28, )))
network.add(layers.Dense(10, activation='softmax'))

# The compilation Step
network.compile(optimizer='rmsprop',
                loss='categorical_crossentropy',
                metrics=['accuracy'])

# Preparing the image data
train_images = train_images.reshape((60000, 28*28))
train_images = train_images.astype('float32')/255

test_images = test_images.reshape((10000, 28*28))
test_images = test_images.astype('float32')/255

# Preparing the labels
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

# Fit network
network.fit(train_images, train_labels, epochs=5, batch_size=128)

# Test
test_loss, test_acc = network.evaluate(test_images, test_labels)
print('test_acc:', test_acc)