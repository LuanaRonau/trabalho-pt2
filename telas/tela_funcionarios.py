from telas.abstract_tela import AbstractTela
import PySimpleGUI as sg
from datetime import date


class TelaFuncionario(AbstractTela):

    def __init__(self):
        super().__init__()
        self.__window = None 

    def mostra_opcoes(self):
        pass

    def menu_modificacao(self):
        sg.ChangeLookAndFeel('Dark Gray 13')
        layout = [
            [sg.Text('O que deseja modificar?')],
            [sg.Button('Nome', key=1, size=[30, 1])],
            [sg.Button('CPF', key=2, size=[30, 1])],
            [sg.Button('Data de nascimento', key=3, size=[30, 1])],
            [sg.Button('Retornar', key=0, size=[30, 1])]
        ]
        self.__window = sg.Window('Controle de Funcionário', layout, element_justification='c')

        event, values = self.__window.Read()
        self.__window.Close()
        return int(event)
    
    def pega_dados_cadastro(self):
        sg.ChangeLookAndFeel('Dark Gray 13')
        layout = [
            [sg.Text('Cadastro de Funcionário')],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Text('CPF:', size=(15, 1)), sg.InputText('', key='CPF')],
            [sg.Text('Data de nascimento:', size=(15, 1)), sg.InputText('', key='data_nasc')],
            [sg.Text('Data de contratação:', size=(15, 1)), sg.InputText('', key='data_inicio')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Controle de Funcionário', layout, element_justification='c')
        event, values = self.__window.Read()
        values['nome'] = values['nome'].title()
        values['CPF'] = values['CPF'][:3] + '.' + values['CPF'][3:6] + '.' + values['CPF'][6:9] + '-' + values['CPF'][9:]
        values['data_nasc'] = date(int(values['data_nasc'][4:]), int(values['data_nasc'][2:4]), int(values['data_nasc'][:2]))
        values['data_inicio'] = date(int(values['data_inicio'][4:]), int(values['data_inicio'][2:4]), int(values['data_inicio'][:2]))

        self.__window.Close()
        return values
