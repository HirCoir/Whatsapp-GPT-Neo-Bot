from transformers import pipeline

generator = pipeline('text-generation', model='EleutherAI/gpt-neo-1.3B')
prompt = "Código php para extraer datos de una base de datos MySQL llamada datos donde la contraseña es pass123, el usuario es user123 y el host es 127.0.0.1, quiero que extraiga Username y Nivel"

generated_code = generator(prompt, max_length=900, do_sample=True, temperature=0.7)[0]['generated_text']

print(generated_code)
