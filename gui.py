import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap

import pygame
import pygame.camera

pygame.init()
pygame.camera.init()

cam = pygame.camera.Camera("/dev/video0", (width, height))
window = pygame.display.set_mode((width, height), pygame.RESIZABLE)
cam.start()

# https://pythonspot.com/gui/

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'EZ Recycle 1.5'
        self.left = 100
        self.top = 100
        self.width = 1024
        self.height = 960
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.label = QLabel('eAEST', self)
        
        # Create widget
        label = QLabel(self)
        #pixmap = QPixmap('new.jpg')
        image = cam.get_image()
        window.blit(image, (0, 0))
        pixmap = pygame.display.update()

        label.setPixmap(pixmap)
        #self.resize(pixmap.width(),pixmap.height())
        
        self.show()
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())