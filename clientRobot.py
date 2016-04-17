# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 22:53:33 2016

@author: s.dossantos
"""
import socket, sys, threading
import clientRobotView
import time
import Numpy

th_R = "" #global variable

class ThreadReception(threading.Thread):
    """objet thread gérant la réception des messages"""
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.connexion = conn           # réf. du socket de connexion
        
    def run(self):
        while 1:
            message_recu = self.connexion.recv(1024)
            print "*" + message_recu + "*"
            view.textEditFromServer.emit(clientRobotView.QtCore.SIGNAL("add_post(QString)"), message_recu)
        self._Thread__stop()
        print "Client arrêté. Connexion interrompue."
        self.connexion.close()
    
def add_post(message_recu):
    """display on GUI"""
    view.textEditFromServer.setText((message_recu))

def start(host, port):
    # Établissement de la connexion :
    connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        connexion.connect((str(host), int(port)))
    except socket.error:
        print "La connexion a échoué."
        sys.exit()    
    print "Connexion établie avec le serveur."
    time.sleep(2)
    # la réception des messages :
    global th_R
    th_R = ThreadReception(connexion)
    th_R.start()

def stop():
    th_R._Thread__stop()
    print "Client arrêté. Connexion interrompue."
    th_R.connexion.close()

def showGui():
    QtGuiC.show()
    
def initSignals():
    """Initialisation des signaux Qt"""
    view.textEditFromServer.connect(view.textEditFromServer,clientRobotView.QtCore.SIGNAL("add_post(QString)"),add_post)
    view.pushButtonConnect.clicked.connect(lambda: start(view.lineEditIP.text(), view.lineEditPort.text()))
    view.pushButtonDeconnect.clicked.connect(stop)

if __name__ == '__main__':
    ## GUI 
    app = clientRobotView.QtGui.QApplication(sys.argv)
    app.setStyle(clientRobotView.QtGui.QStyleFactory.create("Plastique"))
    QtGuiC = clientRobotView.QtGui.QMainWindow()
    view = clientRobotView.Ui_Robot()
    view.setupUi(QtGuiC)
    ##
    initSignals() #init signaux
    showGui()     #show gui   
    
    app.exec_()