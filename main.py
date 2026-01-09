import sys
import json
from pydantic import BaseModel, Field
from typing import Optional , List
from google import genai
from google.genai import types


client = genai.Client(api_key="AIzaSyAxZMiqTnU4hHWmkJ8UqpOKkKYCy0KR_rM")
class Address(BaseModel):
    Country: Optional[str] = Field(default="N/A", description="Country name")
    street: Optional[str] = Field(default="N/A", description="Street or house info")
    city: Optional[str] = Field(default="N/A", description="City or locality")
    district: Optional[str] = Field(default=None, description="District or Zila if applicable")
    state: Optional[str] = Field(default="N/A", description="State or region")
    zip_code: Optional[str] = Field(default="N/A", description="Postal or Zip code")

def extract_address(text_input: str):
    system_instruction = (
        "You are an expert at parsing messy text into clean addresses. "
        "Extract every complete mailing address found. "
        "Return ONLY a valid JSON list of objects."
    )

    response = client.models.generate_content(
        model="gemini-2.0-flash-lite",
        contents=text_input,
        config=types.GenerateContentConfig(
            system_instruction=system_instruction,
            response_mime_type="application/json",
            response_schema=list[Address],
            temperature=0.0
        ),
    )
    return response.text

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_data = sys.argv[1]
        print(extract_address(input_data))



