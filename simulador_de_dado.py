#simulador de dado D6

import random
import PySimpleGUI as sg

class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Você quer jogar o dado?'
        self.layout = [
            [sg.Text('Jogar o dado?')],
            [sg.Button('Sim'), sg.Button('Não')],
          
        ]

          
    def Iniciar(self):
        self.janela = sg.Window('Simulador de dado', layout=self.layout, size= (100,100))

        self.eventos, self.valores = self.janela.Read()

        try:
            if self.eventos == 'Sim' or self.eventos == 's':
                self.GerarValordoDado()
            elif self.eventos == 'Não' or self.eventos == 'n':
                print('Agradecemos sua participação')
            else:
                print('Informe somente sim ou não.')
        except:
            print('Ocorreu um erro na sua resposta.')        
        
  
    def GerarValordoDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))
        

       
    

simulador = SimuladorDeDado()
simulador.Iniciar()




