from requests import Response
import json
""""метод для проверки ответов для наших запросов"""


class Cheching():
    
    """метод проверки статус кода"""
    @staticmethod
    def cheching_status(response: Response, status_code):
        assert status_code == response.status_code
        if response.status_code == status_code:
            print("успешно, статус код = " + str(response.status_code))
        else:
            print("провал, статус код =  "+ str(response.status_code)) 


    """Метод для проверки наличия обязательных полей в теле ответа"""

    @staticmethod
    def cheching_json_token(response: Response, expected_value):
        token = json.loads(response.text)
        assert list(token) == expected_value
        print("Все поля присутствуют")



    """Метод для проверки Значений обязательных полей в теле ответа"""

    @staticmethod
    def cheching_json_value(response: Response, field_name, expected_value):
        check = response.json()
        check_info = check.get(field_name)
        assert check_info == expected_value
        print(field_name + "значение верно")


    @staticmethod
    def cheching_json_search_word_in_value(response: Response, field_name, expected_value, search_word):
        check = response.json()
        check_info = check.get(field_name)
        if search_word in check_info:
            print("Слово" + search_word + "присутствует")
        else:
            print("Слово" + search_word + "отсутствует")

        

