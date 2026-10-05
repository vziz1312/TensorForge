import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

import tensorflow as tf

x_train = tf.constant([[1.0], [2.0], [3.0], [4.0]])
y_train = tf.constant([2.0, 4.0, 6.0, 8.0])

x_test = tf.constant([[5.0], [6.0], [7.0]])
y_test = tf.constant([10.0, 12.0, 14.0])

model=tf.keras.Sequential([
    tf.keras.layers.Dense(1)])

model.compile(
    optimizer=tf.keras.optimizers.SGD(learning_rate=0.1),
    loss="mse"
)
model.fit(x_train, y_train, epochs=100, verbose=0)

test_loss = model.evaluate(x_test, y_test, verbose=0)

print("Test loss:", test_loss)
predictions = model.predict(x_test, verbose=0)

print("Predictions:", predictions.flatten())
print("Actual:", y_test.numpy())
