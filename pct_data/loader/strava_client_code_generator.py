from stravalib.client import Client

API_SCOPE = ['read', 'profile:read_all', 'activity:read']


class StravaClientCodeGenerator:
    def __init__(self):
        self._client = Client()

    def get_code(self, client_id: int) -> None:
        # Will create a popup that needs to be confirmed
        authorize_url = self._client.authorization_url(client_id=40761,
                                                       redirect_uri='http://localhost:8282/authorized',
                                                       scope=API_SCOPE)
        print(f'Authorization URL: {authorize_url}')


if __name__ == '__main__':
    StravaClientCodeGenerator().get_code(40761)
