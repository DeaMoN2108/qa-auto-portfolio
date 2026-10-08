import pytest
from faker import Faker
from api_project.clients.pet_client import PetClient
from api_project.clients.store_client import StoreClient
from api_project.clients.user_client import UserClient
from config import config

faker = Faker()

@pytest.fixture
def pet_client():
    return PetClient(base_url=config.api_base_url)

@pytest.fixture
def store_client():
    return StoreClient(base_url=config.api_base_url)

@pytest.fixture
def user_client():
    return UserClient(base_url=config.api_base_url)

@pytest.fixture
def new_pet(pet_client):
    pet_id = faker.random_int(min=1000, max=999999)
    payload = {
        "id": pet_id,
        "name": faker.first_name(),
        "photoUrls": [],
        "status": "available"
    }
    pet_client.create_pet(payload)
    yield pet_id
    pet_client.delete_pet_by_id(pet_id)