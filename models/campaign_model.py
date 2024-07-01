from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Campaign(Base):
    __tablename__ = "tb_campaign"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    name = Column(String(200))
    description = Column(String(500))
    is_active = Column(Boolean, default=True)
    
