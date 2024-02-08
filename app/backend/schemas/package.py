from pydantic import BaseModel

class PackageCreate(BaseModel):
    recipient_name: str
    recipient_surname: str
    weight: int
    country: str
    delivery_address: str


