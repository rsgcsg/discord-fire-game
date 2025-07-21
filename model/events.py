class BaseEvent:
    def __init__(self, player, world, context=None):
        self.player = player
        self.world = world
        self.context = context or {}

    def run(self):
        raise NotImplementedError("a event should be able to run")

