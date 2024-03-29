# Blockcard



  - [ Introduction](#introduction)
  - [ Installation](#installation)
  - [ Usage](#usage)
    - [ Displaying headers and message of a block:](#displaying-headers-and-metadata-of-a-block)
    - [ Generating the first block in a chain](#generating-the-first-block-in-a-chain)
    - [ Generating subsequent blocks in the chain:](#generating-subsequent-blocks-in-the-chain)
    - [ Checking validity of blocks](#checking-validity-of-blocks)
      - [ Check current block](#check-current-block)
      - [ Check all blocks in chain recursively](#check-all-blocks-in-chain-recursively)

## Introduction
A pure Python implementation of the blockcard protocol's proof-of-thought system for gift transactions. Read the full paper [here](https://drive.google.com/file/d/1R2kP6jt5FqH2T9jSR1icVfcJkdFsLUht/view?usp=sharing).

## Installation

Install the latest version from PyPI with `pip install blockcard`.

## Usage

### Displaying headers and message of a block:

`python -m blockcard -d target.blk`

### Generating the first block in a chain

`python -m blockcard -g`

### Generating subsequent blocks in the chain:

`python -m blockcard -g parent.blk`

(For longer messages you may want to pipe this into a pager like `less`)

### Checking validity of blocks

#### Check current block

`python -m blockcard -c target.blk`

#### Check all blocks in chain recursively

`python -m blockcard -C target.blk`

(All .blk files should be stored in current working directory)

## Animated demos

### Mining genesis block
![](https://chriskw.xyz/images/blockcard/0.svg)

### Displaying a message
![](https://chriskw.xyz/images/blockcard/1.svg)

### Appending a block
![](https://chriskw.xyz/images/blockcard/2.svg)
