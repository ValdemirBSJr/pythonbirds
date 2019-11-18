#!/home/valdemir/.virtualenvs/k36/bin/python
# -*- coding: utf-8 -*-
#Author: Valdemir Bezerra

'''
Para usar o framework de testes do python o arquivo deve comecar com test
e o metodo com test tbm
'''

from unittest import TestCase
from oo.exercicio_composicao import Motor

class CarroTestCase(TestCase):
    def teste_velocidade_inicial(self):
        motor = Motor()
        self.assertEqual(0, motor.velocidade) #testa se o valor de velocidade é igual a zero

    def teste_acelerar(self):
        motor = Motor()
        motor.acelerar()
        self.assertEqual(1, motor.velocidade)