# 🧠 AI-Generated NFT Game Characters with Ownership History

Welcome to the **AI NFT Game** — a futuristic project combining **AI-generated art**, **NFT minting**, and **blockchain ownership history** into one seamless platform.

> Imagine a world where each game character is born from AI, uniquely styled, ranked by levels, and immortalized on the blockchain as your own collectible NFT.

---

## 🚀 Live Features

🎨 Auto-generated character images (name, level, art)  
🧠 AI-inspired metadata for game-based NFTs  
📦 IPFS-backed decentralized storage  
💎 ERC-721 NFT smart contracts (on Ethereum testnet)  
🖼️ Web interface to view, connect wallet, and mint NFTs  
📜 Ownership history tracked on-chain

---

## 📸 Preview

<img src="images/Aether_NFT.png" width="300" alt="NFT Preview" />

---

## 🧱 Tech Stack

| Layer       | Tech                               |
|-------------|------------------------------------|
| Smart Contract Solidity, OpenZeppelin ERC-721    |
| Web3 SDK    | Ethers.js, MetaMask, Hardhat       |
| AI/Backend  | Python, Flask, PIL, Web3.Storage   |
| Storage     | IPFS (via Web3.Storage API)        |
| Frontend    | HTML, CSS, Vanilla JS              |

---

## 📂 Project Structure

```
ai-nft-game/
│
├── contracts/           # Smart contract (Solidity)
├── scripts/             # Deployment scripts
├── frontend/            # Web UI (HTML, JS, CSS)
├── backend/             # Flask API & AI image generator
├── images/              # Generated NFT images
├── .env                 # Web3.Storage token (DO NOT COMMIT)
├── README.md
```

---

## 🛠️ How It Works

1. 🎲 **Generate Characters**  
   Run a Python script to generate AI-styled characters with names and levels.

2. ☁️ **Upload to IPFS**  
   Flask backend uploads image + metadata to IPFS using Web3.Storage.

3. 🧠 **Mint the NFT**  
   Use the web UI to mint your character as an ERC-721 NFT on Sepolia.

4. 🧾 **Track Ownership**  
   View your characters in the UI and track them on-chain.

---

## 🧪 Quick Start

### 1. Install & Compile Contracts

```bash
npm install
npx hardhat compile
```

### 2. Deploy to Sepolia

```bash
npx hardhat run scripts/deploy.js --network sepolia
```

### 3. Run Backend API

```bash
cd backend
pip install flask requests python-dotenv
python app.py
```

### 4. Generate Sample Characters

```bash
python generate_characters.py
```

### 5. Run Frontend

```bash
npm start
```

---

## 🔐 Security Note

- Store your `.env` like this (and **never commit it**):

```env
WEB3_STORAGE_TOKEN=your_web3_storage_api_key
PRIVATE_KEY=your_wallet_private_key
```

- Add `.env` to your `.gitignore`

---

## 🌐 Demo Token URI Example

```json
{
  "name": "Aether",
  "description": "Level 5 character",
  "image": "https://bafybeib2bt75doon3rtxoww2j5a6enljwdhpm45hz35lsg2tz44acsbvqa.ipfs.w3s.link/Aether_NFT.png",
  "attributes": [
    { "trait_type": "Level", "value": 5 }
  ]
}
```

🔗 Token URI:  
`https://bafybeib2bt75doon3rtxoww2j5a6enljwdhpm45hz35lsg2tz44acsbvqa.ipfs.w3s.link/Aether.json`

---

## 🧠 Ideas to Expand

- Add AI-generated **abilities**, **skills**, or **rarity**
- Integrate **Stable Diffusion** or **DALLE** for real image gen
- Create a **marketplace** for users to buy/sell AI-NFTs
- Build a **game** around these NFTs (RPG or card-style)

---

## 👨‍💻 Author

**Umair Zia**  

[LinkedIn](https://www.linkedin.com/in/umair-zia-061ba5261?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)

---

## 📜 License

MIT — feel free to fork, build, or contribute!
