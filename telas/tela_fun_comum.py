from telas.tela_funcionarios import TelaFuncionario
import PySimpleGUI as sg


class TelaFuncomum(TelaFuncionario):

    def __init__(self):
        super().__init__()
        self.__window = None 
        self.init_components()

    def mostra_opcoes(self):
        self.init_components()
        event, values = self.__window.Read()
        self.__window.Close()
        if event in (None, 'Cancelar'):
            exit(0)
        return int(event)
    
    def init_components(self):
        sg.ChangeLookAndFeel('Dark Gray 13')
        layout = [
            [sg.Text('TELA DE MODIFICAÇÃO: FUNCIONARIO COMUM')],
            [sg.Text('O que deseja fazer?')],
            [sg.Button('Modificar informações', key=1, size=[30, 1])],
            [sg.Button('Cadastrar novo funcionário comum', key=2, size=[30, 1])],
            [sg.Button('Acessar contrato', key=3, size=[30, 1])],
            [sg.Button('Listar todos', key=4, size=[30, 1])],
            [sg.Button('Demitir', key=5, size=[30, 1])],
            [sg.Button('Retornar', key=0, size=[30, 1])]
        ]
        self.__window = sg.Window('Controle de Funcionário Comum', layout, element_justification='c')

    def pega_cpf(self, msg):
        return self.le_int_positivo(msg)

    def listagem(self, funcionarios):
        string = ''
        for fun in funcionarios:
            string += f"\nNome: {fun.nome}\nCPF: {fun.cpf}\nData_nasc: {fun.data_nasc}\n"
        sg.Popup("Listagem de funcionários comuns", string)

    def mostra_mensagem(self, msg):
        sg.popup("", msg)

