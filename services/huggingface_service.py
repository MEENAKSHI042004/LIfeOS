import os
import requests


HF_API_TOKEN = os.getenv("HF_API_TOKEN")

API_URL = (
    "https://api-inference.huggingface.co/models/"
    "google/flan-t5-base"
)

headers = {
    "Authorization": f"Bearer {HF_API_TOKEN}"
}


def generate_ai_recommendation(
    prompt: str
) -> str:

    payload = {
        "inputs": prompt
    }

    try:

        response = requests.post(
            API_URL,
            headers=headers,
            json=payload,
            timeout=30
        )

        # DEBUGGING
        print("HF STATUS:", response.status_code)
        print("HF RESPONSE:", response.text)

        # If response empty
        if not response.text:
            return (
                "Stay focused on your goals "
                "and maintain healthy habits today."
            )

        result = response.json()

        # If model still loading
        if isinstance(result, dict):

            if "error" in result:

                return (
                    "AI model is warming up. "
                    "Focus on productivity and spending discipline today."
                )

        # Success
        return result[0]["generated_text"]

    except Exception as e:

        print("HF ERROR:", str(e))

        return (
            "Focus on completing your habits "
            "and reducing unnecessary spending today."
        )