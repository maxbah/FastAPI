class RBItem:
    def __init__(self, item_id: int | None = None,
                 item_name: str = None,
                 item_description: str | None = None,
                 count: int = None,
                 price: int =  None):
        self.id = item_id
        self.item_name = item_name
        self.item_description = item_description
        self.count = count
        self.price = price

    def to_dict(self) -> dict:
        data = {'id': self.id, 'item_name': self.item_name,
                'item_description': self.item_description,
                'count': self.count,
                'price': self.price}
        # Создаем копию словаря, чтобы избежать изменения словаря во время итерации
        filtered_data = {key: value for key, value in data.items() if value is not None}
        return filtered_data
