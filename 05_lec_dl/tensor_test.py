import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

(X_train, y_train), (X_test, y_test) = tf.keras.datasets.mnist.load_data()

X_train = X_train / 255.0
X_test = X_test / 255.0

# CNN
model = Sequential([
    tf.keras.Input(shape=(28, 28, 1)),
    Conv2D(16, 3, activation='relu'),
    MaxPooling2D(2),
    Flatten(),
    Dense(10, activation='softmax')
])

# 설정
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# 학습
model.fit(
    X_train,
    y_train,
    epochs=3,
    batch_size=64
)

# 평가
loss, acc = model.evaluate(X_test, y_test)

print("정확도 :", acc)