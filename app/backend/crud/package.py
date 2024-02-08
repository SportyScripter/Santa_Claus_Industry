from sqlalchemy.orm import Session
from app.backend.db.models.package import Package
from app.backend.schemas.package import PackageCreate
from app.backend.db.models.elf import Elf


def add_package(db: Session, package_data: PackageCreate):
    db_elf = Package(**package_data.dict())
    db.add(db_elf)
    db.commit()
    db.refresh(db_elf)
    return


def assign_elf_to_package(db: Session, package_id: int):
    package_to_assign = db.query(Package).filter(Package.id == package_id).first()
    if package_to_assign:
        elf_to_assign = db.query(Elf).filter(Elf.country == package_to_assign.country and Elf.available == True).first()
        if elf_to_assign:
            package_to_assign.elf_id = elf_to_assign.id
            db.query(Elf).filter(elf_to_assign.id == Elf.id).update({Elf.available: False})
            db.query(Package).filter(package_to_assign.id == Package.id).update({Package.status: "in progress"})
            db.commit()
            return {"message": "Elf successfully assigned to package"}
        else:
            return {"message": "No elf available for the package's country"}
    else:
        return {"message": "Package not found"}


def confirm_the_shipment_delivery(db: Session, package_id: int):
    package_to_confirm = db.query(Package).filter(Package.id == package_id).first()
    if package_to_confirm:
        db.query(Package).filter(package_to_confirm.id == Package.id).update({Package.status: "delivered"})
        db.query(Elf).filter(package_to_confirm.elf_id == Elf.id).update({Elf.available: True})
        db.commit()
        return {"message": "Package successfully delivered"}
    else:
        return {"message": "Package not found"}
    pass
