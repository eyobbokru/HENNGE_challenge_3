import base64
import requests
import time

# Constants
SHARED_SECRET_SUFFIX = 'HENNGECHALLENGE003'
TOTP_API_URL = 'https://totpfast.azurewebsites.net/api/TOTPGenerator'
CHALLENGE_API_URL = 'https://api.challenge.hennge.com/challenges/003'

# Replace these with actual values
SECRET_GIST_PLACEHOLDER = "REPLACE_ME_WITH_SECRET_GIST"
EMAIL_PLACEHOLDER = "REPLACE_ME_WITH_EMAIL"
SOLUTION_PLACEHOLDER = "REPLACE_ME_WITH_SOLUTION"  # 'python' or 'golang'

def generate_totp_password(userid):
    """
    Generates a Time-based One-Time Password (TOTP) for authentication.

    Args:
        userid (str): The user identifier for which the TOTP is generated.

    Returns:
        str: The generated TOTP password.
    """
    secret = userid + SHARED_SECRET_SUFFIX
    current_time = int(time.time()) + 30

    params = {
        'code': 'V4E3yvUMwDz7UbzaZ8LdPpJMa6SkbgD0dXHLCFsfJgxNps12ZIJppQ==',
        'T0': '0',
        'X': '30',
        'sharedSecret': secret,
        'digits': '10',
        'timestamp': str(current_time),
        'hashAlgorithm': 'HmacSHA512'
    }

    response = requests.get(TOTP_API_URL, params=params)

    if response.status_code == 200:
        return response.text.strip()
    else:
        raise ValueError(f"Error: {response.status_code}, {response.text}")

def make_post_request(url, json_data):
    """
    Makes a POST request to the specified URL with JSON data and authentication.

    Args:
        url (str): The URL to make the POST request to.
        json_data (dict): The JSON data to include in the request body.

    Returns:
        requests.Response: The response object from the POST request.
    """
    email = json_data.get("contact_email", EMAIL_PLACEHOLDER)
    totp_password = generate_totp_password(email)
    auth_credentials = f"{email}:{totp_password}"
    auth_header = f"Basic {base64.b64encode(auth_credentials.encode()).decode()}"
    headers = {
        "Authorization": auth_header,
        "Content-Type": "application/json",
        "Accept": "*/*",
    }

    response = requests.post(url, json=json_data, headers=headers)
    return response

if __name__ == "__main__":
 
    json_data = {
        "github_url": SECRET_GIST_PLACEHOLDER,
        "contact_email": EMAIL_PLACEHOLDER,
        "solution_language": SOLUTION_PLACEHOLDER  # 'python' or 'golang'
    }

    try:
        response = make_post_request(CHALLENGE_API_URL, json_data)
        print("Response Code:", response.status_code)
        print("Response Content:", response.text)
    except Exception as e:
        print(f"Error: {e}")
