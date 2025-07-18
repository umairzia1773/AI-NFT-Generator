// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract GameCharacterNFT is ERC721URIStorage, Ownable {
    uint256 public nextTokenId;
    mapping(uint256 => string) public characterNames;
    mapping(uint256 => uint256) public characterLevels;

    constructor() ERC721("GameCharacter", "GCHAR") {}

    function mintCharacter(string memory name, uint256 level, string memory tokenURI) public onlyOwner {
        uint256 tokenId = nextTokenId;
        _safeMint(msg.sender, tokenId);
        _setTokenURI(tokenId, tokenURI);
        characterNames[tokenId] = name;
        characterLevels[tokenId] = level;
        nextTokenId++;
    }

    function getCharacter(uint256 tokenId) public view returns (string memory name, uint256 level) {
        return (characterNames[tokenId], characterLevels[tokenId]);
    }
}
