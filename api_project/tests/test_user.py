import allure
from faker import Faker
from api_project.models.user import UserModel

faker = Faker()

@allure.feature("Управление пользователем")
@allure.title("Создание пользователя")
def test_create_user(user_client):
    payload = {
      "id": faker.random_int(min=1, max=100000),
      "username": faker.user_name(),
      "firstName": faker.first_name(),
      "lastName": faker.last_name(),
      "email": faker.email(),
      "password": faker.password(),
      "phone": faker.phone_number(),
      "userStatus": 1
}
    create_user = user_client.create_user(payload)
    assert create_user.status_code == 200, f"Ожидался 200, а получили {create_user.status_code}"
    user_info = user_client.get_info_user_by_username(payload["username"])
    assert user_info.status_code == 200, f"Ожидался 200, а получили {user_info.status_code}"
    fetched_data = UserModel(**user_info.json())
    assert fetched_data.username == payload["username"]
    assert fetched_data.firstName == payload["firstName"]
    assert fetched_data.lastName == payload["lastName"]
    assert fetched_data.email == payload["email"]
    assert fetched_data.password == payload["password"]
    assert fetched_data.phone == payload["phone"]
    assert fetched_data.userStatus == payload["userStatus"]
    user_client.delete_user_by_username(fetched_data.username)