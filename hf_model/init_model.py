from transformers import AutoModelForCausalLM, AutoTokenizer
from config import config
import torch


def setup_model(model_name):
    model_name = model_name

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    if config.offload_to_cpu:
        max_memory = {
            0: config.vram_in_GiB + "GiB",
            "cpu": config.cpu_in_GiB + "GiB",
        }
        model = AutoModelForCausalLM.from_pretrained(
            model_name,
            device_map="auto",
            max_memory=max_memory,
            torch_dtype=torch.float16,
        )
    else:
        model = AutoModelForCausalLM.from_pretrained(model_name)
        if torch.cuda.is_available():
            model.to("cuda")
    model.eval()
    return model, tokenizer
