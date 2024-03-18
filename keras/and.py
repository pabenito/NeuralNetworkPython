import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Datos de entrenamiento para AND
x_train = np.array([[0,0], [0,1], [1,0], [1,1]])
y_train = np.array([[0], [0], [0], [1]])

# Definición del modelo
model_and = Sequential()
model_and.add(Dense(1, input_dim=2, activation='sigmoid'))

# Compilar el modelo
model_and.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Entrenar el modelo
model_and.fit(x_train, y_train, epochs=1000, verbose=0)

# Mostrar los pesos y bias
weights_and, bias_and = model_and.layers[0].get_weights()
print("Pesos AND:", weights_and)
print("Bias AND:", bias_and)
