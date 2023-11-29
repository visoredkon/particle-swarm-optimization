from math import e
from random import uniform
from PSO.ParticleSwarmOptimization import ParticleSwarmOptimization

if __name__ == "__main__":

    def f(x):
        return 0 <= x <= 3 and -2 * e ** (-(x**2))

    x = [uniform(0, 3) for _ in range(3)]
    v = [0.0]
    c = [1.0, 0.5]
    r = [uniform(0, 1) for _ in range(2)]
    w = 1.0

    case_1 = ParticleSwarmOptimization(
        [list(particle) for particle in zip(x)], v, c, r, w, f
    )

    case_1.run(3)
