# 🧪 File-type-Checker-for-LLM

This project benchmarks how efficiently different file types (.csv, .pdf, .json, .txt) are processed when used as input for a **Large Language Model (LLM)**. The goal is to determine **which format offers the fastest parsing and lowest latency**, helping optimize LLM pipelines.

---

## 📁 Project Structure

- `LLMTEST.py` – Main benchmarking script to test file parsing speeds.
- `Sample.csv` – Tabular data.
- `Sample.pdf` – Document-style data.
- `sample.json` – Structured data.
- `sample.txt` – Unstructured plain text.
- `README.md` – Project overview.

---

## 🔍 Objective

To find out:
> _"Which file format is processed most efficiently by an LLM model pipeline?"_

This can guide developers on what format to prefer for:
- Dataset ingestion
- Prompt engineering
- Document summarization
- Conversational agents

---

## 🚀 How to Run

```bash
# Clone the repo
git clone https://github.com/abhi2326/File-type-Checker-for-LLM.git

cd File-type-Checker-for-LLM

# Run the benchmarking script
python LLMTEST.py
```

---

## 📊 Output

The script logs the following:
- Time taken to load each file type
- Time taken to convert the content to LLM-compatible format
- Optional: Time taken to pass content to an LLM (if integrated)

Sample output:
```
Processing sample.txt... ✅ 0.013s
Processing sample.json... ✅ 0.020s
Processing Sample.csv... ✅ 0.032s
Processing Sample.pdf... ✅ 0.054s

Fastest format: .txt
```

---

## 💡 Why This Matters

Different file types have different parsing complexities. For example:
- `.txt` is fastest but unstructured.
- `.pdf` needs decoding and OCR in some cases.
- `.json` is structured and easy to parse.
- `.csv` is tabular and lightweight.

This tool helps decide **which format to use** when speed is critical in LLM applications.

---

## 👨‍💻 Author

**Abhijeet Srivastava**  and **Suavnsh Madaan**
🔗 [LinkedIn](https://www.linkedin.com/in/abhijeet-sri11/)  
📬 abhijeet.sri11@gmail.com  
