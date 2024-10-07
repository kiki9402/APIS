import base64
from base64 import *

encode_str = input("base64코드를 입력해주세요 :")

decode_bytes = base64.b64decode(encode_str)

decode_str = decode_bytes.decode('utf-8')

print(decode_str)