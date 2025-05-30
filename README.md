<img width="1230" alt="image" src="https://github.com/sezaras85/Nous-research-Hermes-3-Llama-3.1-70B/blob/main/nous%20ekran.jpeg" />

# Nous-research-

Nous Research is a leader in the development of human-centric language models and simulators.  there primary focus areas include model architecture, data synthesis, fine-tuning, and reasoning, all aimed at aligning AI systems with real-world user experiences. its prioritize the development of open-source, human-compatible models, which challenge the conventional closed-model approach. 

This project started out of curiosity — to better understand how Hermes-3 might one day connect with the broader Nous Protocol, possibly through on-chain inference or smart contract integration.
Ideas, improvements, or just playing around? PRs welcome!
This repo is community-driven. Let's explore the future of decentralized AI together.

# 🧠 Hermes-3 Terminal Chatbot (Nous Research API)

A simple CLI-based chatbot using the powerful `Hermes-3-Llama3-70B` model from https://portal.nousresearch.com/api-keys
Built for testing, learning, and exploring the capabilities of Hermes-3 via its official inference API.


<img width="1230" alt="image" src="https://github.com/sezaras85/Nous-research-Hermes-3-Llama-3.1-70B/blob/main/nous%20ekran%201.png" />
---

## 🚀 Features

- Connects to Nous Hermes-3 via REST API
- Terminal-based question/answer interface
- Lightweight, no dependencies beyond `requests`
- Great for experimentation and early contributions to Nous ecosystem

---

## 📦 Requirements

- Python 3.7+
- A valid API key from [https://portal.nousresearch.com](https://portal.nousresearch.com)

---

## 🛠️ Installation


```bash
mkdir hermes-bot
cd hermes-bot
```

Install dependencies:

```bash

pip install requests
```

```bash

nano hermes_bot.py
```

```bash

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

```
Add your API key to YOUR_API_KEY (or use an .env file for security).

ctrl+O+ yes and save


🧪 How to Use

Run the bot with:

```bash
python bot.py
```

Then simply chat with the Hermes-3 model:

```bash
You: What is Nous Protocol?
Hermes-3: Nous Protocol is a decentralized knowledge infrastructure that...
```

🧩 Example Prompt (cURL)

You can also test your key directly via cURL:

```bash
curl https://inference-api.nousresearch.com/v1/chat/completions \
  -H "Authorization: Bearer sk-xxx" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "nous-hermes-3-llama3-70b",
    "messages": [{"role": "user", "content": "Hello Hermes-3!"}]
  }'
```


🛡️ Disclaimer

This project is unofficial and not affiliated with Nous Research.
All credits to the amazing Nous team for providing API access to Hermes-3.











