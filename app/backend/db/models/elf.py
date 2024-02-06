from app.backend.db.base_class import Base
from sqlalchemy import Column , Boolean, Integer, String, ForeignKey, DateTime


class Elf(Base):
    id = Column(Integer, primary_key=True, index=True , autoincrement=True)
    name = Column(String, nullable=False, unique=True, index=True)
    Country = Column(String, nullable=False)
    available = Column(Boolean(), default=False)
