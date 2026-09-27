from datetime import datetime

from sqlalchemy import DateTime, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.database.database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(120))
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    password_hash: Mapped[str] = mapped_column(String(255))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    wells: Mapped[list["Well"]] = relationship(back_populates="owner")
    reports: Mapped[list["Report"]] = relationship(back_populates="owner")


class Well(Base):
    __tablename__ = "wells"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    name: Mapped[str] = mapped_column(String(120))
    location: Mapped[str | None] = mapped_column(String(255), nullable=True)
    depth_start: Mapped[float | None] = mapped_column(Float, nullable=True)
    depth_end: Mapped[float | None] = mapped_column(Float, nullable=True)
    fmi_path: Mapped[str | None] = mapped_column(String(500), nullable=True)
    logs_path: Mapped[str | None] = mapped_column(String(500), nullable=True)

    owner: Mapped[User] = relationship(back_populates="wells")
    fractures: Mapped[list["Fracture"]] = relationship(back_populates="well")
    zones: Mapped[list["FaciesZone"]] = relationship(back_populates="well")
    sessions: Mapped[list["AnalysisSession"]] = relationship(back_populates="well")


class AnalysisSession(Base):
    __tablename__ = "analysis_sessions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    well_id: Mapped[int] = mapped_column(ForeignKey("wells.id"))
    status: Mapped[str] = mapped_column(String(32), default="idle")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    well: Mapped[Well] = relationship(back_populates="sessions")


class Fracture(Base):
    __tablename__ = "fractures"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    well_id: Mapped[int] = mapped_column(ForeignKey("wells.id"))
    depth: Mapped[float | None] = mapped_column(Float, nullable=True)
    tvd: Mapped[float | None] = mapped_column(Float, nullable=True)
    dip: Mapped[float | None] = mapped_column(Float, nullable=True)
    azimuth: Mapped[float | None] = mapped_column(Float, nullable=True)
    fracture_type: Mapped[str | None] = mapped_column(String(64), nullable=True)
    confidence: Mapped[float | None] = mapped_column(Float, nullable=True)

    well: Mapped[Well] = relationship(back_populates="fractures")


class FaciesZone(Base):
    __tablename__ = "facies_zones"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    well_id: Mapped[int] = mapped_column(ForeignKey("wells.id"))
    start_depth: Mapped[float] = mapped_column(Float)
    end_depth: Mapped[float] = mapped_column(Float)
    predicted_class: Mapped[str | None] = mapped_column(String(120), nullable=True)
    confidence: Mapped[float | None] = mapped_column(Float, nullable=True)

    well: Mapped[Well] = relationship(back_populates="zones")


class Report(Base):
    __tablename__ = "reports"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    well_id: Mapped[int] = mapped_column(ForeignKey("wells.id"))
    title: Mapped[str] = mapped_column(String(255))
    body: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    owner: Mapped[User] = relationship(back_populates="reports")
