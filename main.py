from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
)

from funzioni_tab import mainfunctions
from queries import *
from sqlHelper import createConnection
from untitled import Ui_MainWindow


class Contacts(QMainWindow, Ui_MainWindow, mainfunctions):
    def __init__(self, *args, obj=None, **kwargs):
        super(Contacts, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.main_tab.setCurrentIndex(0)
        self.main_tab.currentChanged.connect(self.prova)
        self.listView_Gruppi.clicked.connect(self.clicked_gruppi_item)

    def clicked_gruppi_item(self, i):

        it = self.model.itemFromIndex(i)
        print(" "+"cliccato: "+str(it.text()))

app = QApplication(sys.argv)
if not createConnection():
    sys.exit(1)
create_initial_tables()  # Creo tabelle iniziali "IF NOT EXISTS"
win = Contacts()
win.show()
sys.exit(app.exec_())
