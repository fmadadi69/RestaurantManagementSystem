class MenuItem:
    def __init__(self, name, price, description, category):
        self.name = name
        self.price = price
        self.description = description
        self.category = category


class Menu:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    @staticmethod
    def create_menu_item(name, price, description, category):
        return MenuItem(name, price, description, category)

    def add_menu_item_to_database(self, menu_item):
        query = 'INSERT INTO MenuItems (name, price, description, category) values (%s , %s, %s, %s)'
        params = (menu_item.name, menu_item.price, menu_item.description, menu_item.category)
        self.db_manager.execute(query, params)
        self.db_manager.commit()

    def get_menu_items(self):
        query = 'SELECT * from MenuItems'
        cursor = self.db_manager.execute(query)
        menu_items = []
        for row in cursor:
            menu_items.append(MenuItem(row[0], row[1], row[2], row[3]))
        return menu_items
