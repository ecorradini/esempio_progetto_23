import sys
from PyQt6.QtWidgets import QApplication

from home.VistaHome import VistaHome

if __name__ == '__main__':
    app = QApplication(sys.argv)
    vistahome = VistaHome()
    vistahome.show()
    sys.exit(app.exec())
