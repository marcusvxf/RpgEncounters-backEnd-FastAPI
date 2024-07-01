from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Encounter(Base):
    __tablename__ = "tb_encounters"

    id = Column(Integer, primary_key=True)
    name = Column(String(200), unique=True, index=True)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")
    
