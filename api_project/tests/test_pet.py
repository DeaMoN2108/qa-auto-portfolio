import allure
from faker import Faker
from api_project.models.pet import PetModel

fake = Faker()

@allure.feature("Управление питомцами")
@allure.title("Создание и получение питомца")
def test_create_and_get_pet(pet_client):
    pet_id = fake.random_int(min=10000, max=999999)
    pet_name = fake.first_name()
    payload = {
        "id": pet_id,
        "name": pet_name,
        "category": {"id": 1, "name": "Dogs"},
        "photoUrls": [fake.image_url()],
        "tags": [{"id": 1, "name": "good_boy"}],
        "status": "available"
    }
    create_response = pet_client.create_pet(payload)
    body = PetModel(**create_response.json())
    assert create_response.status_code == 200, f"Ожидался статус 200, но получен: {create_response.status_code}"
    assert body.name == pet_name
    get_response = pet_client.get_pet_by_id(pet_id)
    assert get_response.status_code == 200
    fetched_pet = PetModel(**get_response.json())
    assert fetched_pet.name == pet_name
    pet_client.delete_pet_by_id(pet_id)

@allure.feature("Управление питомцами")
@allure.title("Обновление питомца")
def test_update_pet(pet_client, new_pet):
    pet_id = new_pet
    update_payload = {
        "id": pet_id,
        "name": "UpdatedName",
        "photoUrls": [],
        "status": "sold"
    }
    update_response = pet_client.update_pet(update_payload)
    assert update_response.status_code == 200, f"Ожидался 200, но получили: {update_response.status_code}"
    fetched_body = PetModel(**update_response.json())
    assert fetched_body.status == "sold", f"Обвновление питомца не произошло: {fetched_body.status}"
