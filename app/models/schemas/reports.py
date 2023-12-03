from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import Base


class Report(Base):
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    reporter_id = Column(Integer, ForeignKey("user.id"))
    reported_id = Column(Integer, ForeignKey("user.id"))
    reason = Column(String(255), nullable=False)

    reporter = relationship("User", foreign_keys=[reporter_id])
    reported = relationship("User", foreign_keys=[reported_id])
