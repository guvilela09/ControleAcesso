from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTableWidget,
    QTableWidgetItem, QMessageBox
)
from PySide6.QtCore import Qt
from datetime import datetime

class AcessoView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Controle de Acesso")
        self.setGeometry(200, 100, 950, 500)

        layout = QVBoxLayout()
        form_layout = QHBoxLayout()

        self.inputs = [QLineEdit() for _ in range(5)]
        labels = ["Nome", "CPF", "RG", "Empresa", "Responsável"]

        for i, label in enumerate(labels):
            form_layout.addWidget(QLabel(label))
            form_layout.addWidget(self.inputs[i])

        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Buscar por CPF...")
        self.buscar_button = QPushButton("Buscar")

        self.adicionar_button = QPushButton("Adicionar")
        self.excluir_button = QPushButton("Excluir Selecionado")
        self.editar_button = QPushButton("Editar Selecionado")
        self.importar_button = QPushButton("Importar Excel")
        self.exportar_button = QPushButton("Exportar Excel")

        # Atualizado: 6 colunas (com Data/Hora)
        self.table = QTableWidget(0, 6)
        self.table.setHorizontalHeaderLabels(labels + ["Data/Hora"])
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)

        layout.addLayout(form_layout)
        layout.addWidget(self.adicionar_button)
        layout.addWidget(self.excluir_button)
        layout.addWidget(self.editar_button)


        search_layout = QHBoxLayout()
        search_layout.addWidget(self.search_input)
        search_layout.addWidget(self.buscar_button)
        layout.addLayout(search_layout)

        layout.addWidget(self.table)
        layout.addWidget(self.importar_button)
        layout.addWidget(self.exportar_button)

        self.setLayout(layout)

    def get_form_data(self):
        dados = [inp.text() for inp in self.inputs]
        # Mantém a data atual da linha selecionada, se houver
        row = self.table.currentRow()
        if row >= 0 and self.table.item(row, 5):
            data_hora = self.table.item(row, 5).text()
        else:
            data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        dados.append(data_hora)
        return dados

    def limpar_formulario(self):
        for inp in self.inputs:
            inp.clear()

    def adicionar_na_tabela(self, dados):
        row = self.table.rowCount()
        self.table.insertRow(row)
        for col, valor in enumerate(dados):
            item = QTableWidgetItem(str(valor))
            item.setFlags(item.flags() & ~Qt.ItemIsEditable)
            self.table.setItem(row, col, item)


    def carregar_tabela(self, df):
        self.table.setRowCount(0)
        for _, row in df.iterrows():
            self.adicionar_na_tabela(row.tolist())



    def obter_dados_tabela(self):
        dados = []
        for row in range(self.table.rowCount()):
            linha = []
            for col in range(self.table.columnCount()):
                item = self.table.item(row, col)
                linha.append(item.text() if item else "")
            dados.append(linha)
        from pandas import DataFrame
        return DataFrame(dados, columns=["Nome", "CPF", "RG", "Empresa", "Responsável", "Data/Hora"])

    
    def excluir_selecionado(self):
        row = self.table.currentRow()
        if row >= 0:
            self.table.removeRow(row)

    def preencher_formulario_com_linha(self):
        row = self.table.currentRow()
        if row >= 0:
            for i in range(5):  # Nome, CPF, RG, Empresa, Responsável
                item = self.table.item(row, i)
                self.inputs[i].setText(item.text() if item else "")
            return True
        return False


    def buscar_por_cpf(self, cpf):
        for row in range(self.table.rowCount()):
            item = self.table.item(row, 1)  # coluna CPF
            if item and item.text() == cpf:
                self.table.selectRow(row)
                return True
        return False

    def mostrar_mensagem(self, texto):
        QMessageBox.warning(self, "Aviso", texto)