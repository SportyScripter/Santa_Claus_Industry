from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from app.backend.crud.package import add_package, assign_elf_to_package, confirm_the_shipment_delivery
from app.backend.schemas.package import PackageCreate
from app.backend.db.models.package import Package
from app.backend.db.session import get_db

package_router = APIRouter()


@package_router.post("/package/add_package/{recipient_name}/{recipient_surname}/{weight}/{country}/{delivery_address}")
def create_package_from_params(recipient_name: str, recipient_surname: str, weight: int,
                               country: str, delivery_address: str, db: Session = Depends(get_db)):
    try:
        package_data = PackageCreate(recipient_name=recipient_name, recipient_surname=recipient_surname, weight=weight,
                                     country=country, delivery_address=delivery_address)
        created_package = add_package(db=db, package_data=package_data)
        return created_package
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@package_router.put("/package/assign_elf_to_package/{package_id}")
def assign_package(package_id: int, db: Session = Depends(get_db)):
    assign_elf_to_package(db, package_id)
    return {"message": "package asigned successfully"}


@package_router.put("/package/delivered/{package_id}")
def confirm_delivery(package_id: int, db: Session = Depends(get_db)):
    confirm_the_shipment_delivery(db, package_id)
    return {"message": "package delivered successfully"}
