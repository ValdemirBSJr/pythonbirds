#!/home/valdemir/.virtualenvs/k36/bin/python
# -*- coding: utf-8 -*-
#Author: Valdemir Bezerra

class Pessoa:

    olhos = 2 #Atributo de classe/default -> Comum e igual a todos os objetos. Economiza memoria
    
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá, meu nome é: {self.nome}'

    #Para que um metodo independa do objeto que está sendo executado usa o decorator
    @staticmethod
    def metodo_estatico():
        #funcao atrelada a classe. Não precisa fazer referencia ao obj
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        #com esse decorator, temos acesso a classe que esta executando
        return f'{cls} - olhos: {cls.olhos}'

class Homem(Pessoa):
    #como herdar metodo
    def cumprimentar(self):
        cumprimentar_da_classe_pai = super().cumprimentar()
        return f'{cumprimentar_da_classe_pai}. Aperto de mão.'

class Mutante(Pessoa):
    olhos = 3
    #para sobrescrever o atributo, basta por uma variavel com o mesmo nome

if __name__=='__main__':
    p = Pessoa()
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())

    renzo = Pessoa(nome='Renzo')
    #renzo = Homem(nome='Renzo') #quando fazemos isso roda normal puq ele herdou de pessoa
    luciano = Pessoa(renzo, nome='Luciano')
    print(id(luciano))
    print(Pessoa.cumprimentar(luciano))
    print(luciano.nome)
    print(luciano.idade)
    print(luciano.filhos)

    for filho in luciano.filhos:
        print(filho.nome)

    del luciano.filhos #apaga atributo
    luciano.sobrenome = 'Ramalho' #adiciona atributo dinamicamente
    print(luciano.__dict__)
    print(renzo.__dict__) #ve qual atributos tem
    print(Pessoa.olhos)
    print(luciano.olhos)
    print(id(Pessoa.olhos), id(luciano.olhos), id(renzo.olhos)) #São o mesmo elemento

    luciano.olhos = 1

    print(luciano.__dict__) #se mudar o valor, ele passa a pertebcer ao grupo de atributo
    print(id(Pessoa.olhos), id(luciano.olhos), id(renzo.olhos)) #O de luciaono agora é diferente

    #Pessoa.olhos = 3 #Agora todo mundo terá 3 olhos, menos luciano puq foi explicitado que ele tem 1

    print(Pessoa.olhos)
    print(luciano.olhos)

    print(Pessoa.metodo_estatico(), luciano.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), luciano.nome_e_atributos_de_classe())

    pessoa = Pessoa('Anonimo')
    pessoa2 = Homem(nome='Lilo')
    print(isinstance(pessoa, Pessoa))#verifica se o objeto pertence a essa classe
    print(isinstance(pessoa, Homem))
    print(isinstance(pessoa2, Pessoa))
    print(isinstance(pessoa2, Homem))
    print(pessoa2.cumprimentar())

    pessoa3 = Mutante(nome='Luis')
    print(pessoa3.olhos)
