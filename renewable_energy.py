
class RenewableEnergy:

    def __init__(self):
        self.capacity_mw = 100

    #HyTEA Way

    def configure(self, config=None):
        if config is None:
            return

        self.capacity_mw = config.get("capacity_mw",self.capacity_mw)