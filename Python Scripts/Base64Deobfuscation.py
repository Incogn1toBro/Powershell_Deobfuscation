import base64

# Define a Base64 string
base64_string = "XXXX"

# Decode the Base64 string
decoded_bytes = base64.b64decode(base64_string)

# Convert the bytes to a string
decoded_string = decoded_bytes.decode('utf-8')

# Print the string
print(decoded_string)
