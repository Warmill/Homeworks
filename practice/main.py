import sys
import json
from argparse import ArgumentParser
from signers import Signer


def args_parser() -> ArgumentParser:
    parser = ArgumentParser(description="Very strong decoder.")
    parser.add_argument(
        "--secret", type=str, required=True, help="Secret key for encode / decode."
    )
    parser.add_argument(
        "--salt", type=str, required=True, help="Secret key for encode / decode."
    )
    parser.add_argument(
        "--using",
        choices=["pyjwt", "itsdangerous"],
        required=True,
        help="Package to encode / decode.",
    )
    parser.add_argument("--action", choices=["encode", "decode"], required=True)
    parser.add_argument(
        "--input_file", type=str, required=True, help="Input filename *.json"
    )
    parser.add_argument(
        "--output_file", type=str, required=True, help="Output filename *.json"
    )
    return parser


if __name__ == "__main__":
    parser = args_parser()
    namespace = parser.parse_args(sys.argv[1:])
    sign = Signer(secret=namespace.secret, salt=namespace.salt)
    if namespace.action == "encode":
        encode: list = []
        with open(file=namespace.input_file) as file:
            try:
                data = json.load(file)
            except json.decoder.JSONDecodeError:
                raise "invalid input data..."
        for count, line in enumerate(data):
            if namespace.using == "pyjwt":
                encode.append(sign.jwt_encode(payload=data[count]))
            if namespace.using == "itsdangerous":
                encode.append(sign.itsdangerous_encode(payload=data[count]))
        with open(file=namespace.output_file, mode="w") as file:
            file.write(json.dumps(encode))

    if namespace.action == "decode":
        decode: list = []
        with open(file=namespace.input_file) as file:
            try:
                data = json.load(file)
            except json.decoder.JSONDecodeError:
                raise "invalid input data..."
        for count, line in enumerate(data):
            if namespace.using == "pyjwt":
                decode.append(sign.jwt_decode(encoded=line))
            if namespace.using == "itsdangerous":
                decode.append(sign.itsdangerous_decode(encoded=line))
        with open(file=namespace.output_file, mode="w") as file:
            file.write(json.dumps(decode))
