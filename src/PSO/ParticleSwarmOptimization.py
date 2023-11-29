import inspect
from tabulate import tabulate


class ParticleSwarmOptimization:
    def __init__(self, particle, v, c, r, w, f):
        self.particle = {"old": particle, "new": particle.copy()}
        self.velocities = [v.copy() for _ in range(len(particle))]
        self.cognitive_coefficient = c.copy()
        self.social_coefficient = r.copy()
        self.inertia_weight = w
        self.f = f

        self.pbest = particle.copy()
        self.gbest = None

        self.iter = 0

    def update_pbest(self):
        self.pbest = [
            new_particle
            if self.f(*new_particle) < self.f(*old_particle)
            else old_particle
            for new_particle, old_particle in zip(
                self.particle["new"], self.particle["old"]
            )
        ]

    def update_gbest(self):
        self.gbest = min(
            [self.f(*particle), particle] for particle in self.particle["new"]
        )[1]

    def update_velocity(self):
        self.velocities = [
            [
                self.inertia_weight * current_velocity[j]
                + self.social_coefficient[0]
                * self.cognitive_coefficient[0]
                * (self.pbest[i][j] - current_particle)
                + self.social_coefficient[1]
                * self.cognitive_coefficient[1]
                * (self.gbest[j] - current_particle)
                for j, current_particle in enumerate(self.particle["new"][i])
            ]
            for i, current_velocity in enumerate(self.velocities)
        ]

    def update_particle(self):
        self.particle["old"] = self.particle["new"].copy()
        self.particle["new"] = [
            [
                particle_value + self.velocities[i][j]
                for j, particle_value in enumerate(current_particle)
            ]
            for i, current_particle in enumerate(self.particle["new"])
        ]

    def run(self, iter=1):
        for _ in range(iter):
            self.update_pbest()
            self.update_gbest()
            self.update_velocity()
            self.update_particle()

            self.iter += 1

            print("\n", self)

    def __str__(self):
        objective_function = inspect.getsource(self.f).split("\n")
        objective_function = f'{objective_function[0].strip().replace("def ", "")} {objective_function[1].strip().replace("return ", "")}'

        print(objective_function)
        table_header = [
            "Iteration",
            "Position",
            "Function",
            "Fitness (pBest)",
            "Optimization Result (gBest)",
            "Velocity",
            "New Position",
        ]
        table_data = [
            [
                self.iter,
                ",\n".join(
                    [
                        str([f"{position:.3f}" for position in particle_position])
                        for particle_position in self.particle["old"]
                    ]
                ),
                ",\n".join(
                    [
                        f"{f_value:.3f}"
                        for f_value in [
                            self.f(*position) for position in self.particle["old"]
                        ]
                    ]
                ),
                ",\n".join(
                    [
                        str([f"{position:.3f}" for position in particle_position])
                        for particle_position in self.pbest
                    ]
                ),
                ""
                if self.iter == 0
                else ",\n".join(str(position) for position in self.gbest),
                ",\n".join(
                    [
                        str([f"{velocity:.3f}" for velocity in particle_velocity])
                        for particle_velocity in self.velocities
                    ]
                ),
                ""
                if self.iter == 0
                else ",\n".join(
                    [
                        str([f"{position:.3f}" for position in particle_position])
                        for particle_position in self.particle["new"]
                    ]
                ),
            ]
        ]
        return tabulate(
            table_data,
            headers=table_header,
            stralign="center",
            numalign="center",
            tablefmt="rounded_grid",
        )
