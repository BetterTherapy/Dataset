from config import config
from database.model import BasePromptResponse
from database.query import add_base_prompt_response
from hf_model.generator import generate_response
from hf_model.init_model import setup_model
import logging
from rich.logging import RichHandler

# Configure logging with rich
logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    handlers=[RichHandler(rich_tracebacks=True)],
)
logger = logging.getLogger(__name__)


def main():
    model, tokenizer = setup_model(config.model_name)
    prompt = """<|begin_of_text|><|start_header_id|>system<|end_header_id|>  
    You are a compassionate mental health assistant.  
    Generate both a mental health question and its empathetic answer.  
    Respond **only** with a VALID JSON object that:  
    • Begins with `{` and ends with `}`  
    • Contains exactly two keys: "question" and "answer"  
    • Includes no additional text, comments, or formatting  
    Example:{"question":"<mental health question>","answer":"<empathetic answer>"}  
    <|eot_id|>  
    <|start_header_id|>assistant<|end_header_id|>{ 
    """
    for i in range(config.data_count):
        base_data = generate_response(prompt, model, tokenizer)
        prompt = base_data.get("question", None)
        base_response = base_data.get("answer", None)
        if not prompt or not base_response:
            logger.error(f"Invalid response format: {base_data}")
            continue
        base_prompt_response = BasePromptResponse(
            prompt=prompt,
            response=base_response,
        )
        add_base_prompt_response(base_prompt_response)
        logger.info(f"Successfully added {i + 1} base prompt response ")


if __name__ == "__main__":
    main()
