# from main import Ui_MainWindow
from PyQt6 import QtWidgets
import sys  
import main, mahoa, giaima
import Ceasar.MaHoaCeasar as MaHoaCeasar, Ceasar.GiaiMaCeasar as GiaiMaCeasar
import Vignere.MaHoaVignere as MaHoaVignere , Vignere.GiaiMaVignere as GiaiMaVignere
import Trithemius.MaHoaTrithemius as MaHoaTrithemius, Trithemius.GiaiMaTrithemius as GiaiMaTrithemius
import ChuyenVi.MaHoaChuyenVi as MaHoaChuyenVi, ChuyenVi.GiaiMaChuyenVi as GiaiMaChuyenVi
import ChuyenViNhieuDong.MaHoaChuyenViNhieuDong as MaHoaChuyenViNhieuDong, ChuyenViNhieuDong.GiaiMaChuyenViNhieuDong as GiaiMaChuyenViNhieuDong
import Belasco.MaHoaBelasco as MaHoaBelasco, Belasco.GiaiMaBelasco as GiaiMaBelasco

ui=''
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

def mainUI():
    global ui 
    ui = main.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.btnMaHoa.clicked.connect(mahoa_UI)
    ui.btnGiaiMa.clicked.connect(giaima_UI)
    MainWindow.show()

def mahoa_UI():
    global ui 
    ui = mahoa.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.btnback.clicked.connect(mainUI)
    ui.btnCaesar.clicked.connect(mahoaCeasar_UI)
    ui.btnVigenere.clicked.connect(maHoaVignere_UI)
    ui.btnTrithemius.clicked.connect(mahoatrithemius_UI)
    ui.btnBelasco.clicked.connect(mahoabelasco_UI)
    ui.btnChuyenViHaiDong.clicked.connect(mahoachuyenvi_UI)
    ui.btnChuyenViNhieuDong.clicked.connect(mahoachuyenvinhieudong_UI)
    MainWindow.show()

def giaima_UI():
    global ui 
    ui = giaima.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.btnback.clicked.connect(mainUI)
    ui.btnCaesar.clicked.connect(giaiMaCeasar_UI)
    ui.btnVigenere.clicked.connect(giaimaVignere_UI)
    ui.btnTrithemius.clicked.connect(giaimatrithemius_UI)
    ui.btnBelasco.clicked.connect(giaimabelasco_UI)
    ui.btnChuyenViHaiDong.clicked.connect(giaimachuyenvi_UI)
    ui.btnChuyenViNhieuDong.clicked.connect(giaimachuyenvinhieudong_UI)
    MainWindow.show()


def mahoaCeasar_UI():
    global ui 
    ui = MaHoaCeasar.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.btnBack.clicked.connect(mahoa_UI)
    ui.btnGiaiMa.clicked.connect(giaiMaCeasar_UI)
    MainWindow.show()


def giaiMaCeasar_UI():
    global ui 
    ui = GiaiMaCeasar.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.btnBack.clicked.connect(mahoaCeasar_UI)


def maHoaVignere_UI():
    global ui
    ui = MaHoaVignere.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.btnBack.clicked.connect(mahoa_UI)
    ui.btnGiaiMaVignere.clicked.connect(giaimaVignere_UI)

def giaimaVignere_UI():
    global ui
    ui = GiaiMaVignere.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.btnBack.clicked.connect(giaima_UI)
    ui.btnMaHoaVignere.clicked.connect(maHoaVignere_UI)


def mahoatrithemius_UI():
    global ui
    ui = MaHoaTrithemius.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.btnBack.clicked.connect(mahoa_UI)
    ui.btnGiaiMaTrithemius.clicked.connect(giaimatrithemius_UI)

def giaimatrithemius_UI():
    global ui
    ui = GiaiMaTrithemius.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.btnBack.clicked.connect(giaima_UI)
    ui.btnMaHoaTrithemius.clicked.connect(mahoatrithemius_UI)


def mahoabelasco_UI():
    global ui
    ui = MaHoaBelasco.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.btnBack.clicked.connect(mahoa_UI)
    ui.btnGiaiMaBelasco.clicked.connect(giaimabelasco_UI)


def giaimabelasco_UI():
    global ui
    ui = GiaiMaBelasco.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.btnBack.clicked.connect(giaima_UI)
    ui.btnMaHoaBelasco.clicked.connect(mahoabelasco_UI)

def mahoachuyenvi_UI():
    global ui
    ui = MaHoaChuyenVi.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.btnBack.clicked.connect(mahoa_UI)
    ui.btnGiaiMaChuyenVi.clicked.connect(giaimachuyenvi_UI)

def giaimachuyenvi_UI():
    global ui
    ui = GiaiMaChuyenVi.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.btnBack.clicked.connect(giaima_UI)
    ui.btnMaHoaChuyenVi.clicked.connect(mahoachuyenvi_UI)

def mahoachuyenvinhieudong_UI():
    global ui
    ui = MaHoaChuyenViNhieuDong.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.btnBack.clicked.connect(mahoa_UI)
    ui.btnGiaiMaChuyenViNhieuDong.clicked.connect(giaimachuyenvinhieudong_UI)

def giaimachuyenvinhieudong_UI():
    global ui
    ui = GiaiMaChuyenViNhieuDong.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.btnBack.clicked.connect(giaima_UI)
    ui.btnMaHoaChuyenViNhieuDong.clicked.connect(mahoachuyenvinhieudong_UI)

mainUI() 
sys.exit(app.exec())