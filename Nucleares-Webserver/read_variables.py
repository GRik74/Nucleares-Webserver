import requests

portnum = 8080
url = f"http://localhost:{portnum}/"

def read_variable(variable):
    params = {"Variable": variable}
    response = requests.get(f"{url}", params=params)
    return response.text

