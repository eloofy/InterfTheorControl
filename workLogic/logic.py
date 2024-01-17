import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import copy
import control as ct
import math


def polar_to_cartesian(radius_main, theta):
    x = []
    y = []
    for rad, th in zip(radius_main, theta):
        x.append(rad * math.cos(math.radians(th)))
        y.append(rad * math.sin(math.radians(th)))
    return x, y


class Model:
    def __init__(self, k, T, xi):
        self.w = []
        self.k = k
        self.T = T
        self.Time = 3000
        self.xi = xi
        self.w = []
        self.X0 = [0, 0]
        self.Ax = []
        self.dtt = []
        self.phi = []
        self.L = []
        self.x = []
        self.t = np.linspace(0, self.Time, 200000)

    def model(self, x, t):
        y = np.sin(self.w[-1] * t)
        a2 = self.T ** 2
        a1 = 2 * self.xi * self.T
        a0 = 1
        b0 = self.k
        dx1 = x[1]
        dx2 = 1 / a2 * (b0 * y - (a1 * x[1] + a0 * x[0]))
        return [dx1, dx2]

    def init(self):
        for i, w_data in enumerate([0.01, 0.03, 0.1, 0.3, 1, 3, 10]):
            self.w.append(w_data)
            self.x.append(odeint(self.model, self.X0, self.t, atol=1e-8, rtol=1e-8))
            self.Ax.append(max(self.x[i][:, 0]))
            self.L.append(20*np.log10(self.Ax[-1]))
            self.calc_data_graph2(i, draw_mode=False)

        self.table_data = np.array([self.Ax, self.dtt, self.phi, self.L])

        numerator = [self.k]
        denominator = [self.T ** 2, 2 * self.T * self.xi, 1]
        self.sys = ct.TransferFunction(numerator, denominator)

    def draw_graphic_one(self, ui):
        ax = ui.ui_main_window.figure.add_subplot(111)
        ax.plot(self.t, self.x[0][:, 0], 'b-', linewidth=2)
        y = np.sin(self.w[0] * self.t)
        ax.plot(self.t, y, 'g-', linewidth=2, alpha=0.5)
        ax.legend(['x(t)', 'y(t)'])
        ax.grid(True)
        ax.set_xlabel('t, c')
        ax.set_ylabel('x_i(t)')
        ax.set_title(f'ω={self.w[0]} Гц, A_x={round(self.Ax[0], 4)}')

        ui.ui_main_window.canvas.draw()

    def draw_graphic_two(self, ui):
        (X1_src,
         Xt,
         Y_src,
         X1_MAX_IDX,
         Y_MAX_IDX) = self.calc_data_graph2(0, draw_mode=True)

        ax = ui.ui_main_window.figure.add_subplot(111)

        ax.plot(Xt, X1_src / self.Ax[0], 'b-', linewidth=2)
        ax.plot(Xt, Y_src, 'g-', linewidth=2)
        ax.plot(Xt[X1_MAX_IDX], X1_src[X1_MAX_IDX] / self.Ax[0], 'bo')
        ax.plot(Xt[Y_MAX_IDX], Y_src[Y_MAX_IDX], 'go')
        ax.grid(True)
        ax.legend(['x(t) / A_x', 'y(t)'])
        ax.set_title(f'ω={self.w[0]} Гц, φ=')
        ax.set_xlabel('t, c')
        ax.set_ylabel('x_i(t) / A_x')

        ui.ui_main_window.canvas.draw()

    def draw_graphic_three(self, ui):
        # АЧХ
        ax = ui.ui_main_window.figure.add_subplot(111)
        ax.plot(self.w, self.Ax, linewidth=2)
        ax.grid(True)
        ax.set_title('График АЧХ')
        ax.set_ylabel('A(omega)')
        ax.set_xlabel('omega, Гц')

        ui.ui_main_window.canvas.draw()

    def draw_graphic_four(self, ui):
        # ФЧХ
        ax = ui.ui_main_window.figure.add_subplot(111)
        ax.plot(self.w, self.phi, linewidth=2)
        ax.grid(True)
        ax.set_title('График ФЧХ')
        ax.set_ylabel('phi(omega), град.')
        ax.set_xlabel('omega, Гц')

        ui.ui_main_window.canvas.draw()

    def draw_graphic_five(self, ui):
        # Логарифмическая АЧХ
        ax = ui.ui_main_window.figure.add_subplot(111)
        ax.semilogx(self.w, self.L, linewidth=2)
        ax.grid(True)
        ax.set_title('График логарифмической АЧХ')
        ax.set_ylabel('L(omega), дБ')
        ax.set_xlabel('omega, декады Гц')

        ui.ui_main_window.canvas.draw()


    def draw_graphic_six(self, ui):
        # ЛАЧХ И ЛФЧХ
        ax = ui.ui_main_window.figure.add_subplot(111)
        ct.bode_plot(self.sys, plot=True)

        ui.ui_main_window.canvas.draw()

    def draw_graphic_seven(self, ui):
        ax = ui.ui_main_window.figure.add_subplot(111)
        x, y = polar_to_cartesian(self.Ax, self.phi)

        # Nyquist plot
        ct.nyquist_plot(self.sys, omega_limits=[0.01, 100])
        ax.plot(x, y, 'r-')

        ui.ui_main_window.canvas.draw()

    def calc_data_graph2(self, w_ind, draw_mode=False):
        y = np.sin(self.w[w_ind] * self.t)
        x1 = self.x[w_ind][:, 0].copy()

        DT = 2 * np.pi / self.w[w_ind]
        steps = int(np.ceil(3 * DT / np.mean(np.diff(self.t))))
        idx_2 = len(self.t)
        idx_1 = len(self.t) - steps + 1
        X1 = x1[idx_1:idx_2]
        Y = y[idx_1:idx_2]
        Xt = self.t[idx_1:idx_2]
        X1_src = X1.copy()
        Y_src = Y.copy()

        X1_MAX_IDX = []
        Y_MAX_IDX = []

        for k in range(3):
            X1_max_idx = np.argmax(X1)
            dt = int(np.ceil(0.1 * DT / np.mean(np.diff(self.t))))  # 10% offset
            tidx_1_x = max(X1_max_idx - dt, 0)
            tidx_2_x = X1_max_idx + dt
            X1[tidx_1_x:tidx_2_x] = 0

            Y_max_idx = np.argmax(Y)
            tidx_1_y = max(Y_max_idx - dt, 0)
            tidx_2_y = Y_max_idx + dt
            Y[tidx_1_y:tidx_2_y] = 0

            X1_MAX_IDX.append(X1_max_idx)
            Y_MAX_IDX.append(Y_max_idx)
        X1_MAX_IDX.sort()
        Y_MAX_IDX.sort()

        if draw_mode:
            return X1_src, Xt, Y_src, X1_MAX_IDX, Y_MAX_IDX

        self.dtt.append(Xt[min(X1_MAX_IDX[1], Y_MAX_IDX[1])] - Xt[max(Y_MAX_IDX[1], X1_MAX_IDX[1])])
        Tw = 2 * np.pi / self.w[w_ind]
        self.phi.append((self.dtt[-1] / Tw) * 360)

