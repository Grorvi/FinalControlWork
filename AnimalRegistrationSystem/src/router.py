from typing import Annotated

from fastapi import Query
from fastapi.routing import APIRoute

import logs.logger as logger
from utils.crud import AnimalRepo
from models import Response, Animal
import utils.counter as counter_class

ERROR_MESSAGE_BY_ID = "No animal with this _id"
COUNTER = counter_class.Counter()

log = logger.BaseLogger(__name__)


async def get_animals():
    """Получить список всех животных """
    _animals_list = await AnimalRepo.retrieve()
    size = len(_animals_list)
    if size < 0:
        log.logger.info(f'[get_animals] No data in db. Return - {size} objects ')
        return Response(code=200, status="Ok", message="Success retrieve all data", result=_animals_list).dict(
            exclude_none=True)
    log.logger.info(f'[get_animals] Return - {size} objects')
    return Response(code=200, status="Ok", message="No data", result=_animals_list).dict(
        exclude_none=True)


async def create_animal(animal: Animal):
    """Добавить новое животное"""
    count = await COUNTER.get_count()
    await AnimalRepo.insert(animal)
    result = {'count': count}
    await COUNTER.add()
    log.logger.info(f'[create_animal] Animal successfully created. Data: {animal.dict()}')
    return Response(code=200, status="Ok", message="Success save data", result=result).dict(exclude_none=True)


async def get_animal_by_id(_id: str):
    """Получить животное по _id"""
    _animal = await AnimalRepo.retrieve_id(_id)
    if _animal is not None:
        log.logger.info(f'{ERROR_MESSAGE_BY_ID} - {_id}')
        return Response(code=200, status="Ok", message="Success retrieve data", result=_animal).dict(exclude_none=True)
    log.logger.info(f'Return - {_animal}')
    return Response(code=200, status="Ok", message=ERROR_MESSAGE_BY_ID, result=_animal).dict(exclude_none=True)


async def animal_update(
        _id: str,
        commands: Annotated[str | None, Query(max_length=50, description="Commands the animal knows")] = None):
    """Обновить информацию о животном"""
    result = await AnimalRepo().update(_id, commands)
    if result is not None:
        log.logger.info(f'{ERROR_MESSAGE_BY_ID} - {_id}')
        return Response(code=200, status="Ok", message="Success update data", result=result).dict(exclude_none=True)
    log.logger.info(f'Updated commands for {_id}\n Commands {commands}')
    return Response(code=200, status="Ok", message=ERROR_MESSAGE_BY_ID).dict(exclude_none=True)


async def animal_delete(_id: str):
    """Удалить животное"""
    is_delete = await AnimalRepo().delete(_id)
    log.logger.info(f'[animal_delete] Removed animal from id: {_id}. is_delete - {is_delete}')
    if is_delete:
        return Response(code=200, status="Ok", message="Success delete data").dict(exclude_none=True)
    return Response(code=200, status="Ok", message=ERROR_MESSAGE_BY_ID).dict(exclude_none=True)


routes = [
    APIRoute(path="/animal/", endpoint=get_animals, methods=["GET"]),
    APIRoute(path="/animal/{id}", endpoint=get_animal_by_id, methods=["GET"]),
    APIRoute(path="/animal", endpoint=create_animal, methods=["POST"]),
    APIRoute(path="/animal/update", endpoint=animal_update, methods=['PUT']),
    APIRoute(path="/animal/{id}", endpoint=animal_delete, methods=['DELETE']),
]