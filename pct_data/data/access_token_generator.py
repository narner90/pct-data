import pickle

from stravalib.client import Client

from pct_data.data.secret_loader import SecretLoader


class AccessTokenGenerator:
    def __init__(self, secret_loader: SecretLoader):
        self._client = Client()
        self._secret_loader = secret_loader

    def write_access_token(self) -> None:
        secret = self._secret_loader.load_secret()

        token_response = self._client.exchange_code_for_token(client_id=secret['client_id'],
                                                              client_secret=secret['client_secret'],
                                                              code=secret['code'])
        access_token = token_response['access_token']
        print(f'Retrieved access token: {access_token} for athlete: {self._client.get_athlete()}')

        with open('./secret/access_token.pkl', 'wb') as file:
            pickle.dump(access_token, file)


if __name__ == '__main__':
    secret_loader = SecretLoader()
    AccessTokenGenerator(secret_loader).write_access_token()
