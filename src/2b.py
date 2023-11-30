from math import cos
from random import uniform
from PSO.ParticleSwarmOptimization import ParticleSwarmOptimization

if __name__ == "__main__":

    def f(x, y):
        return (5 <= x == y <= 5 <= 5 and cos(x + y) + (x - y) ** 2 - 1.5 * x + 2.5 * y + 1)

    dimension = 10

    x = [uniform(5, 5) for _ in range(dimension)]
    y = [uniform(5, 5) for _ in range(dimension)]
    v = [0.0, 0.0]
    c = [1.0, 0.5]
    r = [uniform(0, 1) for _ in range(2)]
    w = 1.0

    particle = ParticleSwarmOptimization(
        [list(particle) for particle in zip(x, y)], v, c, r, w, f
    )

    particle.run(3)
