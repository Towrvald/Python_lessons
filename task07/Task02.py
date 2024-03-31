import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider, Button


# Я настрадался в PyQt, поэтому всё переписал на matplotlib
class HarmonicAnimation:
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        self.canvas = self.fig.canvas

        self.amplitude_slider_ax = plt.axes([0.2, 0.15, 0.65, 0.03])
        self.amplitude_slider = Slider(self.amplitude_slider_ax, 'Amplitude', 0, 10, valinit=5)

        self.phase_slider_ax = plt.axes([0.2, 0.1, 0.65, 0.03])
        self.phase_slider = Slider(self.phase_slider_ax, 'Phase', 0, 360, valinit=0)

        self.frequency_slider_ax = plt.axes([0.2, 0.05, 0.65, 0.03])
        self.frequency_slider = Slider(self.frequency_slider_ax, 'Frequency', 1, 10, valinit=5)

        self.noise_slider_ax = plt.axes([0.2, 0.2, 0.65, 0.03])
        self.noise_slider = Slider(self.noise_slider_ax, 'Noise Amplitude', 0, 2, valinit=0)

        self.button_ax = plt.axes([0.8, 0.05, 0.1, 0.1])
        self.button = Button(self.button_ax, 'Start animation')
        self.button.on_clicked(self.start_animation)

        self.amplitude = 1
        self.phase = 0
        self.frequency = 2 * np.pi
        self.time = np.linspace(0, 2 * np.pi, 100)
        self.line_sin, = self.ax.plot([], [], label='Sin')
        self.line_cos, = self.ax.plot([], [], label='Cos')
        self.ax.set_xlabel('Time')
        self.ax.set_ylabel('Amplitude')
        self.ax.set_title('Harmonic Oscillation Animation')
        self.ax.legend()

        plt.subplots_adjust(left=0.1, right=0.85, bottom=0.3, top=0.9)

    def update_plot(self, frame):
        self.ax.lines.clear()
        phase = self.phase + frame * np.pi / 50
        x_sin = self.amplitude * np.sin(self.frequency * self.time + phase)
        x_cos = self.amplitude * np.cos(self.frequency * self.time + phase)
        noise_amplitude = self.noise_slider.val
        noise = np.random.normal(0, noise_amplitude, self.time.shape)
        x_sin += noise
        x_cos += noise
        self.line_sin, = self.ax.plot(self.time, x_sin, label='Sin')
        self.line_cos, = self.ax.plot(self.time, x_cos, label='Cos')
        self.ax.set_xlim(0, 2 * np.pi)
        self.ax.set_ylim(-1.5 * self.amplitude, 1.5 * self.amplitude)

    def start_animation(self, event):
        self.amplitude = self.amplitude_slider.val
        self.phase = np.deg2rad(self.phase_slider.val)
        self.frequency = self.frequency_slider.val * np.pi
        self.animation = FuncAnimation(self.fig, self.update_plot, frames=100, interval=50)
        plt.show()


if __name__ == '__main__':
    animation = HarmonicAnimation()
    plt.show()
