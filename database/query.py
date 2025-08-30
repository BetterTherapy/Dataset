from .session import session
from .model import BasePromptResponse
from sqlalchemy.orm import Session


@session
def add_base_prompt_response(
    session: Session, base_prompt_response: BasePromptResponse
):
    session.add(base_prompt_response)
    session.commit()
