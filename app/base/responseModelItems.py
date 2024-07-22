from pydantic import BaseModel
from typing import List


class responseModelItems(BaseModel):
    items: List
