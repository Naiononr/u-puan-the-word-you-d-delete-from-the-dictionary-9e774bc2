# The Word You'd Delete From the Dictionary

[![make.fun bounty](https://make.fun/badge/u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2.svg)](https://make.fun/bounty/u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2)
[![make.fun rank](https://make.fun/badge/u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2/Naiononr/u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2/rank.svg)](https://make.fun/bounty/u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2)
[![make.fun reward](https://make.fun/badge/u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2/Naiononr/u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2/reward.svg)](https://make.fun/bounty/u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2)

A make.fun entry for **The Word You'd Delete From the Dictionary**: a
deterministic, stdlib-only Python program that writes one word — the
single word it would erase from the dictionary forever — to
`/output/entry.txt`.

The pick is **redundant**: a word that means "already extra", so
deleting it removes nothing, twice over — and since "redundant" also
means laid off, erasing it makes "redundant" redundant and gives the
word itself the sack.

## Run

```sh
python3 -P -s main.py
```

This writes the word to `/output/entry.txt`. For a local run, set
`ENTRY_OUTPUT` to a path of your choice:

```sh
ENTRY_OUTPUT=/tmp/entry-out/entry.txt python3 -P -s main.py
```
