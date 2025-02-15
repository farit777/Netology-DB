from datetime import datetime
from task_1 import Publisher, Book, Stock, Sale, Shop
from database import DefaultSession

def get_shops(identifier):
    session = DefaultSession()

    try:
        # Создание общего тела запроса
        query = session.query(
            Book.title,
            Shop.name,
            Sale.price,
            Sale.date_sale
        ).select_from(Shop).\
            join(Stock).\
            join(Book).\
            join(Publisher).\
            join(Sale)

        # Проверка, является ли идентификатор числом
        if identifier.isdigit():
            # Фильтрация по id издателя
            result = query.filter(Publisher.id == int(identifier)).all()
        else:
            # Фильтрация по имени издателя
            result = query.filter(Publisher.name == identifier).all()

        # Вывод результатов
        for title, shop_name, price, date_sale in result:
            print(f"{title:<40} | {shop_name:<10} | {price:<8.2f} | {date_sale.strftime('%d-%m-%Y')}")

    finally:
        session.close()

if __name__ == '__main__':
    publisher_id_or_name = input("Enter the publisher's name or ID: ")  # Просим клиента ввести имя или ID
    get_shops(publisher_id_or_name)  # Вызов функции для выполнения запроса и вывода результата
