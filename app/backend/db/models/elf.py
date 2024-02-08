from app.backend.db.base_class import Base
from sqlalchemy import Column , Boolean, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship


class Elf(Base):
    __tablename__ = "elves"
    id = Column(Integer, primary_key=True, index=True , autoincrement=True)
    name = Column(String, nullable=False, index=True)
    country = Column(String, nullable=False)
    available = Column(Boolean(), default=True)
    pesel = Column(String, nullable=False, unique=True, index=True)
    vacation = Column(Integer, default=26)
    packages = relationship("Package", back_populates="elf")
    class Config:
        orm_mode = True
