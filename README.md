# Blockcard



  - [ Introduction](#introduction)
  - [ Installation](#installation)
  - [ Usage](#usage)
    - [ Generating the first block in a chain](#generating-the-first-block-in-a-chain)
    - [ Generating subsequent blocks in the chain:](#generating-subsequent-blocks-in-the-chain)
    - [ Displaying headers and metadata of a block:](#displaying-headers-and-metadata-of-a-block)
    - [ Checking validity of blocks](#checking-validity-of-blocks)
      - [ Check current block](#check-current-block)
      - [ Check all blocks in chain recursively](#check-all-blocks-in-chain-recursively)
  - [ Examples](#examples)
    - [ Starting a new chain](#starting-a-new-chain)
    - [ Displaying an existing .bkc file](#displaying-an-existing-bkc-file)
    - [ Appending to an existing chain and checking blocks recursively](#appending-to-an-existing-chain-and-checking-blocks-recursively)

## Introduction
A pure Python implementation of the blockcard protocol's proof-of-thought system for gift transactions. Read the full paper [here](https://drive.google.com/file/d/1R2kP6jt5FqH2T9jSR1icVfcJkdFsLUht/view?usp=sharing).

## Installation

Install the latest version from PyPI with `pip install blockcard`.

## Usage

### Generating the first block in a chain

`python -m blockcard -g`

### Generating subsequent blocks in the chain:

`python -m blockcard -g parent.blk`

### Displaying headers and metadata of a block:

`python -m blockcard -d target.blk`

(For longer messages you may want to pipe this into a pager like `less`)

### Checking validity of blocks

#### Check current block

`python -m blockcard -c target.blk`

#### Check all blocks in chain recursively

`python -m blockcard -C target.blk`

(All .blk files should be stored in current working directory)

## Examples

### Starting a new chain

![](examples/svg/0.svg)

### Displaying an existing .bkc file

![](examples/svg/1.svg)

### Appending to an existing chain and checking blocks recursively

![](examples/svg/2.svg)