from datasets import load_dataset

# Login using e.g. `huggingface-cli login` to access this dataset
ds = load_dataset("POLARIS-Project/Polaris-Dataset-53K")

print(f"Dataset info: {ds}")
print(f"Example entry: {ds['train'][0]}")

ds_old = load_dataset("openai/gsm8k", "main", split="train")

print(f"Old Dataset info: {ds_old}")
print(f"Old Example entry: {ds_old[0]}")

aime_ds = load_dataset("opencompass/AIME2025", "AIME2025-I", split="test")
print(f"AIME Dataset info: {aime_ds}")
print(f"AIME Example entry: {aime_ds[0]}")
print(f"AIME Example question: {aime_ds[0]['question']}")
print(f"AIME Example answer: {aime_ds[0]['answer']}")