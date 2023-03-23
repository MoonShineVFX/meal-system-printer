from typing import Tuple, List
from pydantic import BaseModel
from datetime import datetime
import logging
import os


class LabelArgs(BaseModel):
    order_id: int
    date: datetime
    index: Tuple[int, int]
    name: str
    options: List[str]
    user: str


IS_DEBUG = os.getenv("DEBUG", "").lower() == "true"

if IS_DEBUG:
    logging.basicConfig(level=logging.DEBUG)
