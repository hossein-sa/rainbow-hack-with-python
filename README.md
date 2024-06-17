# Password Hashing and Hacking

This repository contains Python scripts to demonstrate the generation of SHA-256 hashed passwords and their subsequent hacking using precomputed hashes of 4-digit numbers.

## Contents

1. [Files](#files)
2. [Dependencies](#dependencies)
3. [Usage](#usage)
4. [License](#license)

---

## Files

- **generate_passwords.py**: Generates a `passwords.csv` file containing names and SHA-256 hashes of randomly generated 4-digit numbers.
  
- **hack_passwords.py**: Reads the `passwords.csv` file, matches the hashes with precomputed hashes of 4-digit numbers, and saves matched name/password pairs to `hacked_passwords.csv`.

## Dependencies

- Python 3.x
- `hashlib` (Standard library for cryptographic hashing)
- `csv` (Standard library for CSV file operations)
- `random` (Standard library for random number generation)

## Usage

1. **Generating Passwords**

   Run `generate_passwords.py` to create `passwords.csv` with randomly generated 4-digit passwords for each name.

2. **Hacking Passwords**

   Run `hack_passwords.py` to read `passwords.csv`, match the hashes, and save matched name/password pairs to `hacked_passwords.csv`.

---

## License

This project is licensed under the MIT License - see the LICENSE file for details.
