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


def check_if_elf_exists(db: Session, elf_pesel: str):
    return db.query(Elf).filter(Elf.pesel == elf_pesel).first()


def go_on_holiday(db: Session, elf_id: int, duration_time: int):
    elf = db.query(Elf).filter(Elf.id == elf_id).first()
    if elf.vacation > duration_time:
        elf.vacation -= duration_time
        elf.available = False
        db.commit()
        return {"message": "Elf is on vacation"}
    else:
        return {f"message": "Elf does not have enough vacation days, he has {elf.vacation} days left"}

def get_elf_pesel(db: Session, elf_id: int):
    elf = db.query(Elf).filter(Elf.id == elf_id).first()
    if elf:
        return elf.pesel
    else:
        return {"message": "Elf not found"}

def change_available_status(db: Session, elf_id: int, status: bool):
    elf = db.query(Elf).filter(Elf.id == elf_id).first()
    if elf:
        elf.available = status
        db.commit()
        return {"message": "Elf status changed"}
    else:
        return {"message": "Elf not found"}
