from dataclasses import dataclass, astuple
from pydantic import BaseModel


# define all types here

class ReceiptParameter(BaseModel):
    parameter: str
    axis: dict
    file: str

