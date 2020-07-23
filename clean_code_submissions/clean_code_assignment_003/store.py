class Item:
    def __init__(self, name="", price=None, category=None):
        if price <= 0:
            raise ValueError("Invalid value for price, got {}".format(price))
        self._name = name
        self._price = price
        self._category = category
    @property
    def name(self):
        return self._name
    @property
    def price(self):
        return self._price
    @property
    def category(self):
        return self._category
    def __str__(self):
        return "{}@{}-{}".format(self.name, self.price, self.category)
class Query:
    def __init__(self, field=None, operation=None, value=None):
        if operation not in["IN", "EQ", "GT", "GTE", "LT",
                            "LTE", "STARTS_WITH", "ENDS_WITH", "CONTAINS"]:
            raise ValueError(f"Invalid value for operation, got {operation}")
        self._field = field
        self._operation = operation
        self._value = value
    @property
    def field(self):
        return self._field
    @property
    def operation(self):
        return self._operation
    @property
    def value(self):
        return self._value
    def __str__(self):
        return "{} {} {}".format(self.field, self.operation, self.value)
class Store:
    def __init__(self, items_list=None):
        if items_list is None:
            self.items_list = []
        else:
            self.items_list = items_list
    def __str__(self):
        if not self.items_list:
            return "No items"
        items = []
        for item in self.items_list:
            items.append(str(item))
        output = "\n".join(items)
        return output
    def add_item(self, item):
        if item not in self.items_list:
            self.items_list.append(item)
    def filter(self, query):
        query_result = []
        for item in self.items_list:
            item_value = getattr(item, query.field)
            item_exists = self.is_item_exists(query, item_value)
            if item_exists:
                query_result.append(item)
        return Store(query_result)
    @staticmethod
    def is_item_exists(query, item_value):
        if query.operation == "IN":
            result = item_value in query.value
        if query.operation == "EQ":
            result = item_value == query.value
        if query.operation == "GT":
            result = item_value > query.value
        if query.operation == "GTE":
            result = item_value >= query.value
        if query.operation == "LT":
            result = item_value < query.value
        if query.operation == "LTE":
            result = item_value <= query.value
        if query.operation == "STARTS_WITH":
            result = item_value.startswith(query.value)
        if query.operation == "ENDS_WITH":
            result = item_value.endswith(query.value)
        if query.operation == "CONTAINS":
            result = item_value.find(query.value) != -1
        return result
    def exclude(self, query):
        query_result = []
        filtered = self.filter(query)
        for item in self.items_list:
            if item not in filtered.items_list:
                query_result.append(item)
        return Store(query_result)
    def count(self):
        return len(self.items_list)
