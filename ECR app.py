import sys
from tkinter import *   
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
import ctypes

myappid = 'com.kl5is.ecrapp' 
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
class Window(QMainWindow):
 
    def __init__(self):
        super(Window,self).__init__()
         
        
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://ko4uyj.com/ecr_app/main.php'))
        self.setCentralWidget(self.browser)
        self.showMaximized()
        self.setWindowIcon(QtGui.QIcon('logo.ico'))

        navbar = QToolBar()
        self.addToolBar(navbar)
       
        AboutBtn = QAction('About',self)
        AboutBtn.triggered.connect(self.About)
        navbar.addAction(AboutBtn)
    
        

        homeBtn = QAction('Home',self)
        homeBtn.triggered.connect(self.home)
        navbar.addAction(homeBtn)

        

        print(self.browser.url().toString())
         
        
    def home(self):
        self.browser.setUrl(QUrl('http://ko4uyj.com/ecr_app/main.php'))
    def About(self):
        win = Tk()  
        win.title('ERC About')
        win.geometry("340x410")
        win.iconbitmap('logo.ico')
  

        header = Label(win, text = "East Coast Reflector Desktop app v1.3").place(x = 30,y = 10)
        header = Label(win, text = "Source page programed by Caleb B Harrell (KO4UYJ)").place(x = 30,y = 50)
        header = Label(win, text = "Windows Port programed by Asa J Lorentzen (KL5IS)").place(x = 30,y = 70)
        header = Label(win, text = "Page source:").place(x = 30,y = 110)
        header = Label(win, text = "http://ko4uyj.com/ecr_app/main.php").place(x = 30,y = 130)
        header = Label(win, text = "The port source code is avalable at:").place(x = 30,y = 160)
        header = Label(win, text = "https://github.com/KL5IS/East-Coast-Reflector-app-windows-port").place(x = 30,y = 180)
        header = Label(win, text = "Port relese date: 5/9/2022").place(x = 30,y = 220)
        header = Label(win, text = "Contact emails:").place(x = 30,y = 250)
        header = Label(win, text = "Asa, for port development and installer maintenance:").place(x = 30,y = 290)
        header = Label(win, text = "KL5IS@protonmail.com").place(x = 30,y = 310)
        header = Label(win, text = "Caleb, for page development and distribution:").place(x = 30,y = 350)
        header = Label(win, text = "KO4UYJ@gmail.com").place(x = 30,y = 370)
        win.mainloop()  


        

MyApp = QApplication(sys.argv)
QApplication.setApplicationName('ERC app')
window = Window()
MyApp.exec_()
