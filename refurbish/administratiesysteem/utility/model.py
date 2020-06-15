from firebase import firebase


class Model:
    table_name = None
    database_name = None

    def __init__(self):
        self.database = firebase.FirebaseApplication(self.database_name, None)
        self.table = self.database.get(f'{self.table_name}', '')

    def all(self):
        table_dictionary = {}
        container = []
        counter = 0

        if self.table:
            for key, value in self.table.items():
                table_dictionary[int(counter)] = value
                counter += 1

            for item in table_dictionary.values():
                container.append(item)

        return container

    def create(self, data):
         self.database.post(f'{self.table_name}/', data)

    def delete(self, key, value):
        for k, v in self.table.items():
            if v[key] == value:
                self.database.delete(f'{self.table_name}/', k)

    def update(self, key, value, context):
        for k, v in self.table.items():
            if v[key] == value:
                for k_context, v_context in context.items():
                    self.database.put(f'{self.table_name}/{k}', k_context, v_context)

    def where(self, key, value):
        table = self.all()
        container = {}

        for item in table:
            if item[key] == value:
                container = item

        return container

    def primary_key(self, primary_key):
        table = self.all()
        key = 1

        if table:
            for item in table:
                if item[primary_key] > key:
                    key = item[primary_key]
                else:
                    key += 1

        return key



