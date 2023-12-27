from utils.http_methods import Http_methods

#данные из требований
base_url = 'https://rahulshettyacademy.com' #базовый url                            
key = '?key=qaclick123'     # параметр всех запросов

""""методы для тестирования определенного функционала"""

class Google_maps_api():



    """"Создание новой локации"""

    @staticmethod
    def create_new_place():
        post_resourse = '/maps/api/place/add/json'  # ресурс метода пост


        json_for_create_new_place = {"location": { 

                                    "lat": -38.383494, 

                                    "lng": 33.427362 

                                    }, "accuracy": 50, 

                                    "name": "Frontline house", 

                                    "phone_number": "(+91) 983 893 3937", 

                                    "address": "29, side layout, cohen 09", 

                                    "types": [

                                    "shoe park", 

                                    "shop"

                                    ],

                                    "website": "http://google.com", 

                                    "language": "French-IN"}
        
        post_url = base_url+post_resourse+key
        print(post_url)

        result_post = Http_methods.post(post_url, json_for_create_new_place)
        print(result_post)
        return result_post


    """"Проверка (get) локации по её place_id"""

    @staticmethod
    def get_new_place(place_id):           #принимаем place_id для выгрузки по ней
        get_resourse = '/maps/api/place/get/json'        #ресурс метода get по требованиям
        get_url = base_url + get_resourse + key + '&place_id=' + place_id
        print(get_url)
        result_get = Http_methods.get(get_url)
        print(result_get.text)
        return result_get
    

    @staticmethod
    def put_new_place(place_id):           #принимаем place_id работы по нему
        put_resourse = "/maps/api/place/update/json"        #ресурс метода put по требованиям
        put_url = base_url + put_resourse + key
        print(put_url)
        json_for_update_location = {"place_id": place_id,
                                     "address":"100 Lenina street, RU", 
                                     "key":"qaclick123" }
        result_put = Http_methods.put(put_url, json_for_update_location)
        print(result_put.text) 
        return result_put
    
    @staticmethod
    def delete_new_place(place_id):           #принимаем place_id для его последующего удаления
        delete_resourse = "/maps/api/place/delete/json"      #блок Удаления  локации
        delete_url = base_url + delete_resourse + key
        print(delete_url)
        json_for_delete_location = {"place_id": place_id}
        print(place_id)
        result_delete = Http_methods.delete(delete_url, json_for_delete_location)
        print(result_delete.text) 
        return result_delete

