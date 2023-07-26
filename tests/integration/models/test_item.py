from models.item import ItemModel
from tests.base_test import BaseTest


class ItemTest(BaseTest):

    def test_crud(self):
# Создание контекстного менеджера
        with self.app_context():
# Создание объекта ItemModel с именем 'test' и ценой "19.99"
            item = ItemModel("test", 19.99)
        # Проверяем, что его нет в базе данных
# Это проверка того, что метод find_by_name класса ItemModel возвращает None, то есть не находит объект с именем "test".
            self.assertIsNone(ItemModel.find_by_name("test"),
                              f"Найден элемент с именем {item.name}, но ожидалось, что его не будет.")
        # Сохраняем его в базу данных
            item.save_to_db()
        # Проверяем, что он теперь ЕСТЬ в базе данных
# Это проверка того, что после сохранения объекта item в базу данных метод find_by_name теперь вернет объект с именем "test".
            self.assertIsNotNone(ItemModel.find_by_name("test"))
        # Удаляем его из базы данных
            item.delete_from_db()
        # Проверяем, что его снова НЕТ в базе данных
# Это последняя проверка того, что после удаления объекта item из базы данных метод find_by_name снова вернет None
            self.assertIsNone(ItemModel.find_by_name("test"))