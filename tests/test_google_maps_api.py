from utils.api import Google_maps_api
from requests import Response
from utils.checking import Cheching

"""создание, изменение и удаление новой локации"""
class Test_create_place():

    def test_create_new_place(self):

        print("метод post")
        result_post: Response = Google_maps_api.create_new_place()

        check_post = result_post.json()
        place_id = check_post.get("place_id")

        Cheching.cheching_status(result_post, 200)
        Cheching.cheching_json_value(result_post, 'status', 'OK')

        print("метод get")                                    
        result_get: Response = Google_maps_api.get_new_place(place_id) # на созданную локацию методом post проверяем по полученному place id что локация создана методом get

        Cheching.cheching_status(result_get, 200)
        Cheching.cheching_json_value(result_get, 'address', '29, side layout, cohen 09')


        print("метод put")                                    
        result_put: Response = Google_maps_api.put_new_place(place_id) # заменяем, сам текст json зашит в методе

        Cheching.cheching_status(result_put, 200)
        Cheching.cheching_json_token(result_put, ['msg'])
        Cheching.cheching_json_value(result_put, 'msg', 'Address successfully updated')

        
        print("метод delete")                                    
        result_delete: Response = Google_maps_api.delete_new_place(place_id) # удаляем по place_id он передается в теле, в самом методе

        Cheching.cheching_status(result_delete, 200)
        Cheching.cheching_json_value(result_delete, 'status', "OK")


        print("повторный метод delete")                                    
        result_delete: Response = Google_maps_api.delete_new_place(place_id) # удаляем по place_id он передается в теле, в самом методе

        Cheching.cheching_status(result_delete, 404)
        Cheching.cheching_json_value(result_delete, 'msg', "Delete operation failed, looks like the data doesn't exists")


        
 