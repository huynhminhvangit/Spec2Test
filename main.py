#!/usr/bin/env python3
"""
AutoTestcase Generator - Main Entry Point

This CLI tool reads requirement documents and generates manual test cases
using AI engines (OpenAI GPT or Google Gemini).
"""

import argparse
import sys
from pathlib import Path
from typing import Optional

import yaml

from extract_text import extract_text_from_file
from ai_engines.openai_engine import OpenAIEngine
from ai_engines.gemini_engine import GeminiEngine
from export_excel import save_testcases_to_excel


def load_config(config_path: str = "config.yaml") -> dict:
    """Load configuration from YAML file."""
    try:
        with open(config_path, 'r', encoding='utf-8') as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        print(f"❌ Configuration file '{config_path}' not found.")
        sys.exit(1)
    except yaml.YAMLError as e:
        print(f"❌ Error parsing configuration file: {e}")
        sys.exit(1)


def get_ai_engine(config: dict):
    """Initialize the appropriate AI engine based on configuration."""
    engine_type = config.get('ai_engine', 'openai').lower()
    
    if engine_type == 'openai':
        openai_config = config.get('openai', {})
        return OpenAIEngine(
            api_key=openai_config.get('api_key'),
            model=openai_config.get('model', 'gpt-4')
        )
    elif engine_type == 'gemini':
        gemini_config = config.get('gemini', {})
        return GeminiEngine(
            api_key=gemini_config.get('api_key'),
            model=gemini_config.get('model', 'gemini-pro')
        )
    else:
        print(f"❌ Unsupported AI engine: {engine_type}")
        sys.exit(1)


def main():
    """Main function to orchestrate the test case generation process."""
    parser = argparse.ArgumentParser(
        description="Generate test cases from requirement documents using AI"
    )
    parser.add_argument(
        "input_file",
        help="Path to the requirement document (PDF, DOCX, or TXT)"
    )
    parser.add_argument(
        "-o", "--output",
        default="testcases.xlsx",
        help="Output Excel file path (default: testcases.xlsx)"
    )
    parser.add_argument(
        "-c", "--config",
        default="config.yaml",
        help="Configuration file path (default: config.yaml)"
    )
    
    args = parser.parse_args()
    
    # Validate input file
    input_path = Path(args.input_file)
    if not input_path.exists():
        print(f"❌ Input file '{args.input_file}' not found.")
        sys.exit(1)
    
    print(f"📖 Reading requirement document: {args.input_file}")
    
    try:
        # Extract text from the document
        text_content = extract_text_from_file(args.input_file)
        if not text_content.strip():
            print("❌ No text content found in the document.")
            sys.exit(1)
        
        print(f"✅ Extracted {len(text_content)} characters from document")
        
        # Load configuration and initialize AI engine
        config = load_config(args.config)
        ai_engine = get_ai_engine(config)
        
        print(f"🤖 Using AI engine: {config.get('ai_engine', 'openai')}")
        
        # Generate test cases using AI
        print("🧪 Generating test cases...")
        testcases = ai_engine.generate_testcases(text_content)
        
        if not testcases:
            print("❌ No test cases were generated.")
            sys.exit(1)
        
        print(f"✅ Generated {len(testcases)} test cases")
        
        # Export to Excel
        print(f"💾 Saving test cases to: {args.output}")
        save_testcases_to_excel(testcases, args.output)
        
        print("🎉 Test case generation completed successfully!")
        
    except Exception as e:
        print(f"❌ Error during processing: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
