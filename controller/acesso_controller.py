from PySide6.QtWidgets import QFileDialog
from view.acesso_view import AcessoView
from model.acesso_model import AcessoModel

class AcessoController:
    def __init__(self):
        self.model = AcessoModel()
        self.view = AcessoView()

        self.view.adicionar_button.clicked.connect(self.adicionar_registro)
        self.view.importar_button.clicked.connect(self.importar_excel)
        self.view.exportar_button.clicked.connect(self.exportar_excel)
        self.view.excluir_button.clicked.connect(self.excluir_selecionado)
        self.view.editar_button.clicked.connect(self.editar_selecionado)
        self.view.buscar_button.clicked.connect(self.buscar_cpf)
        self.view.carregar_tabela(self.model.carregar_dados())


    def run(self):
        self.view.show()

    def adicionar_registro(self):
        dados = self.view.get_form_data()

        # Verifica se todos os campos estão preenchidos
        if any(str(campo).strip() == "" for campo in dados[:-1]):  # ignora o campo Data/Hora
            self.view.mostrar_mensagem("Por favor, preencha todos os campos antes de adicionar.")
            return

        self.model.adicionar(dados)
        self.view.adicionar_na_tabela(dados)
        self.view.limpar_formulario()

    def importar_excel(self):
        arquivo, _ = QFileDialog.getOpenFileName(
        None, "Importar Excel", "", "Arquivos Excel (*.xlsx)"
    )
        if arquivo:
            df = self.model.importar(arquivo)
            self.view.carregar_tabela(df)

    def exportar_excel(self):
        arquivo, _ = QFileDialog.getSaveFileName(
        None, "Exportar Excel", "", "Arquivos Excel (*.xlsx)"
    )
        if arquivo:
            df = self.view.obter_dados_tabela()
            self.model.exportar(arquivo, df)

    def buscar_cpf(self):
        cpf = self.view.search_input.text()
        if not self.view.buscar_por_cpf(cpf):
            print("CPF não encontrado.")

    def excluir_selecionado(self):
        row = self.view.table.currentRow()  # Obtém a linha selecionada
        if row >= 0:  # Verifica se a linha selecionada é válida (se for -1, nenhuma linha foi selecionada)
            cpf_item = self.view.table.item(row, 1)  # Coluna 1 é onde o CPF está
            if cpf_item:  # Verifica se o item de CPF realmente existe
                cpf = cpf_item.text()  # Extrai o CPF do item
                self.model.remover(cpf)  # Remove o CPF do modelo (Excel)
                # Recarrega a tabela com os dados atualizados
                self.view.carregar_tabela(self.model.carregar_dados())  
            else:
                self.view.mostrar_mensagem("Erro: Não foi possível acessar o CPF dessa linha.")
        else:
            self.view.mostrar_mensagem("Por favor, selecione uma linha para excluir.")

    def editar_selecionado(self):
        row = self.view.table.currentRow()
        if row < 0:
            self.view.mostrar_mensagem("Selecione uma linha para editar.")
            return

        # Captura o CPF da linha antes da edição
        cpf_item = self.view.table.item(row, 1)
        if not cpf_item:
            self.view.mostrar_mensagem("Erro ao acessar o CPF.")
            return

        self.cpf_em_edicao = cpf_item.text()  # Guardamos para atualizar depois

        # Preenche os campos com os dados da linha
        if self.view.preencher_formulario_com_linha():
            self.view.adicionar_button.setEnabled(False)
            self.view.excluir_button.setEnabled(False)
            self.view.importar_button.setEnabled(False)
            self.view.exportar_button.setEnabled(False)
            self.view.editar_button.setText("Salvar Alterações")
            self.view.editar_button.clicked.disconnect()
            self.view.editar_button.clicked.connect(self.salvar_edicao)


    def salvar_edicao(self):
        novos_dados = self.view.get_form_data()

        if any(str(campo).strip() == "" for campo in novos_dados[:-1]):
            self.view.mostrar_mensagem("Por favor, preencha todos os campos.")
            return

        print(f"Atualizando CPF antigo: {self.cpf_em_edicao} com: {novos_dados}")

        self.model.atualizar(self.cpf_em_edicao, novos_dados)
        self.view.carregar_tabela(self.model.carregar_dados())
        self.view.limpar_formulario()

        # Resetar botão editar
        self.view.editar_button.setText("Editar Selecionado")
        self.view.editar_button.clicked.disconnect()
        self.view.editar_button.clicked.connect(self.editar_selecionado)

        self.view.adicionar_button.setEnabled(True)
        self.view.excluir_button.setEnabled(True)
        self.view.importar_button.setEnabled(True)
        self.view.exportar_button.setEnabled(True)






