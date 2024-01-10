import secrets

def gen_api_key():
    return secrets.token_hex(16)

