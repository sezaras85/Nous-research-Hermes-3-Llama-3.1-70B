import requests

API_KEY = 'YOUR_API_KEY'
API_URL = 'https://inference-api.nousresearch.com/v1/chat/completions'  

def hermes_query(prompt):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "Hermes-3-Llama-3.1-70B",
        "messages": [{"role": "user", "content": prompt}]
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()
        result = response.json()
        return result['choices'][0]['message']['content']
    except Exception as e:
        return f"Hata oluştu: {str(e)}"

def main():
    print("🔹 Hermes-3 Terminal Chatbot'a Hoş Geldin! (Çıkmak için: 'çık' yaz)")
    while True:
        prompt = input("\n👤 Sen: ")
        if prompt.lower() in ['çık', 'exit', 'quit']:
            print("🧠 Görüşmek üzere!")
            break
        reply = hermes_query(prompt)
        print(f"\n🤖 Hermes-3: {reply}")

if __name__ == "__main__":
    main()
