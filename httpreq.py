import asyncio
import aiohttp
import json

async def send_message_to_llama(message, api_key):
    url = 'http://127.0.0.1:8000/process/'
    async with aiohttp.ClientSession() as session:
        try:
            payload = json.dumps({"message": message})
            headers = {
                'Content-Type': 'application/json',
                'access_token': api_key  # Include the API key in the request headers
            }

            async with session.post(url, data=payload, headers=headers) as response:
                if response.status == 200:
                    data = await response.json()
                    return data['response']
                else:
                    return f"Error: Server responded with status code {response.status}"
        except Exception as e:
            return f"Error: {str(e)}"

# Load API key from config.json
def load_api_key():
    with open('apiconfig.json', 'r') as file:
        config = json.load(file)
        return config.get('API_KEY')

# Example usage
async def main():
    api_key = load_api_key()
    response = await send_message_to_llama("Hello, Llama!", api_key)
    print(response)

if __name__ == "__main__":
    asyncio.run(main())