import os

# Оставляем jsonplaceholder для старых тестов
BASE_URL = os.getenv("BASE_URL", "https://jsonplaceholder.typicode.com")

# Специфичный URL для Petstore (используются для новых тестов)
PETSTORE_URL = os.getenv("PETSTORE_URL", "http://localhost:8080/v2")