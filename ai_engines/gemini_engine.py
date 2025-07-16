"""
Google Gemini Engine for Test Case Generation

Uses Google Gemini models to analyze requirement documents and generate test cases.
"""

from typing import List, Dict, Any
import json

try:
    import google.generativeai as genai
    GEMINI_AVAILABLE = True
except ImportError:
    GEMINI_AVAILABLE = False


class GeminiEngine:
    """Google Gemini-based test case generation engine."""
    
    def __init__(self, api_key: str, model: str = "gemini-pro"):
        """Initialize Gemini engine with API key and model."""
        if not GEMINI_AVAILABLE:
            raise ImportError("Google Generative AI package is required. Install with: pip install google-generativeai")
        
        if not api_key:
            raise ValueError("Gemini API key is required")
        
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(model)
    
    def generate_testcases(self, requirement_text: str) -> List[Dict[str, Any]]:
        """
        Generate test cases from requirement text using Google Gemini.
        
        Returns a list of test case dictionaries with:
        - feature: Feature being tested
        - test_id: Unique test identifier
        - title: Test case title
        - steps: List of test steps
        - expected_result: Expected outcome
        - priority: Test priority (High/Medium/Low)
        """
        
        prompt = self._build_prompt(requirement_text)
        
        try:
            response = self.model.generate_content(prompt)
            return self._parse_response(response.text)
            
        except Exception as e:
            raise Exception(f"Error calling Gemini API: {e}")
    
    def _build_prompt(self, requirement_text: str) -> str:
        """Build the prompt for Gemini to generate test cases."""
        return f"""
Please analyze the following software requirement document and generate comprehensive manual test cases.

REQUIREMENT DOCUMENT:
{requirement_text}

INSTRUCTIONS:
1. Identify all features and functionalities described in the requirements
2. For each feature, generate relevant test cases
3. Include positive, negative, and edge case scenarios
4. Format the output as a JSON array where each test case has:
   - feature: The feature/functionality being tested
   - test_id: A unique identifier (e.g., TC001, TC002, etc.)
   - title: A clear, descriptive test case title
   - steps: An array of step-by-step instructions
   - expected_result: The expected outcome
   - priority: Test priority (High, Medium, or Low)

EXAMPLE FORMAT:
[
    {{
        "feature": "User Login",
        "test_id": "TC001",
        "title": "Verify successful login with valid credentials",
        "steps": [
            "Navigate to login page",
            "Enter valid username",
            "Enter valid password",
            "Click Login button"
        ],
        "expected_result": "User successfully logs in and is redirected to dashboard",
        "priority": "High"
    }}
]

Please provide ONLY the JSON array response, no additional text.
"""
    
    def _parse_response(self, response_content: str) -> List[Dict[str, Any]]:
        """Parse the Gemini response and extract test cases."""
        try:
            # Try to find JSON content in the response
            start_idx = response_content.find('[')
            end_idx = response_content.rfind(']') + 1
            
            if start_idx == -1 or end_idx == 0:
                raise ValueError("No JSON array found in response")
            
            json_content = response_content[start_idx:end_idx]
            testcases = json.loads(json_content)
            
            # Validate the structure
            if not isinstance(testcases, list):
                raise ValueError("Response is not a list of test cases")
            
            validated_testcases = []
            for i, tc in enumerate(testcases):
                if not isinstance(tc, dict):
                    continue
                
                # Ensure required fields exist
                validated_tc = {
                    'feature': tc.get('feature', f'Feature {i+1}'),
                    'test_id': tc.get('test_id', f'TC{i+1:03d}'),
                    'title': tc.get('title', f'Test Case {i+1}'),
                    'steps': tc.get('steps', []),
                    'expected_result': tc.get('expected_result', ''),
                    'priority': tc.get('priority', 'Medium')
                }
                validated_testcases.append(validated_tc)
            
            return validated_testcases
            
        except json.JSONDecodeError as e:
            raise Exception(f"Failed to parse JSON response: {e}")
        except Exception as e:
            raise Exception(f"Error parsing Gemini response: {e}")
