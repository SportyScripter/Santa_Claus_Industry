from app.backend.db.session import Base
from sqlalchemy import Column , Boolean, Integer, String, ForeignKey, DateTime


class Package(Base):
    __tablename__ = "packages"
    id = Column(Integer, primary_key=True, index=True , autoincrement=True)
    name = Column(String, nullable=False, unique=True, index=True)
    weight = Column(Integer, nullable=False)
    delivery_address = Column(String, nullable=False)
