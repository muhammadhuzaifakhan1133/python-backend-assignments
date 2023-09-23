from google.oauth2 import service_account

# Define the required scopes
scopes = [
  "https://www.googleapis.com/auth/userinfo.email",
  "https://www.googleapis.com/auth/firebase.database"
]

# Authenticate a credential with the service account
credentials = service_account.Credentials.from_service_account_file(
    "E:\github\python-backend-assignments\service-account-file.json", scopes=scopes)
print()