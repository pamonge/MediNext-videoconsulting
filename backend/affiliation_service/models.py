from sqlalchemy import Column, Integer, String, Date, ForeignKey, Enum
from database import Base
import enum

class StatusEnum(str, enum.Enum):
    vigente = "v"
    sin_cobertura = "c"

class RelationshipEnum(str, enum.Enum):
    titular = "t"
    familiar = "f"

class Affiliation(Base):
    __tablename__ = "affiliate"

    affiliate_id = Column(Integer, primary_key=True, index=True)
    beneficiary = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    discharge_date = Column(Date)
    plan_id = Column() #models.ForeignKey("plan.id", on_delete=models.CASCADE) Todavia no está "plan"
    status = Column(Enum(StatusEnum))
    relationship = Column(Enum(RelationshipEnum))

