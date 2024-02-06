from pydantic import BaseModel, Field


#properties required during user creation
class ElfCreate(BaseModel):
    name: str
    Country: str