# 🤖 Copilot Instructions for AutoTestcase Generator

This project is a **Python CLI tool** that reads a **requirement document** (PDF, DOCX, TXT), extracts **software features**, and then **automatically generates manual test cases** using either **OpenAI GPT** or **Google Gemini**.

---

## 🧠 Goal

Generate structured test cases in Excel format based on requirement documents.

- 📥 Input: Software specification in `.docx`, `.pdf`, or `.txt`
- 🧪 Output: Manual test cases with clear title, steps, and expected results
- ⚙️ Configurable AI engine via `config.yaml` (OpenAI or Gemini)
- 💾 Save output to `testcases.xlsx`

---

## ✅ Functional Flow

1. Read file → extract plain text
2. Analyze the text using an LLM (OpenAI or Gemini) to:
   - Detect features/functions
   - Generate test cases per feature
3. Output results to an Excel file using pandas

---

## 🧩 Project Structure
auto_testcase_generator/
├── main.py # Entry point
├── config.yaml # Selects OpenAI or Gemini engine
├── extract_text.py # Reads DOCX or PDF
├── ai_engines/
│ ├── openai_engine.py # Calls OpenAI API
│ └── gemini_engine.py # Calls Gemini API
├── export_excel.py # Writes testcases to Excel

## 🧑‍💻 Code Style Guidelines

- Python 3.9+
- Clear function names: `extract_text_from_docx`, `generate_testcases`
- Modular and reusable functions
- Use `pandas` for Excel generation
- Avoid hardcoded values — prefer configuration
- Support fallback if AI response is invalid
- Use f-strings and type hints

---

## 🛠 Sample config.yaml

```yaml
ai_engine: openai
openai:
  api_key: "sk-xxx"
  model: "gpt-4"
gemini:
  api_key: "AIza..."
  model: "gemini-pro"
```
