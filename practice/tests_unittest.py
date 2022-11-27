from unittest import TestCase
from signers import Signer

sign = Signer(secret="1", salt="2")


class TestSigners(TestCase):

    def Test_Equal(self):
        self.assertEqual(type(sign), Signer)

    def Test_JwtEqual(self):
        data = {"name":"John"}
        encd = sign.jwt_encode(data)
        dcd = sign.jwt_decode(encd)
        self.assertEqual(sign.jwt_decode(encd,{"name":"John"}))
        self.assertEqual(sign.jwt_encode(dcd,encd))

    def Test_DataChange(self):
        data = {'':''}
        encd = sign.jwt_encode(data)
        dcd = sign.jwt_decode(encd)
        self.assertNotEqual(encd,dcd)

    def Test_ReturnStr(self):
        data = {"name":"John"}
        self.assertEqual(type(sign.jwt_encode(data)),str)

    def Test_TypeError(self):
        self.assertRaises(TypeError,Signer(["a","b"],{"c","d"}))

    def Test_CheckData(self):
        data = {"name": "John"}
        encd = sign.jwt_encode(data)
        dcd = sign.jwt_decode(encd)
        self.assertEqual(sign.jwt_decode(encd, {"name": "John"}))
        self.assertEqual(sign.jwt_encode(dcd, encd))
