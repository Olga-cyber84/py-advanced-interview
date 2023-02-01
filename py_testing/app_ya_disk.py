import requests
from datetime import date
from config import token


class YaDisk:
    def __init__(self, token: str):
        self.token = token

    def createdir(self, dir_name):
        """Метод создает папку на яндекс диске"""
        info_dir = self.infodir(dir_name)
        headers = {'Content-Type': 'application/json',
                   'Accept': 'application/json', 'Authorization': f'OAuth {self.token}'}
        url = "https://cloud-api.yandex.net/v1/disk/resources?path=" + dir_name

        if info_dir:
            print('папка с таким именем существует')
            return dir_name, False
        else:
            response = requests.put(url, headers=headers)

            if response.status_code in (200, 201, 202):
                print('папка создана')
                return dir_name, True
            else:
                print('не удалось создать папку')
                return dir_name, False

    def infodir(self, dir_name):
        """Метод получения метаинфорации о папке"""
        headers = {'Content-Type': 'application/json',
                   'Accept': 'application/json', 'Authorization': f'OAuth {self.token}'}
        url = "https://cloud-api.yandex.net/v1/disk/resources?path=" + dir_name
        response = requests.get(url, headers=headers)
        return response.status_code == 200

    def deletedir(self, dir_name):
        """Метод удаляет папку на яндекс диске"""
        headers = {'Content-Type': 'application/json',
                   'Accept': 'application/json', 'Authorization': f'OAuth {self.token}'}
        url = "https://cloud-api.yandex.net/v1/disk/resources?path=" + dir_name
        info_dir = self.infodir(dir_name)
        if info_dir:
            response = requests.delete(url, headers=headers)
            if response.status_code in (200, 202, 204):
                print('папка удалена')
                return dir_name, True
            else:
                print('не удалось удалить папку')
                return dir_name, False
        print('такой папки нет')
        return dir_name, False


if __name__ == '__main__':

    ya_disk = YaDisk(token)
    dir_name = f"new_{date.today()}"
    # created_dir = ya_disk.createdir(dir_name)
    # delete_dir_dir = ya_disk.deletedir(dir_name)
