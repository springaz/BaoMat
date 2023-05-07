from PyQt6.QtWidgets import QFileDialog
from PyQt6.QtCore import pyqtSlot
import sys

# get path
def pathFile():
    file_path, _ = QFileDialog.getOpenFileName(
        None,  # Parent window
        "Open file",  # Dialog title
        "",  # Directory to start in
        "Text Files (*.txt)"  # File filter
    )
    return file_path


# read content
def openFileDialog(file_path):
    with open(file_path, "r", encoding='utf-8') as file:
        contents = file.read()
    return contents

# def saveFile(data):
#     file_path, _ = QFileDialog.getSaveFileName(
#         None,  # Parent window
#         "Save file",  # Dialog title
#         "",  # Directory to start in
#         "Text Files (*.txt)"  # File filter
#     )

#     if file_path:
#         with open(file_path, 'w') as f:
#             f.write(data)



