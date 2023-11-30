from math import cos
from PSO.ParticleSwarmOptimization import ParticleSwarmOptimization

if __name__ == "__main__":

    def f(x, y):
        return cos(x + y) + (x - y) ** 2 - 1.5 * x + 2.5 * y + 1

    x = [1.0, -1.0, 2.0]
    y = [1.0, 1.0, 1.0]
    v = [0.0, 0.0]
    c = [1.0, 0.5]
    r = [1.0, 1.0]
    w = 1.0

    pso = ParticleSwarmOptimization(
        [list(particle) for particle in zip(x, y)], v, c, r, w, f
    )

    pso.run(3)
