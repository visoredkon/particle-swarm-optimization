class ParticleSwarmOptimization:
    def __init__(self, x, v, c, r, w, f):
        self.x = {"old": x, "new": x.copy()}
        self.v = v.copy() * len(x)
        self.c = c.copy()
        self.r = r.copy()
        self.w = w
        self.f = f

        self.pbest = x.copy()
        self.gbest = None

    def update_pbest(self):
        for index, (old_x, new_x) in enumerate(zip(self.x["old"], self.x["new"])):
            if self.f(new_x) < self.f(old_x):
                self.pbest[index] = new_x

    def update_gbest(self):
        self.gbest = min(self.pbest)

    def update_v(self):
        for index, (v_i, pbest_i, x_i) in enumerate(
            zip(self.v, self.pbest, self.x["new"])
        ):
            self.v[index] = (
                self.w * v_i
                + self.r[0] * self.c[0] * (pbest_i - x_i)
                + self.r[1] * self.c[1] * (self.gbest - x_i)
            )

    def update_x(self):
        self.x["old"] = self.x["new"].copy()

        for index, _ in enumerate(self.x["new"]):
            self.x["new"][index] += self.v[index]

    def run(self, iter):
        for _ in range(iter):
            self.update_pbest()
            self.update_gbest()
            self.update_v()
            self.update_x()

            print(self)
            print("\n")

    def __str__(self):
        return f"""
        x: {self.x},
        v: {self.v},
        c: {self.c},
        r: {self.r},
        w: {self.w},
        pBest: {self.pbest},
        gBest: {self.gbest}
        f{[x for x in self.x['old']]}: {[self.f(x) for x in self.x['old']]}"""
