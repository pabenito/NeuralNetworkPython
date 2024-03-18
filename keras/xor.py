import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Datos de entrenamiento para XOR
x_train = np.array([[0,0], [0,1], [1,0], [1,1]])
y_train = np.array([[0], [1], [1], [0]])

# Definición del modelo
model_xor = Sequential()
model_xor.add(Dense(2, input_dim=2, activation='relu'))  # Capa oculta
model_xor.add(Dense(1, activation='sigmoid'))  # Capa de salida

# Compilar el modelo
model_and.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Entrenar el modelo
model_and.fit(x_train, y_train, epochs=1000, verbose=0)

# Mostrar los pesos y bias
weights_and, bias_and = model_and.layers[0].get_weights()
print("Pesos XOR:", weights_and)
print("Bias XOR:", bias_and)
