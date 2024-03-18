import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Datos de entrenamiento para la función lógica compleja
x_train = np.array([
    [0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1],
    [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]
])
y_train = np.array([[0], [0], [0], [1], [0], [1], [1], [1]])

# Definición del modelo
model_complex = Sequential()
model_complex.add(Dense(units=4, input_dim=3, activation='relu'))  # Capa oculta
model_complex.add(Dense(units=1, activation='sigmoid'))  # Capa de salida

# Compilar el modelo
model_and.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Entrenar el modelo
model_and.fit(x_train, y_train, epochs=1000, verbose=0)

# Mostrar los pesos y bias
weights_and, bias_and = model_and.layers[0].get_weights()
print("Pesos Función Lógica:", weights_and)
print("Bias Función Lógica:", bias_and)
