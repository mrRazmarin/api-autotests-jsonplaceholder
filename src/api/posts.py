from api.base_client import BaseClient


class PostClient(BaseClient):
    """
    Клиент для работы с ресурсом /posts.
    Унаследован от BaseClient, поэтому умеет делать get, post и т.д.
    """

    def __init__(self, base_url):
        super().__init__(base_url)

    def get_all_posts(self):
        """
        Получить список всех постов.
        Endpoint: GET /posts
        """

        return self.get("/posts")

    def get_post_by_id(self, post_id):
        """
        Получить конкретный пост по ID.
        Endpoint: GET /posts/{id}
        """

        endpoint = f"/posts/{post_id}"
        return self.get(endpoint=endpoint)

    def create_post(self, title, body, user_id):
        """
        Создать новый пост.
        Endpoint: POST /posts
        """

        payload = {
            "title": title,
            "body": body,
            "userId": user_id
        }
        return self.post(endpoint="/post", json=payload)