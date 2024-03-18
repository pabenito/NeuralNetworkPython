import os
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Silenciar todos los mensajes
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

def crear_y_entrenar_modelo(x_train, y_train, input_dim, hidden_layers, epochs=1000):
    """
    Crea y entrena un modelo de red neuronal.

    Parámetros:
    - x_train: Entradas de entrenamiento.
    - y_train: Salidas de entrenamiento esperadas.
    - input_dim: Dimensión de entrada.
    - hidden_layers: Lista de tuplas (unidades, activación) para cada capa oculta.
    - epochs: Número de épocas para el entrenamiento.

    Retorna:
    - modelo entrenado.
    """
    model = Sequential()
    for i, (units, activation) in enumerate(hidden_layers):
        if i == 0:
            model.add(Dense(units, input_dim=input_dim, activation=activation))
        else:
            model.add(Dense(units, activation=activation))
    model.add(Dense(1, activation='sigmoid'))

    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    model.fit(x_train, y_train, epochs=epochs, verbose=0)

    return model

def mostrar_pesos_bias(model):
    """
    Muestra los pesos y bias de un modelo.

    Parámetro:
    - model: Modelo de red neuronal.
    """
    for i, layer in enumerate(model.layers):
        weights, bias = layer.get_weights()
        print(f"Capa {i+1} - Pesos: {weights}, Bias: {bias}")

# Datos de entrenamiento
datos = {
    'AND': (np.array([[0,0], [0,1], [1,0], [1,1]]), np.array([[0], [0], [0], [1]])),
    'OR': (np.array([[0,0], [0,1], [1,0], [1,1]]), np.array([[0], [1], [1], [1]])),
    'XOR': (np.array([[0,0], [0,1], [1,0], [1,1]]), np.array([[0], [1], [1], [0]])),
    'Función Compleja': (np.array([
        [0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1],
        [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]
    ]), np.array([[0], [0], [0], [1], [0], [1], [1], [1]]))
}

# Configuraciones de la red para cada ejercicio
configuraciones = {
    'AND': (2, []),
    'OR': (2, []),
    'XOR': (2, [(2, 'relu')]),  # XOR requiere al menos una capa oculta
    'Función Compleja': (3, [(4, 'relu')])  # Ejemplo con una capa oculta más compleja
}

for ejercicio, (x_train, y_train) in datos.items():
    input_dim, hidden_layers = configuraciones[ejercicio]
    print(f"\n{ejercicio}:")
    model = crear_y_entrenar_modelo(x_train, y_train, input_dim, hidden_layers)
    mostrar_pesos_bias(model)
