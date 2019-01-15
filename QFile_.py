from PyQt5.QtCore import QFile, QIODevice


if __name__ == '__main__':
    A = QFile('tips.txt')
    A.open(QIODevice.ReadWrite)
    A.rollbackTransaction()
    print(A.readAll())