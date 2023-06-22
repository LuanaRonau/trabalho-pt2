from telas.abstract_tela import AbstractTela
import PySimpleGUI as sg


class TelaFilial(AbstractTela):

    def __init__(self):
        super().__init__()
        self.__window = None 
        self.init_components()

    def mostra_opcoes(self):
        self.init_components()
        event, values = self.__window.Read()
        self.__window.Close()
        if event in (None, 'Cancelar'):
            event = 0
        opcao = int(event)
        return opcao
    
    def init_components(self):
        sg.ChangeLookAndFeel('Dark Gray 13')
        layout = [
            [sg.Text('Gerenciando a filial')],
            [sg.Text('O que deseja fazer?')],
            [sg.Button('Acessar opções de funcionários comuns', key=1, size=[30, 1])],
            [sg.Button('Acessar opções de gerencia', key=2, size=[30, 1])],
            [sg.Button('Modificar dados da filial', key=3, size=[30, 1])],
            [sg.Button('Acessar contratos da filial', key=4, size=[30, 1])],
            [sg.Button('Acessar funcionários ativos', key=5, size=[30, 1])],
            [sg.Button('Sair', key=0, size=[30, 1])]
        ]
        self.__window = sg.Window('Controle da Filial', layout, element_justification='c')

    def menu_modificacao(self):
        sg.ChangeLookAndFeel('Dark Gray 13')
        layout = [
            [sg.Text('O que deseja modificar?')],
            [sg.Text('(Para demais modificações, consulte as outras opções do menu.)')],
            [sg.Button('CEP', key=1, size=[30, 1])],
            [sg.Button('Cidade', key=2, size=[30, 1])],
            [sg.Button('Sair', key=0, size=[30, 1])],
        ]
        self.__window = sg.Window('Controle da Filial', layout, element_justification='c')

        event, values = self.__window.Read()
        self.__window.Close()
        return int(event)
    
    def le_cep(self):
        sg.ChangeLookAndFeel('Dark Gray 13')
        layout = [
            [sg.Text('Modificação de Filial')],
            [sg.Text('Digite no campo abaixo o novo CEP da filial')],
            [sg.Text('CEP:', size=(15, 1)), sg.InputText('', key='cep')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Controle da Filial', layout, element_justification='c')
        event, values = self.__window.Read()
        self.__window.Close()
        return values['cep']

    def le_cidade(self):
        sg.ChangeLookAndFeel('Dark Gray 13')
        layout = [
            [sg.Text('Modificação de Filial')],
            [sg.Text('Digite no campo abaixo a nova cidade da filial')],
            [sg.Text('Cidade:', size=(15, 1)), sg.InputText('', key='cidade')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Controle da Filial', layout, element_justification='c')
        event, values = self.__window.Read()
        self.__window.Close()
        return values['cidade']

    def listagem(self, funcionarios):
        string = ''
        for fun in funcionarios:
            string += f"\nNome: {fun.nome}\nCPF: {fun.cpf}\nData_nasc: {fun.data_nasc}\n"
        sg.Popup("Listagem de funcionários\n", string)

    def mostra_mensagem(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values
