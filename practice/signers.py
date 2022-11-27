import jwt
from itsdangerous import URLSafeSerializer


class Signer:
    def __init__(self, secret: str, salt: str):
        self.secret = secret
        self._salt = salt

    def jwt_encode(self, payload: dict):
        return jwt.encode(payload, self.secret + self._salt, algorithm="HS256")

    def jwt_decode(self, encoded):
        return jwt.decode(encoded, self.secret + self._salt, algorithms=["HS256"])

    def itsdangerous_encode(self, payload: dict):
        data = URLSafeSerializer(self.secret, salt=self._salt)
        return data.dumps(payload)

    def itsdangerous_decode(self, encoded):
        data = URLSafeSerializer(self.secret, salt=self._salt)
        return data.loads(encoded)
