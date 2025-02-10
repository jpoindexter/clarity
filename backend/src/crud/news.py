# News CRUD operations (Dummy example)
class NewsCRUD:
    def get_all(self):
        return [{"id": 1, "title": "Sample News"}]

news = NewsCRUD()  # ✅ This ensures `from crud.news import news` works

# Dummy schema for news
class News:
    id: int
    title: str
