class BaseScene:
    def __init__(self, ctx):
        self.ctx = ctx
        self.entities = []

    def add(self, e):
        self.entities.append(e)
        return e

    def on_key(self, key, is_down):
        pass

    def update(self, dt):
        for e in self.entities:
            e.update(dt, self.ctx)

    def draw(self):
        for e in self.entities:
            if getattr(e, "visible", True):
                e.draw(self.ctx)
