# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 22:53:33 2016

@author: s.dossantos
"""
import socket, sys, threading
import clientSensorView

th_E = "" #global variable

class ThreadEmission(threading.Thread):
    """objet thread gérant l'émission des messages"""
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.connexion = conn           # réf. du socket de connexion
        
    def send(self, message_emis):
        self.connexion.send(message_emis)

def start(host, port):
    # Établissement de la connexion :
    connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        connexion.connect((str(host), int(port)))
    except socket.error:
        print "La connexion a échoué."
        sys.exit()    
    print "Connexion établie avec le serveur."
                
    # Emission des messages :
    global th_E
    th_E = ThreadEmission(connexion)
    th_E.start()

def stop():
    th_E._Thread__stop()
    print "Client arrêté. Connexion interrompue."
    th_E.connexion.close()

def showGui():
    QtGuiC.show()

def increment(lineEdit):
    """simulation de la position du lidar, pushButton '+' gui"""
    lineEdit.setText(str(int(lineEdit.text())+1))
    
def decrement(lineEdit):
    """simulation de la position du lidar, pushButton '-' gui"""
    lineEdit.setText(str(int(lineEdit.text())-1))
    
def sendLidarPosition():
    """Fabrication de la trame à envoyer"""
    message = (
        str(view.lineEditX.text()) + " " + 
        str(view.lineEditY.text()) + " " +
        str(view.lineEditZ.text()) + " " +
        str(view.lineEditA.text()) + " " +
        str(view.lineEditB.text()) + " " +
        str(view.lineEditC.text()) )
    th_E.send(message)
    
def initSignals():
    """Initialisation des différents signaux qt"""
    view.pushButtonXP.clicked.connect(lambda: increment(view.lineEditX))
    view.pushButtonYP.clicked.connect(lambda: increment(view.lineEditY))
    view.pushButtonZP.clicked.connect(lambda: increment(view.lineEditZ))
    view.pushButtonAP.clicked.connect(lambda: increment(view.lineEditA))
    view.pushButtonBP.clicked.connect(lambda: increment(view.lineEditB))
    view.pushButtonCP.clicked.connect(lambda: increment(view.lineEditC))
    
    view.pushButtonXM.clicked.connect(lambda: decrement(view.lineEditX))
    view.pushButtonYM.clicked.connect(lambda: decrement(view.lineEditY))
    view.pushButtonZM.clicked.connect(lambda: decrement(view.lineEditZ))
    view.pushButtonAM.clicked.connect(lambda: decrement(view.lineEditA))
    view.pushButtonBM.clicked.connect(lambda: decrement(view.lineEditB))
    view.pushButtonCM.clicked.connect(lambda: decrement(view.lineEditC))
    
    view.pushButtonSend.clicked.connect(sendLidarPosition)
    
    view.pushButtonConnect.clicked.connect(lambda: start(view.lineEditIP.text(), view.lineEditPort.text()))
    view.pushButtonDeconnect.clicked.connect(stop)

if __name__ == '__main__':
    ## GUI 
    app = clientSensorView.QtGui.QApplication(sys.argv)
    app.setStyle(clientSensorView.QtGui.QStyleFactory.create("Plastique"))
    QtGuiC = clientSensorView.QtGui.QMainWindow()
    view = clientSensorView.Ui_Sensor()
    view.setupUi(QtGuiC)
    ##
    initSignals() # init signaux qt
    showGui()     # show gui
    
    app.exec_()