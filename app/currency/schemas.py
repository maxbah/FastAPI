from typing import List

from pydantic import BaseModel, ConfigDict


class Symbol(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    symbol: str


class Symbols(BaseModel):
    symbols: List[Symbol]
