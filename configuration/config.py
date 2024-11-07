import json

class Config():
    """Wrapper class configuration class"""

    def __init__(self, config_path: str = "config.json"):
        with open(config_path, mode="r") as f:
            self.data = json.load(f)

    def __getitem__(self, item: str):
        return self.data[item]


if __name__ == "__main__":
    c = Config()
    print(c)

