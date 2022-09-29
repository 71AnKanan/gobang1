from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys


# 创建第一个窗口
class mainwindow(QMainWindow):
    def __init__(self):
        super(mainwindow, self).__init__()
        # 设置窗口标题
        self.setWindowTitle('这里是阳阳的天下')
        # 设置标签
        label = QLabel('欢迎来到阳阳的世界')
        # 将标签显示在窗口中央
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)
        # 设置大小
        self.resize(300, 600)
        # 创建布局
        layout = QVBoxLayout()
        # 创建按钮
        for i in range(5):
            button = QPushButton(str(i))
            #绑定槽函数
            button.pressed.connect(lambda x=i:self.mybutton(x))
            # 将按钮添加到布局里面
            layout.addWidget(button)
        # 创建一个部件
        weight = QWidget()
        # 将布局添加到部件里面
        weight.setLayout(layout)
        # 将部件添加到窗口
        self.setCentralWidget(weight)

    # 槽函数
    def mybutton(self, n):
        print(f'这是第{n}个阳阳')



# 创建应用实例，通过sys.argv传入命令行参数
app = QApplication(sys.argv)
# 创建窗口
window = mainwindow()
# 显示窗口
window.show()
# 执行应用，进入事件循环
app.exec_()
