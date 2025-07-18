# 🤖 AutoTestcase Generator

A Python CLI tool that automatically generates manual test cases from software requirement documents using AI (OpenAI GPT or Google Gemini).

## 🚀 Features

- 📥 **Multi-format Support**: Read requirements from PDF, DOCX, and TXT files
- 🤖 **AI-Powered**: Use OpenAI GPT or Google Gemini for intelligent test case generation
- 📊 **Excel Output**: Generate structured test cases in Excel format
- ⚙️ **Configurable**: Easy configuration via YAML file
- 🧪 **Comprehensive**: Generate positive, negative, and edge case scenarios

## 📦 Installation

1. Clone the repository:
```bash
git clone https://github.com/huynhminhvangit/Spec2Test.git
cd Spec2Test
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure your API keys in `config.yaml`:
```yaml
ai_engine: openai  # or 'gemini'

openai:
  api_key: "your-openai-api-key-here"
  model: "gpt-4"

gemini:
  api_key: "your-gemini-api-key-here"
  model: "gemini-pro"
```

## 🛠 Usage

### Basic Usage

```bash
python main.py path/to/requirements.docx
```

### Advanced Usage

```bash
# Specify output file
python main.py requirements.pdf -o my_testcases.xlsx

# Use custom config file
python main.py requirements.txt -c custom_config.yaml

# Full example
python main.py docs/requirements.docx -o testcases/sprint1_tests.xlsx -c config/prod_config.yaml
```

### Command Line Options

- `input_file`: Path to requirement document (PDF, DOCX, or TXT)
- `-o, --output`: Output Excel file path (default: testcases.xlsx)
- `-c, --config`: Configuration file path (default: config.yaml)

## 📁 Project Structure

```
auto_testcase_generator/
├── main.py                 # Entry point
├── config.yaml            # Configuration file
├── requirements.txt       # Python dependencies
├── extract_text.py        # Document text extraction
├── export_excel.py        # Excel export functionality
├── ai_engines/
│   ├── __init__.py
│   ├── openai_engine.py   # OpenAI integration
│   └── gemini_engine.py   # Google Gemini integration
└── README.md
```

## 🔧 Configuration

### AI Engine Selection

Choose between OpenAI and Google Gemini in `config.yaml`:

```yaml
ai_engine: openai  # or 'gemini'
```

### API Keys

Get your API keys from:
- **OpenAI**: https://platform.openai.com/api-keys
- **Google Gemini**: https://makersuite.google.com/app/apikey

## 📊 Output Format

The tool generates an Excel file with the following columns:

| Column | Description |
|--------|-------------|
| Test ID | Unique test identifier (TC001, TC002, etc.) |
| Feature | Feature/functionality being tested |
| Test Case Title | Descriptive title of the test case |
| Test Steps | Step-by-step instructions |
| Expected Result | Expected outcome |
| Priority | Test priority (High/Medium/Low) |
| Status | Test execution status (Not Executed by default) |
| Actual Result | Space for actual test results |
| Notes | Additional notes |

## 🧪 Example

### Input (requirements.txt):
```
User Login Feature:
- Users must be able to log in with email and password
- System should validate credentials against database
- Invalid login attempts should display error message
- Users should be redirected to dashboard after successful login
```

### Output (testcases.xlsx):
- TC001: Verify successful login with valid credentials
- TC002: Verify login failure with invalid email
- TC003: Verify login failure with invalid password
- TC004: Verify error message display for invalid credentials
- TC005: Verify dashboard redirection after successful login

## 🔍 Troubleshooting

### Common Issues

1. **Import Errors**: Make sure all dependencies are installed
   ```bash
   pip install -r requirements.txt
   ```

2. **API Key Errors**: Verify your API keys are correctly set in `config.yaml`

3. **File Format Errors**: Ensure your input file is in supported format (PDF, DOCX, TXT)

4. **Empty Output**: Check if the requirement document contains readable text

### Supported File Formats

- ✅ PDF files (via PyPDF2)
- ✅ DOCX files (via python-docx)
- ✅ TXT files (UTF-8 and Latin-1 encoding)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## �‍💻 Author

**Huynh Minh Vang**
- GitHub: [@huynhminhvangit](https://github.com/huynhminhvangit)
- Email: huynhminhvang.it@gmail.com

## �📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Copyright (c) 2025 Huynh Minh Vang

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## 💰 Support the Project

If this project helps you save time and improves your testing workflow, consider supporting the development:

### 🏦 Bank Transfer (Vietnam)
- **Bank**: ACB (Asia Commercial Bank)
- **Account Number**: 4278361
- **Account Name**: HUYNH MINH VANG

### ☕ Other Ways to Support
- ⭐ Star this repository
- 🐛 Report bugs and issues
- 💡 Suggest new features
- 🤝 Contribute code improvements

Your support helps maintain and improve this project for the community!

## 🙋‍♂️ Support

For issues and questions:
1. Check the troubleshooting section
2. Review existing issues on GitHub
3. Create a new issue with detailed information

---

Made with ❤️ by [Huynh Minh Vang](https://github.com/huynhminhvangit)
