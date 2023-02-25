import pytest
import requests

class TestApi:
    names = [
        ("Posha"),
        ("Vasya"),
        ("")
    ]
    @pytest.mark.parametrize('name', names)
    def test_hello(self, name):
        url = "https://playground.learnqa.ru/api/hello"
        data = {'name' : name}

        response = requests.get(url, params=data)

        assert response.status_code == 200, "Wrong response code"

        response_dict = response.json()
        assert "answer" in response_dict, "No answer in response"
        if len(name) == 0:
            expected_text = "Hello, someone"
        else:
            expected_text = f"Hello, {name}"
        actual_text = response_dict["answer"]
        assert expected_text == actual_text, "Text is not correct"