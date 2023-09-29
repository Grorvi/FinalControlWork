import uuid

from config import database
from models import Animal


class AnimalRepo:

    @staticmethod
    async def retrieve() -> list:
        _animal = []
        collection = database.get_collection('animal').find()
        async for animal in collection:
            _animal.append(animal)
        return _animal

    @staticmethod
    async def insert(animal: Animal) -> dict:
        _id = str(uuid.uuid4())
        birthday = f'{animal.birthday.day}.{animal.birthday.month}.{animal.birthday.year}'
        _animal = {
            '_id': _id,
            'name': animal.name,
            'birthday': birthday,
            'commands': animal.commands,
            'genus_name': animal.genus_name
        }
        await database.get_collection('animal').insert_one(_animal)

    async def update(self, _id: str, commands: str) -> dict | None:
        _animal = await self.retrieve_id(_id)
        if _animal is None:
            return None
        _animal['commands'] = commands
        await database.get_collection('animal').update_one({"_id": _id}, {"$set": _animal})
        return _animal

    @staticmethod
    async def retrieve_id(_id: str) -> dict | None:
        return await database.get_collection('animal').find_one({"_id": _id})

    async def delete(self, _id: str) -> bool:
        animal = await self.retrieve_id(_id)
        if animal is not None:
            await database.get_collection('animal').delete_one({"_id": _id})
            return True
        return False