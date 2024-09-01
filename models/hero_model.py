from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Hero(Base):
    __tablename__ = "tb_hero"

    id = Column(Integer, primary_key=True)
    level = Column(Integer)
    is_active = Column(Boolean, default=True)
    group_id = Column(Integer,ForeignKey("tb_group.id"))
    
    group = relationship("Group",back_populates="heroes")

