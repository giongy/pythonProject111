from PyQt5 import QtGui


class mainfunctions:
    def prova(self, i):
        tit = self.main_tab.currentWidget().objectName().title()
        if tit == 'Causali':
            esempio = ["casa", "trasporti"]
            self.model = QtGui.QStandardItemModel()
            self.listView_Gruppi.setModel(self.model)

            for ii in esempio:
                item = QtGui.QStandardItem(ii)
                self.model.appendRow(item)
        print("cambiato" + str(i) + tit+" ")