
class ModelDatabaseFascade():
    def __init__(self):
        self.model = {}

    def get(self, k):
        print("model get {}".format(k))
        return self.model.get(k, False)

    def set(self, k, v):
        print("model set({}, {})".format(k, v))
        self.model[str(k)] = v

    def delete(self, k):
        print("model delete {}".format(k))
        del self.model[str(k)]

    def quit(self):
        pass

    def begin(self):
        pass

    def commit(self):
        pass

    def teardown(self):
        pass




