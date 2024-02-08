from pydantic import BaseModel


#properties required during user creation

class Elf(BaseModel):
    id: int
    name: str
    country: str
    available: bool
class ElfCreate(BaseModel):
    name: str
    country: str
    pesel: str

class ElfDelete(BaseModel):
    id: int

