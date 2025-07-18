require("@nomicfoundation/hardhat-toolbox");

module.exports = {
  solidity: "0.8.24",
  networks: {
    hardhat: {},
    localhost: {},
    sepolia: {
      url: "https://sepolia.infura.io/v3/YOUR_INFURA_ID",
      accounts: ["YOUR_PRIVATE_KEY"]
    }
  }
};
