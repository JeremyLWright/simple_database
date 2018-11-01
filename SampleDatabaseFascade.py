import pickledb
import tempfile

class SampleDatabaseFascade():
    def __init__(self):
        self.temp = tempfile.mktemp()
        self.database = pickledb.load(self.temp, False)

    def get(self, k):
        print("uut get {}".format(k))
        return self.database.get(k)

    def set(self, k, v):
        print("uut set({}, {})".format(k, v))
        self.database.set(str(k), v)

    def delete(self, k):
        print("uut delete {}".format(k))
        self.database.rem(str(k))

    def quit(self):
        pass

    def begin(self):
        pass

    def commit(self):
        pass

    def teardown(self):
        pass




