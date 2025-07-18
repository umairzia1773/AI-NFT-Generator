async function connectWallet() {
  if (window.ethereum) {
    try {
      const accounts = await ethereum.request({ method: "eth_requestAccounts" });
      console.log("Connected:", accounts[0]);
      return accounts[0];
    } catch (err) {
      alert("Wallet connection failed");                 
    }
  } else {
    alert("MetaMask not installed!");
  }
}

async function mintNFT(name, level, imagePath, tokenURI) {
  const provider = new ethers.providers.Web3Provider(window.ethereum);
  const signer = provider.getSigner();

  const contractAddress = "YOUR_CONTRACT_ADDRESS";   
  const abi = [
    "function mintCharacter(string memory name, uint256 level, string memory tokenURI) public"
  ];

  const contract = new ethers.Contract(contractAddress, abi, signer);
  const tx = await contract.mintCharacter(name, level, tokenURI);
  await tx.wait();
  alert("NFT Minted!");
}

document.addEventListener("DOMContentLoaded", () => {
  const gallery = document.getElementById("nft-gallery");
  const characters = [
    { name: "Aether", image: "../images/Aether_NFT.png", level: 5 }
  ];
  characters.forEach(c => {
    const img = document.createElement("img");
    img.src = c.image;
    img.alt = `${c.name} - Level ${c.level}`;
    gallery.appendChild(img);
  });
});
