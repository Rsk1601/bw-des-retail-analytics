# import hvac

# # Initialize the Vault client
# client = hvac.Client(url="http://127.0.0.1:8200", token="hvs.la3oPoRng7kzBSTPgkWfkRbK")

# # Path to the secret
# secret_path = 'secret/data/aws'

# # Retrieve the secret
# try:
#     secret = client.read(secret_path)
#     print(secret)
#     if secret and 'data' in secret:
#         # Access the password or any other secret data
#         bw_aws_access_key = secret.get('data', {}).get('data', {}).get('bw_aws_access_key')
#         bw_aws_secret_key = secret.get('data', {}).get('data', {}).get('bw_aws_secret_key')

#         print(f"Retrieved access_key: {bw_aws_access_key}")
#         print(f"Retrieved secret_key:{bw_aws_secret_key}")
#     else:
#         print("Secret not found or empty")
# except hvac.exceptions.InvalidPath:
#     print("Invalid path or permission issue")
# except hvac.exceptions.Forbidden:
#     print("Access to the secret is forbidden")
# except hvac.exceptions.VaultDown:
#     print("Vault server is down or unreachable")
# except Exception as e:
#     print(f"An error occurred: {str(e)}")

import hvac

def get_aws_access_keys(vault_url, vault_token, secret_path):
    try:
        client = hvac.Client(url=vault_url, token=vault_token)
        secret = client.read(secret_path)
        if secret and 'data' in secret:
            bw_aws_access_key = secret.get('data', {}).get('data', {}).get('bw_aws_access_key')
            bw_aws_secret_key = secret.get('data', {}).get('data', {}).get('bw_aws_secret_key')
            return bw_aws_access_key, bw_aws_secret_key
        else:
            return None, None  # Or raise an exception for empty secret
    except hvac.exceptions.InvalidPath:
        raise ValueError("Invalid path or permission issue")
    except hvac.exceptions.Forbidden:
        raise ValueError("Access to the secret is forbidden")
    except hvac.exceptions.VaultDown:
        raise ConnectionError("Vault server is down or unreachable")
    except Exception as e:
        raise RuntimeError(f"An error occurred: {str(e)}")



