import sys
from transformers import GPTNeoForCausalLM, GPT2Tokenizer

#tokenizer = GPT2Tokenizer.from_pretrained("EleutherAI/gpt-neo-125M")
#model = GPTNeoForCausalLM.from_pretrained("EleutherAI/gpt-neo-125M")

tokenizer = GPT2Tokenizer.from_pretrained("EleutherAI/gpt-neo-1.3B")
model = GPTNeoForCausalLM.from_pretrained("EleutherAI/gpt-neo-1.3B")

if len(sys.argv) < 2:
    print("Usage: python3 gpt.py <prompt>")
    exit(1)

prompt = sys.argv[1]
input_ids = tokenizer.encode(prompt, return_tensors='pt')

sample_outputs = model.generate(
    input_ids,
    do_sample=True,
    max_length=100,
    top_p=0.95,
    top_k=50,
    pad_token_id=model.config.eos_token_id
)

generated_text = tokenizer.decode(sample_outputs[0], skip_special_tokens=True)

print(generated_text.encode('utf-8').decode())
