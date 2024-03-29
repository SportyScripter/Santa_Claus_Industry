from fastapi import FastAPI , HTTPException
from app.backend.core.config import settings
from app.backend.db.session import engine , SessionLocal
from app.backend.db.base import Base
from app.backend.routes.elves import elf_router as elf_router
from app.backend.routes.packages import package_router as package_router
from fastapi.middleware.cors import CORSMiddleware

def create_tables():
    try:
        Base.metadata.create_all(bind=engine)
        print("Tables created successfully and updated if necessary.")
    except Exception as e:
        print("Error creating tables:", e)


def start_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=False,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    create_tables()
    return app

app = start_application()


app.include_router(elf_router)
app.include_router(package_router)
