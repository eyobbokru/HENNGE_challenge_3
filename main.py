import base64
import requests
import time

def generate_totp_password(userid):
    # Use requests library to generate TOTP password
    secret = userid + 'HENNGECHALLENGE003'
    
    current_time = int(time.time()) +30
    
    url = f'https://totpfast.azurewebsites.net/api/TOTPGenerator'
    params = {
        'code': 'V4E3yvUMwDz7UbzaZ8LdPpJMa6SkbgD0dXHLCFsfJgxNps12ZIJppQ==',
        'T0': '0',
        'X': '30',
        'sharedSecret': secret,
        'digits': '10',
        'timestamp': str(current_time),
        'hashAlgorithm': 'HmacSHA512'
    }

    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        return response.text.strip()
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None

def make_post_request(url, json_data, email):
    totp_password = generate_totp_password(email)
    en  = "eyob.bokru@gmail.com:"+totp_password
   
    auth_header = f"Basic {base64.b64encode(en.encode()).decode()}"
    headers = {
        "Authorization": auth_header,
        "Content-Type": "application/json",
        "Accept": "*/*",
    }

    response = requests.post(url, json=json_data, headers=headers)
    return response

if __name__ == "__main__":
    url = "https://api.challenge.hennge.com/challenges/003"
    
    json_data = {
        "github_url": "https://gist.github.com/eyobbokru/4dff769e80a7ec5eb43c9330e6738af9",
        "contact_email": "eyob.bokru@gmail.com",
        "solution_language": "python"
    }
    
    email = "eyob.bokru@gmail.com"
    
    response = make_post_request(url, json_data, email)

    print("Response Code:", response.status_code)
    print("Response Content:", response.text)
