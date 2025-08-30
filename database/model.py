from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class BasePromptResponse(Base):
    __tablename__ = "base_prompt_response"
    id = Column(Integer, primary_key=True, index=True)
    prompt = Column(String, nullable=False)
    response = Column(String, nullable=False)
    is_used = Column(Boolean, default=False, index=True)
