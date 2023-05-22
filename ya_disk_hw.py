from pprint import pprint
import requests

TOKEN = "..."

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        headers = {
            'Contetnt-Type': 'aplication/json',
            'Authorization': f'OAuth {self.token}'
        }
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        params = {"path": file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers = headers, params = params)
        response_data = response.json()
        pprint(response.json())
        href = response_data.get("href", "")
        
        response = requests.put(href, data = open("test.txt", "rb"))
        if response.status_code == 201:
            print("Ура! Получилось!")

if __name__ == '__main__':
    path_to_file = "test.txt"
    token = TOKEN
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)



