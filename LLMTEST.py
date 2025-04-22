import time
import json
import pandas as pd
import PyPDF2
import tiktoken
import psutil
from memory_profiler import memory_usage

# Function to measure token count
def count_tokens(text):
    enc = tiktoken.get_encoding("cl100k_base")  # OpenAI's token encoder
    return len(enc.encode(text))

# Function to measure processing time and memory usage
def measure_performance(file_path, read_function):
    start_time = time.time()
    mem_before = psutil.Process().memory_info().rss  # Memory before
    content = read_function(file_path)
    mem_after = psutil.Process().memory_info().rss  # Memory after
    processing_time = time.time() - start_time
    memory_used = (mem_after - mem_before) / (1024 * 1024)  # Convert to MB
    token_count = count_tokens(content)
    return processing_time, memory_used, token_count

# Functions to read different file types
def read_txt(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

def read_json(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return json.dumps(json.load(file))

def read_csv(file_path):
    df = pd.read_csv(file_path)
    return df.to_csv(index=False)

def read_pdf(file_path):
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        return " ".join([page.extract_text() for page in reader.pages if page.extract_text()])

# File paths (update with your actual files)
files = {
    "TXT": "sample.txt",
    "JSON": "sample.json",
    "CSV": "sample.csv",
    "PDF": "sample.pdf",
}

# Measure performance for each file type
results = {}
for file_type, path in files.items():
    read_function = globals()[f"read_{file_type.lower()}"]
    results[file_type] = measure_performance(path, read_function)

# Print results
for file_type, (time_taken, memory_used, token_count) in results.items():
    print(f"{file_type} - Time: {time_taken:.4f}s, Memory: {memory_used:.4f}MB, Tokens: {token_count}")
