
from PySide6.QtWidgets import QApplication
import sys
from controller.acesso_controller import AcessoController

if __name__ == "__main__":
    app = QApplication(sys.argv)
    controller = AcessoController()
    controller.run()
    sys.exit(app.exec())
