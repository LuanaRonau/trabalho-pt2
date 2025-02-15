from telas.tela_filial import TelaFilial
from entidade.filial import Filial
from controladores.controlador_gerente_esp import ControladorGerenteEsp
from controladores.controlador_fun_comum_esp import ControladorFunComumEsp
from controladores.controlador_fun_comum import ControladorFunComum
from controladores.controlador_gerente import ControladorGerente


class ControladorFilial:

    def __init__(self, controlador_sistema, filial: Filial):
        self.__controlador_sistema = controlador_sistema
        self.__controlador_contrato = self.__controlador_sistema.controlador_contrato
        self.__controlador_gerente = ControladorGerente(controlador_sistema)
        self.__controlador_fun_comum = ControladorFunComum(controlador_sistema)
        self.__filial = filial
        self.__tela_filial = TelaFilial()

    @property
    def filial(self):
        return self.__filial

    @property
    def controlador_sistema(self):
        return self.__controlador_sistema
    
    @property
    def controlador_gerente(self):
        return self.__controlador_gerente
    
    @property
    def controlador_fun_comum(self):
        return self.__controlador_fun_comum

    def inicializa_sistema(self):
        lista_opcoes = {1: self.controlador_fun_comum_esp, 2: self.controlador_gerente_esp,
                        3: self.modificar_dados, 4: self.acessar_contratos,
                        5: self.listar_fun_ativos, 0: self.retornar}

        while True:
            opcao_escolhida = self.__tela_filial.mostra_opcoes()
            print("\nfun_comum:", len(self.__controlador_fun_comum.fun_comum_dao.get_all()))
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

    def controlador_fun_comum_esp(self):
        ControladorFunComumEsp(self, self.__filial.funcionarios).inicializa_sistema()

    def controlador_gerente_esp(self):
        ControladorGerenteEsp(self, self.__filial.gerente).inicializa_sistema()

    def modificar_dados(self):
        opcao = self.__tela_filial.menu_modificacao()
        if opcao == 1:
            while True:
                cep_novo = self.__tela_filial.le_cep()
                if self.__controlador_sistema.checagem_repeticao_cep(cep_novo):
                    break
            self.__filial.cep = cep_novo
            self.__controlador_sistema.filial_dao.update(self.__filial)

        elif opcao == 2:
            while True:
                cidade_nova = self.__tela_filial.le_cidade()
                if self.__controlador_sistema.checagem_repeticao_cidade(cidade_nova):
                    break
            self.__filial.cidade = cidade_nova
            self.__controlador_sistema.filial_dao.update(self.__filial)

        elif opcao == 0:
            return

    def acessar_contratos(self):
        todos_os_contratos = self.__controlador_contrato.contrato_dao.get_all()
        contratos = []
        for contrato in todos_os_contratos:
            if contrato.filial == self.__filial:
                contratos.append(contrato)
        self.__controlador_contrato.listar_contrato_auto(contratos)

    def listar_fun_ativos(self):
        lista_fun = self.__filial.funcionarios
        funcionarios_a_listar = [self.__filial.gerente]
        if len(lista_fun) > 0:
            for fun in lista_fun:
                if fun.atividade is True:
                    funcionarios_a_listar.append(fun)
            self.__tela_filial.listagem(funcionarios_a_listar)
        else:
            self.__tela_filial.mostra_mensagem('Lista de funcionários comuns vazia.')

    def retornar(self):
        self.__controlador_sistema.inicializa_sistema()
