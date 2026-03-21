from typing import List

from api.base_client import BaseClient
from dto.request.pet_request import PetDto


class PetClient(BaseClient):
    f"""
    Клиент для работы с ресурсом /pet.
    Унаследован от BaseClient, поэтому умеет делать get, post и т.д.
    """

    def __init__(self, base_url):
        super().__init__(base_url)

    def get_pet_by_id(self, pet_id: int):
        f"""
        Получить конкретного питомца по id
        Endpoint: GET /pet/{pet_id}
        """

        endpoint = f"/pet/{pet_id}"
        return self.get(endpoint=endpoint)

    def get_pet_by_status(self, pet_status_list: List[str]):
        """
        Получить список питомцев по статусу
        Endpoint: GET /pet/{pet_status}
        """

        params = {
            "status": pet_status_list
        }
        endpoint = f"/pet/findByStatus"
        return self.get(endpoint=endpoint, params=params)

    def update_pet_with_form_data(self, pet_id: int, name: str, status: str):
        f"""
        Обновить данные формы для питомца в магазине
        Endpoint: POST /pet/{pet_id}
        """

        endpoint = f"/pet/{pet_id}"
        payload = {
            "name": name,
            "status": status
        }
        return self.post(endpoint, data=payload)

    def create_pet(self, body: PetDto):
        """
        Создать питомца
        Endpoint: POST /pet
        """
        payload = body.model_dump(by_alias=True)
        return self.post(endpoint="/pet", json=payload)

    def delete_pet(self, pet_id: int):
        """
        Удалить питомца по id
        Endpoint: DELETE /pet/{petId}
        """
        endpoint = f"/pet/{pet_id}"
        return self.delete(endpoint)

    def update_pet(self, body: PetDto):
        """
        Обновить существующего питомца
        Endpoint: PUT /pet
        """

        endpoint = "/pet"
        payload = body.model_dump(by_alias=True)
        return self.put(endpoint=endpoint, json=payload)