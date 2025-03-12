import openai

openai.api_key = 'your api key'  # Replace with your actual API key

def get_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or another valid model like "gpt-4"
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"An error occurred: {e}"

# Test the function with an example
if __name__ == "__main__":
    print(get_response("Write a haiku about AI"))