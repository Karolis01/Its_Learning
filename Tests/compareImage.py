import hashlib


class Comparing:

    def hash_it(self, path):
        with open(path, 'rb') as f:
            hasher = hashlib.md5()
            hasher.update(f.read())
            return hasher.hexdigest()

    def do_compare(self, name1, name2):
        directory = "/Users/karolis/Documents/pythonProject/Its_Learning/Tests/Screen"
        image1 = "{}/{}".format(directory, name1)
        image2 = "{}/{}".format(directory, name2)

        screenshot1 = self.hash_it(image1)
        screenshot2 = self.hash_it(image2)
        assert screenshot1 == screenshot2, "Image HASH do not match. {} vs {}".format(screenshot1, screenshot2)

