# Hennge Challenge 003 submission

This readme provides instructions on how to use the provided Python script for Hennge Challenge 003. The script interacts with the Hennge Challenge API using Time-based One-Time Passwords (TOTP) for authentication.

## Instructions

### Prerequisites

1. **Python:** Ensure that Python is installed on your machine. If not, you can download it from [python.org](https://www.python.org/downloads/).

2. **Pip:** Make sure you have the `requests` library installed. You can install it using the following command:

   ```bash
   pip install requests
   ```

## Getting Started

1. **Clone the repository:**
    ```bash
    git clone https://github.com/eyobbokru/hennge-challenge-003-submission.git
    ```

2. **Navigate to the project directory:**
    ```bash
    cd hennge-challenge-003-submission
    ```

3. **Open the `hennge_challenge_003.py` file in a text editor.**

4. **Replace the placeholder values in the script with your actual data:**
    - Replace `REPLACE_ME_WITH_SECRET_GIST` with the URL of your secret Gist on GitHub.
    - Replace `REPLACE_ME_WITH_EMAIL` with your email address.
    - Replace `REPLACE_ME_WITH_SOLUTION` with the language you used for your solution ('python' or 'golang').

5. **Save the changes to the script.**

6. **Run the script:**
    ```bash
    python hennge_challenge_003.py
    ```

7. **Check the output:**
    - If successful, the script will print the response code and content from the Hennge Challenge API.
    - If there's an error, the script will print an error message.

## Notes

- Ensure that the URLs for the TOTP API (`TOTP_API_URL`) and the Hennge Challenge API (`CHALLENGE_API_URL`) are correct. If there are updates, modify these constants accordingly.
  
- The TOTP is generated based on the current time, and the script adds 30 seconds to ensure synchronization.

- If you encounter any issues or have questions, feel free to reach out for assistance.

Good luck with your Hennge Challenge 003 submission!

### Reference
- https://youngforest.github.io/en/2022/03/19/Hennge-challenge-3/
- https://totp.youngforest.me/ 
