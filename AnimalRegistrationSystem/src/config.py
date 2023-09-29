import logging
import os

import motor.motor_asyncio
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO, filename="", filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")

log = logging.getLogger(__name__)

MONGO_DB = os.getenv("MONGODB_URL")

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DB)

database = client.python_db