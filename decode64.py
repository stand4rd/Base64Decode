from base64 import b64decode

encodedStr = raw_input("Type Base64 Encoded String Here: ")

print(b64decode(encodedStr))
