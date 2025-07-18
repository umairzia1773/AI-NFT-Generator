const hre = require("hardhat");

async function main() {
  const NFT = await hre.ethers.getContractFactory("GameCharacterNFT");
  const nft = await NFT.deploy();
  await nft.deployed();
  console.log(`Deployed to: ${nft.address}`);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
