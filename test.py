from backend.parser import Parser

class Main:
    def __init__(self) -> None:
        pass

    def parse_test(self):
        with open("lit.txt", "r") as file:
            data = file.readlines()

        print(data)

        for book in data:
            volume = Parser().get_data_obj(book, [",", "/", ";"])
            print(book)
            print(volume)
            print("\n")

clazz = Main()
clazz.parse_test()