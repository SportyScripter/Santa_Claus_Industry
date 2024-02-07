from sqlalchemy.orm import Session
from app.backend.db.models.elf import Elf
from app.backend.schemas.elf import ElfCreate
def create_elf(db: Session, elf_data: ElfCreate):
    db_elf = Elf(**elf_data.dict())
    db.add(db_elf)
    db.commit()
    db.refresh(db_elf)
    return db_elf


def delete_elf(db: Session, elf_id: int):
    db.query(Elf).filter(Elf.id == elf_id).delete()
    db.commit()
    return {"message": "Elf deleted successfully"}