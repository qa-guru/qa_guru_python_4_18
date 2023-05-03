class Cart:
    def __init__(self, json):
        self.json = json

    @property
    def addition_success_status(self):
        return self.json["success"]

    @property
    def products_count(self):
        return self.json["updatetopcartsectionhtml"]
