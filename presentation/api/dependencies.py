from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from infrastructure.repositories.sqlalchemy_vestuario_repository import SQLAlchemyVestuarioRepository
from core.application.use_cases.vestuario_use_case import VestuarioUseCase

engine = create_engine("sqlite:///./vestuarios.db")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_vestuario_use_case(db: Session = Depends(get_db)):
    repo = SQLAlchemyVestuarioRepository(db)
    return VestuarioUseCase(repo)