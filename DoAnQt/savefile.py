from PyQt6.QtWidgets import QFileDialog
 


def saveFile(data):
    file_path, _ = QFileDialog.getSaveFileName(
        None,  # Parent window
        "Save file",  # Dialog title
        "",  # Directory to start in
        "Text Files (*.txt)"  # File filter
    )

    if file_path:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(data)   

