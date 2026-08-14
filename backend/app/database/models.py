from datetime import datetime

from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Text,
)
from sqlalchemy.orm import relationship

from app.database.base import Base


class Content(Base):
    __tablename__ = "content"

    # 내부 PK
    id = Column(Integer, primary_key=True, index=True)

    # 출처
    source = Column(String(100), nullable=False)          # inu, k-startup, q-net ...
    source_id = Column(String(100), nullable=False, index=True)

    # 데이터 종류
    content_type = Column(String(50), nullable=False)
    # notice
    # scholarship
    # event
    # certification
    # startup
    # recruitment
    # ...

    # 기본 정보
    title = Column(String(500), nullable=False)
    author = Column(String(200))
    organization = Column(String(200))
    category = Column(String(200))
    target = Column(String(500))

    view_count = Column(Integer)

    posted_at = Column(DateTime)
    updated_source_at = Column(DateTime)

    start_at = Column(DateTime)
    end_at = Column(DateTime)

    content = Column(Text)
    
    summary = Column(Text)

    url = Column(String(1000), nullable=False)

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )

    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False,
    )

    attachments = relationship(
        "Attachment",
        back_populates="content",
        cascade="all, delete-orphan",
    )


class Attachment(Base):
    __tablename__ = "attachment"

    id = Column(Integer, primary_key=True)

    content_id = Column(
        Integer,
        ForeignKey("content.id", ondelete="CASCADE"),
        nullable=False,
    )

    file_name = Column(String(500), nullable=False)

    download_url = Column(String(1000), nullable=False)

    content = relationship(
        "Content",
        back_populates="attachments",
    )