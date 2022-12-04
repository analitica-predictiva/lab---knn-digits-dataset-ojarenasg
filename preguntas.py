"""
Clasificación usando k-NN - Digits Dataset
-----------------------------------------------------------------------------------------

En este laboratio se construirá un clasificador usando k-NN para el dataset de digitos.

"""
import sys

import preguntas


def test_01():
    preguntas.pregunta_01()


def test_02():
    preguntas.pregunta_02()


def test_03():
    assert preguntas.pregunta_03().to_dict() == {
        "k": {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8},
        "train_accuracy": {
            0: 1.0,
            1: 0.9916492693110647,
            2: 0.9937369519832986,
            3: 0.9937369519832986,
            4: 0.9916492693110647,
            5: 0.9895615866388309,
            6: 0.9902574808629089,
            7: 0.9895615866388309,
        },
        "test_accuracy": {
            0: 0.9861111111111112,
            1: 0.9861111111111112,
            2: 0.9861111111111112,
            3: 0.9833333333333333,
            4: 0.9833333333333333,
            5: 0.9805555555555555,
            6: 0.9833333333333333,
            7: 0.9777777777777777,
        },
    }


test = {
    "01": test_01,
    "02": test_02,
    "03": test_03,
}[sys.argv[1]]

test()