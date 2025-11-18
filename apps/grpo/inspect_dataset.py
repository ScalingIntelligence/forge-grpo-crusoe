from datasets import load_dataset

# Login using e.g. `huggingface-cli login` to access this dataset
ds = load_dataset("POLARIS-Project/Polaris-Dataset-53K")

print(f"Dataset info: {ds}")
print(f"Example entry: {ds['train'][0]}")

ds_old = load_dataset("openai/gsm8k", "main", split="train")

print(f"Old Dataset info: {ds_old}")
print(f"Old Example entry: {ds_old[0]}")