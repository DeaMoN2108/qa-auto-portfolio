from enum import Enum

class Endpoints(str, Enum):
    PET = "/pet"
    STORE_ORDER = "/store/order"
    USER = "/user"