from app.backend.db.base_class import Base
from sqlalchemy import Column, Boolean, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship


class Package(Base):
    __tablename__ = "packages"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    recipient_name = Column(String, nullable=False, index=True)
    recipient_surname = Column(String, nullable=False, index=True)
    weight = Column(Integer, nullable=False)
    country = Column(String, nullable=False)
    delivery_address = Column(String, nullable=False)
    status = Column(String, nullable=False, default="in warehouse", index=True)
    elf_id = Column(Integer, ForeignKey("elves.id"))
    elf = relationship("Elf", back_populates="packages")

    class Config:
        orm_mode = True
