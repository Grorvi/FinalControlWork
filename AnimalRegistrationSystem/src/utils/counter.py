class Counter:
    def __init__(self):
        self.__count = 1

    async def add(self):
        self.__count += 1

    async def get_count(self):
        return self.__count
    