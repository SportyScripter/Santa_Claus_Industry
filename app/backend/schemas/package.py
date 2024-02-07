from pydantic import BaseModel

class PackageBase(BaseModel):
    name : str
    weight : int
    delivery_address : str

class PackageCreate(PackageBase):
    pass

class Package(PackageBase):
    id : int
    class Config:
        orm_mode = True