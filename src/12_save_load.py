import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

import tensorflow as tf

x = tf.constant([[1.0], [2.0], [3.0], [4.0]])
y = tf.constant([2.0, 4.0, 6.0, 8.0])

model=tf.keras.Sequential([
    tf.keras.layers.Dense(1)
])

model.compile(
    optimizer=tf.keras.optimizers.SGD(0.1),
    loss='mse'
)

model.fit(x,y,epochs=100, verbose=0)

model.save("../models/football_model.keras")

loaded_model=tf.keras.models.load_model("../models/football_model.keras")
print("Model loaded successfully")


prediction = loaded_model.predict(
    tf.constant([[5.0]]),
    verbose=0
)

print("Prediction for 5:", prediction[0][0])

original_prediction = model.predict(
    tf.constant([[5.0]]),
    verbose=0
)

loaded_prediction = loaded_model.predict(
    tf.constant([[5.0]]),
    verbose=0
)

print("Original model:", original_prediction[0][0])
print("Loaded model:", loaded_prediction[0][0])

