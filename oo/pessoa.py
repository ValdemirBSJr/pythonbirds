class Pessoa:

    olhos = 2 #Atributo de classe/default -> Comum e igual a todos os objetos. Economiza memoria
    
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__=='__main__':
    p = Pessoa()
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())

    renzo = Pessoa(nome='Renzo')
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

    Pessoa.olhos = 3 #Agora todo mundo terá 3 olhos, menos luciano puq foi explicitado que ele tem 1

    print(Pessoa.olhos)
    print(luciano.olhos)
