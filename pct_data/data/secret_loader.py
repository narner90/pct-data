import json


class SecretLoader:
    def load_secret(self) -> dict:
        with open("./secret/secret.json") as file:
            return json.load(file)
