import random

from Capa import Capa
from FuncionActivacion import activacion_binaria
from Neurona import Neurona
from RedNeuronal import RedNeuronal


def get_red_neuronal_media(numero_de_asignaturas, nota_media_corte):
    neurona = Neurona([1 / numero_de_asignaturas] * numero_de_asignaturas, -nota_media_corte)
    return RedNeuronal([Capa([neurona], activacion_binaria)])


def get_neurona_and():
    return Neurona([1, 1], -1.5)


def get_neurona_or():
    return Neurona([1, 1], -0.5)


def get_red_neuronal_and():
    return RedNeuronal([Capa([get_neurona_and()], activacion_binaria)])


def get_red_neuronal_or():
    return RedNeuronal([Capa([get_neurona_or()], activacion_binaria)])


def get_red_neuronal_xor():
    return RedNeuronal(
        [Capa([get_neurona_and(), get_neurona_or()], activacion_binaria),
         Capa([Neurona([-1, 1], -0.5)], activacion_binaria)])

def get_red_neuroronal_funcion_binaria():
    return RedNeuronal([Capa([Neurona([1, 1, 1], -1.5)], activacion_binaria)])

def run_red_neuronal_media(numero_de_asignaturas, nota_media_corte, min, max):
    red_neuronal_media = get_red_neuronal_media(numero_de_asignaturas, nota_media_corte)
    notas = [random.randint(min, max) for _ in range(numero_de_asignaturas)]
    media = sum(notas) / len(notas)
    print(f"Notas: {notas}")
    print(f"Media: {media}")
    print(f"Becado: {red_neuronal_media.activar(notas)}")

def run_red_neuronal_and():
    red_neuronal_and = get_red_neuronal_and()
    print(f"0 and 0: {red_neuronal_and.activar([0, 0])}")
    print(f"0 and 1: {red_neuronal_and.activar([0, 1])}")
    print(f"1 and 0: {red_neuronal_and.activar([1, 0])}")
    print(f"1 and 1: {red_neuronal_and.activar([1, 1])}")

def run_red_neuronal_or():
    red_neuronal_or = get_red_neuronal_or()
    print(f"0 or 0: {red_neuronal_or.activar([0, 0])}")
    print(f"0 or 1: {red_neuronal_or.activar([0, 1])}")
    print(f"1 or 0: {red_neuronal_or.activar([1, 0])}")
    print(f"1 or 1: {red_neuronal_or.activar([1, 1])}")

def run_red_neuronal_xor():
    red_neuronal_xor = get_red_neuronal_xor()
    print(f"0 xor 0: {red_neuronal_xor.activar([0, 0])}")
    print(f"0 xor 1: {red_neuronal_xor.activar([0, 1])}")
    print(f"1 xor 0: {red_neuronal_xor.activar([1, 0])}")
    print(f"1 xor 1: {red_neuronal_xor.activar([1, 1])}")

def run_red_neuronal_funcion_binaria():
    red_neuronal_funcion_binaria = get_red_neuroronal_funcion_binaria()
    print(f"0, 0, 0: {red_neuronal_funcion_binaria.activar([0, 0, 0])}")
    print(f"0, 0, 1: {red_neuronal_funcion_binaria.activar([0, 0, 1])}")
    print(f"0, 1, 0: {red_neuronal_funcion_binaria.activar([0, 1, 0])}")
    print(f"0, 1, 1: {red_neuronal_funcion_binaria.activar([0, 1, 1])}")
    print(f"1, 0, 0: {red_neuronal_funcion_binaria.activar([1, 0, 0])}")
    print(f"1, 0, 1: {red_neuronal_funcion_binaria.activar([1, 0, 1])}")
    print(f"1, 1, 0: {red_neuronal_funcion_binaria.activar([1, 1, 0])}")
    print(f"1, 1, 1: {red_neuronal_funcion_binaria.activar([1, 1, 1])}")


if __name__ == '__main__':
    run_red_neuronal_media(5, 6, 0, 10)
    run_red_neuronal_and()
    run_red_neuronal_or()
    run_red_neuronal_xor()
    run_red_neuronal_funcion_binaria()