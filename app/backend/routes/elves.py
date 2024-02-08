from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from app.backend.crud.elf import create_elf, delete_elf, check_if_elf_exists, go_on_holiday, get_elf_pesel, \
    change_available_status
from app.backend.schemas.elf import ElfCreate, ElfDelete
from app.backend.db.models.elf import Elf
from app.backend.db.session import get_db

elf_router = APIRouter()


@elf_router.post("/elves/add_elf/{name}/{country}/{pesel}")
def create_elf_from_params(name: str, country: str, pesel: str, db: Session = Depends(get_db)):
    try:
        if check_if_elf_exists(db, pesel):
            raise HTTPException(status_code=400, detail="Elf already exists")
        if len(pesel) != 11:
            raise HTTPException(status_code=400, detail="PESEL number must be 11 digits long")
        if not name:
            raise HTTPException(status_code=400, detail="Name cannot be empty")
        for _ in pesel:
            if not _.isdigit():
                raise HTTPException(status_code=400, detail="PESEL must contain only digits")
        for _ in name:
            if not _.isalpha() and _ != " ":
                raise HTTPException(status_code=400, detail="Name must contain only letters and spaces")
        for _ in country:
            if not _.isalpha() and _ != " ":
                raise HTTPException(status_code=400, detail="Country must contain only letters and spaces")
        elf_data = ElfCreate(name=name, country=country, pesel=pesel)
        created_elf = create_elf(db=db, elf_data=elf_data)
        return created_elf
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@elf_router.delete("/elves/delete_elf/{elf_id}")
def delete_delete_elf(elf_id: int, db: Session = Depends(get_db)):
    delete_elf(db, elf_id)
    return {"message": "Elf deleted successfully"}


@elf_router.put("/elves/go_on_holidays/{elf_id}/{duration_time}")
def go_on_holiday_from_params(elf_id: int, duration_time: int, db: Session = Depends(get_db)):
    return go_on_holiday(db, elf_id, duration_time)


@elf_router.get("/elves/get_pesel/{elf_id}")
def get_elf_pesel_from_params(elf_id: int, db: Session = Depends(get_db)):
    return get_elf_pesel(db, elf_id)


@elf_router.put("/elves/change_status/{elf_id}/{status}")
def change_available_status_from_params(elf_id: int, status: bool, db: Session = Depends(get_db)):
    return change_available_status(db, elf_id, status)
