import base64

original_str = input("base64로 인코딩할것을 입력해주세요! : ")

original_bytes = original_str.encode('utf-8')

encoded_bytes = base64.b64encode(original_bytes)

encoded_str = encoded_bytes.decode('utf-8')

print(f"인코딩할것: {original_str}")
print(f"인코딩 완료: {encoded_str}")
