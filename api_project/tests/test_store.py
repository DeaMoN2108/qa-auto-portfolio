import allure
from faker import Faker
from api_project.models.store import OrderModel

faker = Faker()

@allure.feature("Управление магазином")
@allure.title("Создание заказа на существующего питомца")
def test_create_order(store_client, new_pet):
    pet_id = new_pet
    payload = {
      "id": faker.random_int(min=1, max=9999),
      "petId": pet_id,
      "quantity": 0,
      "shipDate": "2026-10-08T08:16:09.217Z",
      "status": "placed",
      "complete": True
}
    create_order = store_client.place_order(payload)
    assert create_order.status_code == 200, f"Ожидался 200, а получили {create_order.status_code}"
    body = OrderModel(**create_order.json())
    assert body.petId == pet_id
    get_inventory = store_client.get_inventory()
    assert get_inventory.status_code == 200, f"Ожидался 200, а получили {get_inventory.status_code}"
    inventory_body = get_inventory.json()
    assert isinstance(inventory_body, dict), f"Ожидался словарь, а получили {type(inventory_body)}"
    store_client.delete_order_by_id(body.id)