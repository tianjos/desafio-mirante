import json


class OutputJSON:
    def __init__(self, data):
        self.data = data

    def display(self):
        print(json.dumps(self.data, indent=4))
