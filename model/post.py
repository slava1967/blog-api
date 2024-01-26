from model.user import User
from model.comment import Comment


class Post:

    def __init__(self, id: int, body: str, author: User, comments: list):
        self.id = id
        self.body = body
        self.author = author
        self.comments = comments
