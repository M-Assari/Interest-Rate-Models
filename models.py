
""" 
This module contains the implementation of Vasicek and Ho-Lee interest rate models.
"""
import numpy as np

class VasicekModel:
    def __init__(self, a, b, sigma, r0, scheme="euler"):
        self.a, self.b, self.sigma, self.r0 = a, b, sigma, r0
        self.scheme = scheme

    def simulate(self, T, dt, n_paths):
        n_steps = int(T / dt)
        paths = np.zeros((n_steps + 1, n_paths))
        paths[0] = self.r0
        dW = np.sqrt(dt) * np.random.normal(size=(n_steps, n_paths))

        for t in range(n_steps):
            drift = self.a * (self.b - paths[t]) * dt
            diffusion = self.sigma * dW[t]
            paths[t + 1] = paths[t] + drift + diffusion

        return paths

class HoLeeModel:
    def __init__(self, theta, sigma, r0, scheme="euler"):
        self.theta, self.sigma, self.r0 = theta, sigma, r0
        self.scheme = scheme

    def simulate(self, T, dt, n_paths):
        n_steps = int(T / dt)
        paths = np.zeros((n_steps + 1, n_paths))
        paths[0] = self.r0
        dW = np.sqrt(dt) * np.random.normal(size=(n_steps, n_paths))

        for t in range(n_steps):
            drift = self.theta * dt
            diffusion = self.sigma * dW[t]
            paths[t + 1] = paths[t] + drift + diffusion

        return paths
