# app/database/models.py

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


class Notice(Base):
    __tablename__ = "notice"

    # 내부 PK
    id = Column(Integer, primary_key=True, index=True)

    # 학교 게시글 번호 (중복 검사 기준)
    notice_number = Column(Integer, unique=True, nullable=False, index=True)

    # 기본 정보
    title = Column(String(500), nullable=False)
    author = Column(String(100))
    target = Column(String(300))

    # 조회수
    view_count = Column(Integer, default=0)

    # 게시일
    posted_at = Column(DateTime)

    # 신청기간
    apply_start = Column(DateTime)
    apply_end = Column(DateTime)

    # 본문
    content = Column(Text, nullable=False)

    #요약
    summary = Column(Text)

    # 원문 URL
    url = Column(String(1000), nullable=False)

    # 생성/수정
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

    # 첨부파일
    attachments = relationship(
        "Attachment",
        back_populates="notice",
        cascade="all, delete-orphan",
    )


class Attachment(Base):
    __tablename__ = "attachment"

    id = Column(Integer, primary_key=True, index=True)

    notice_id = Column(
        Integer,
        ForeignKey("notice.id", ondelete="CASCADE"),
        nullable=False,
    )

    # 표시 이름
    file_name = Column(String(500), nullable=False)

    # 학교 다운로드 링크
    download_url = Column(String(1000), nullable=False)

    notice = relationship(
        "Notice",
        back_populates="attachments",
    )