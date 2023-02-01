# python -m pytest tests/test_pytest.py
import pytest
from app_ya_disk import YaDisk
from config import token

dir_name = 'name_1'

fixture = [
    (dir_name, True),
    (dir_name, False),
]


@pytest.mark.parametrize("dir_name, is_creating_successful", fixture)
def test_createdir(dir_name,  is_creating_successful):
    result = YaDisk(token).createdir(dir_name)
    print(result)
    assert result[1] == is_creating_successful


if __name__ == '__main__':
    res = YaDisk(token).deletedir(dir_name)
