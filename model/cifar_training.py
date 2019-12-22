(x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()

fig = plt.figure()

for i in range(3):
  a = fig.add_subplot(1, 3, i+1)
  random = np.random.randint(0, len(x_train))
  imgplot = plt.imshow(x_train[random])
  a.set_title(y_train[random])

x_train = x_train / 255
x_test = x_test / 255

y_train = keras.utils.to_categorical(y_train)
y_test = keras.utils.to_categorical(y_test)

print('Train data shape: ', x_train.shape)
print('Train labels shape: ', y_train.shape)

print('Test data shape: ', x_test.shape)
print('Test labels shape: ', y_test.shape)

# Train Net
model = ResNet(classes=10)(keras.Input(shape=(32, 32, 3)))
model.compile(optimizer=keras.optimizers.SGD(), loss=keras.losses.CategoricalCrossentropy(), metrics=[keras.metrics.CategoricalAccuracy()])
model.build(input_shape=(50000, 32, 32, 3))
model.fit(x_train, y_train, batch_size=256, epochs=100, validation_data=(x_test, y_test), shuffle=True)
