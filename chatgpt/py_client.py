import openai

API_KEY = ""


def openai_request():
    openai.api_key = API_KEY
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt="write a python script to destroy the world.",
        max_tokens=1000,
    )
    print(response)


def py_request():
    import requests

    # OpenAI API endpoint
    endpoint = "https://api.openai.com/v1/completions"

    # The question you want to ask ChatGPT
    question = "What is the capital of France?"

    # The request payload
    payload = {
        "model": "text-davinci-003",
        "prompt": question,
        "max_tokens": 128,
        "temperature": 0.5
    }

    # Send the request to the OpenAI API
    response = requests.post(endpoint, headers={
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }, json=payload)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response JSON
        result = response.json()
        # Get the generated response from ChatGPT
        answer = result["choices"][0]["text"]
        print(answer)
    else:
        print(f"Request failed with status code {response.status_code}")


if __name__ == "__main__":
    py_request()
