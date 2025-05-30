<img width="1230" alt="image" src="[https://github.com/sezaras85/Sentient-ai/blob/main/sentient%20resim.png](https://github.com/sezaras85/Nous-research-Hermes-3-Llama-3.1-70B/blob/main/nous%20ekran.jpeg)" />

# Nous-research-

Nous Research is a leader in the development of human-centric language models and simulators.  there primary focus areas include model architecture, data synthesis, fine-tuning, and reasoning, all aimed at aligning AI systems with real-world user experiences. its prioritize the development of open-source, human-compatible models, which challenge the conventional closed-model approach. 

This project started out of curiosity — to better understand how Hermes-3 might one day connect with the broader Nous Protocol, possibly through on-chain inference or smart contract integration.
Ideas, improvements, or just playing around? PRs welcome!
This repo is community-driven. Let's explore the future of decentralized AI together.

# 🧠 Hermes-3 Terminal Chatbot (Nous Research API)

A simple CLI-based chatbot using the powerful `Hermes-3-Llama3-70B` model from [Nous Research](https://nousresearch.com/).  
Built for testing, learning, and exploring the capabilities of Hermes-3 via its official inference API.

![Hermes Banner](https://portal.nousresearch.com/_next/image?url=%2Fimages%2Flogos%2Fhermes3.png&w=3840&q=75)

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

1. Clone the repo:

```bash
git clone https://github.com/sezaras85/hermes3-terminal-bot.git
cd hermes3-terminal-bot
```

Install dependencies:

```bash

pip install requests
```

Add your API key to the script (or use an .env file for security).

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











