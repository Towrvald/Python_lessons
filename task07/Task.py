import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget


class HarmonicAnimation(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 800, 400)  # Изменение высоты окна
        central_widget = QWidget()  # cоздаём экзамепляр класса
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

        self.button = QPushButton("Start animation", self)
        self.button.clicked.connect(self.start_animation)  # создаём сигнал
        layout.addWidget(self.button)

        self.amplitude = 1
        self.omega = 2 * np.pi
        self.time = np.linspace(0, 2 * np.pi, 100)
        self.line_sin, = self.ax.plot([], [], label='Sin')
        self.line_cos, = self.ax.plot([], [], label='Cos')
        self.ax.set_xlabel('Время')
        self.ax.set_ylabel('Амплитуда')
        self.ax.legend()

    def update_plot(self, phase):
        x_sin = self.amplitude * np.sin(self.omega * self.time + phase)
        x_cos = self.amplitude * np.cos(self.omega * self.time + phase)
        self.line_sin.set_data(self.time, x_sin)
        self.line_cos.set_data(self.time, x_cos)
        self.ax.set_xlim(0, 2 * np.pi)
        self.ax.set_ylim(-1.5, 1.5)
        return self.line_sin, self.line_cos

    def start_animation(self):  # событие для сигнала нажатия кнопки
        self.animation = FuncAnimation(self.figure, self.update_plot, frames=np.linspace(0, 2 * np.pi, 100),
                                       blit=True, interval=100)
        self.canvas.draw()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = HarmonicAnimation()
    window.show()
    sys.exit(app.exec_())