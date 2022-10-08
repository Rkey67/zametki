#начни тут создавать приложение с умными заметками
import json
from PyQt5.QtCore import Qt 
from random import shuffle
from PyQt5.QtWidgets import  QWidget, QApplication, QListWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton, QMessageBox, QGroupBox, QButtonGroup, QLineEdit, QTextEdit, QInputDialog
notes = {
    "Добро пожаловать":{"Текст":"Это самое лучшее приложение для заметок в мире!",
    "теги":['добро','инструкция']}
}

'''with open("notes_data.json","w") as file:
    json.dump(notes, file, sort_keys=True)    '''  



app = QApplication([])
main_win = QWidget()
main_win.resize(800,500)
main_win.setWindowTitle("Умные заметки")

field_text = QTextEdit()
 #текстзаметки


field_tag1 = QListWidget()
field_tag = QListWidget()

text = QLabel("Текст")
spisok = QLabel("Список заметок")
spisok2 = QLabel("Список тегов")

vvod = QLineEdit()
vvod.setPlaceholderText("Введите тег")


CreateButton = QPushButton('Создать заметку')
deleteButton = QPushButton('Удалить заметку')
saveButton = QPushButton('Сохранить заметку')
addButton = QPushButton('Добавить к заметке')
finedButton = QPushButton('Искать заметки по тегу')
otkrepitButton = QPushButton('Открепить заметку')

list_tags = QListWidget()

lineglav = QHBoxLayout()
LineV1 = QVBoxLayout()
LineV2 = QVBoxLayout()
LineH1 = QHBoxLayout()
LineH2 = QHBoxLayout()
LineH3 = QHBoxLayout()
LineH4 = QHBoxLayout()

LineV1.addWidget(text)
LineV1.addWidget(field_text)

LineV2.addWidget(spisok)
LineV2.addWidget(field_tag1)

LineV2.addLayout(LineH1)
LineV2.addLayout(LineH2)

LineV2.addWidget(spisok2)
LineV2.addWidget(field_tag)

LineV2.addWidget(vvod)


LineV2.addLayout(LineH3)
LineV2.addLayout(LineH4)

lineglav.addLayout(LineV1)
lineglav.addLayout(LineV2)





LineH1.addWidget(CreateButton)
LineH1.addWidget(deleteButton)
LineH2.addWidget(saveButton)






LineH3.addWidget(addButton)
LineH3.addWidget(otkrepitButton)
LineH4.addWidget(finedButton)





def show_note():
    name = field_tag1.selectedItems()[0].text()
    field_text.setText(notes[name]["Текст"])
    field_tag.clear()
    field_tag.addItems(notes[name]["теги"])


field_tag1.itemClicked.connect(show_note)


def add_note():
    note_name, ok = QInputDialog.getText(main_win,"Добавить заметку", "Название заметки:")
    if ok and note_name != '':
        notes[note_name] = {"Текст":'',"теги":[]}
        field_tag1.addItem(note_name)
        field_tag.addItems(notes[note_name]["теги"]) 

def save_note():
    if field_tag1.selectedItems():
        key = field_tag1.selectedItems()[0].text()
        notes[key]["Текст"] = field_text.toPlainText()
        with open("notes_data.json", "w", encoding = 'utf-8') as file:     
            json.dump(notes,file,sort_keys = True)

def del_notes():
    if field_tag1.selectedItems():
        key = field_tag1.selectedItems()[0].text()
        del notes[key]
        field_tag1.clear()
        field_tag.clear()
        field_text.clear()
        field_tag1.addItems(notes)
        with open("notes_data.json", "w", encoding = 'utf-8') as file:     
            json.dump(notes,file,sort_keys = True)
        print(notes)



def add_tag():
    if field_tag1.selectedItems():
        key = field_tag1.selectedItems()[0].text()
        tag = vvod.text()
        if not tag in notes[key]["теги"]:
            notes[key]["теги"].append(tag)
            field_tag.addItem(tag)
            vvod.clear()
        with open("notes_data.json","w") as file:
            json.dump(notes, file, sort_keys=True)
            print(notes)
    else:
        print("Заметка для добавления тега не выбрана!")


def del_tag():
    if field_tag1.selectedItems():
        key = field_tag1.selectedItems()[0].text()
        tag = field_tag.selectedItems()[0].text()
        notes[key]["теги"].remove(tag)
        field_tag.clear()
        field_tag.addItems(notes[key]["теги"])
        with open("notes_data.json","w") as file:
            json.dump(notes, file, sort_keys=True)        


def search_tag():
    tag = vvod.text()
    if finedButton.text() == "Искать заметки по тегу" and tag:
        notes_filtered = {} 
        for note in notes:
            if tag in notes[note]["теги"]:
                notes_filtered[note]=notes[note]
        finedButton.setText("Сбросить поиск")
        field_tag.clear()
        field_tag1.clear()
        field_tag1.addItems(notes_filtered)
    elif finedButton.text() == "Сбросить поиск":
        vvod.clear()
        field_tag.clear()
        field_tag1.clear()
        field_tag1.addItems(notes)
        finedButton.setText("Искать заметки по тегу")
    else:
        pass






CreateButton.clicked.connect(add_note)
deleteButton.clicked.connect(del_notes)
saveButton.clicked.connect(save_note)


addButton.clicked.connect(add_tag) 
otkrepitButton.clicked.connect(del_tag)
finedButton.clicked.connect(search_tag)




main_win.setLayout(lineglav)

main_win.show()
with open("notes_data.json", "r", encoding = 'utf-8') as file:
    notes = json.load(file)
field_tag.addItems(notes)
app.exec()