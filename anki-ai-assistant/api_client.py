"""
API Client for communicating with AI providers (Anthropic Claude)
"""

import json
import urllib.request
import urllib.error


def estimate_tokens(text):
    """Rough estimation of tokens (4 chars ≈ 1 token)."""
    return len(text) // 4


def call_ai_api(prompt, api_key, model="claude-sonnet-4-20250514", max_tokens=1024):
    """
    Call Anthropic Claude API.

    Args:
        prompt: The prompt to send
        api_key: Anthropic API key
        model: Model to use
        max_tokens: Maximum response tokens

    Returns:
        String response from AI

    Raises:
        Exception: If API call fails
    """
    if not api_key:
        raise Exception("No API key configured")

    # Prepare request
    url = "https://api.anthropic.com/v1/messages"

    headers = {
        "Content-Type": "application/json",
        "x-api-key": api_key,
        "anthropic-version": "2023-06-01"
    }

    data = {
        "model": model,
        "max_tokens": max_tokens,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    # Make request
    try:
        req = urllib.request.Request(
            url,
            data=json.dumps(data).encode('utf-8'),
            headers=headers,
            method='POST'
        )

        with urllib.request.urlopen(req, timeout=30) as response:
            response_data = json.loads(response.read().decode('utf-8'))

            # Extract text from response
            if 'content' in response_data and len(response_data['content']) > 0:
                return response_data['content'][0]['text']
            else:
                raise Exception("Unexpected response format")

    except urllib.error.HTTPError as e:
        error_body = e.read().decode('utf-8')
        try:
            error_data = json.loads(error_body)
            error_msg = error_data.get('error', {}).get('message', str(e))
        except:
            error_msg = f"HTTP {e.code}: {error_body}"

        if e.code == 401:
            raise Exception("Invalid API key. Please check your API key in settings.")
        elif e.code == 429:
            raise Exception("Rate limit exceeded. Please try again in a moment.")
        else:
            raise Exception(f"API Error: {error_msg}")

    except urllib.error.URLError as e:
        raise Exception(f"Network error: {str(e)}. Please check your internet connection.")

    except json.JSONDecodeError as e:
        raise Exception(f"Invalid response from API: {str(e)}")

    except Exception as e:
        raise Exception(f"Unexpected error: {str(e)}")


def test_api_key(api_key, model="claude-sonnet-4-20250514"):
    """
    Test if API key is valid.

    Returns:
        (bool, str): (success, message)
    """
    try:
        response = call_ai_api(
            "Say 'API key is working!' and nothing else.",
            api_key,
            model,
            max_tokens=50
        )
        if "working" in response.lower():
            return True, "API key is valid!"
        else:
            return True, f"API key works! Response: {response[:50]}"
    except Exception as e:
        return False, str(e)
