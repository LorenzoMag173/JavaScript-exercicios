from Model import Model

class Control:

    def __init__(self):
        self.modelo = Model()
        self.opcao = 0

    def mostrarMenu(self):
        print ('Escolha uma das opcões abaixo: '+
              '\n1. Sair'                       +
              '\n2. Trocar'                     +
              '\n3. Tabuada'                    +
              '\n4. Exercicio 01'               )

    def operacoes(self):
        while(self.opcao != 1):
            self.mostrarMenu()
            self.opcao = int(input('Escolha uma das opções acima: '))
            if self.opcao == 1:
                print('obrigado')
            elif self.opcao == 2:
                valorA = int(input('informe um valor para A'))
                valorB = int(input('informe um valor para B'))
                print(self.modelo.trocar(valorA,valorB))
            elif self.opcao == 3:
                num = int(input('informe um número: '))
                print(self.modelo.tabuada(num))

            elif self.opcao == 4:
                num = int(input("informe um número"))
                print(self.modelo.exercicioUm(num))

            elif self.opcao == 6:
                num = int(input("informe um número"))
                print(self.modelo.exercicioDois(num))

            elif self.opcao == 7:
                print(f'a soma dos números entre 1 e 100 é:{self.modelo.exercicioTres()}')

            elif self.opcao == 8:
                num = int(input("informe um número"))
                print(f'Os multiplos de 5, de 1 a 50 são: \n{self.modelo.exercicioQuatro()}')

            elif self.opcao == 9:
                num = int(input("Informe um número: "))
                print(self.modelo.exercicioCinco(num))




            else:
                print('opção escolhida não e válida')

