import csv
import hashlib


def hash_password_hack(input_file_name, output_file_name):
    hashed_numbers = {}
    matched_hashes = {}

    # Generate hash dictionary for numbers 0000-9999
    for i in range(10000):
        number_str = str(i).zfill(4)
        number_bytes = number_str.encode()
        sha256_hash = hashlib.sha256(number_bytes).hexdigest()
        hashed_numbers[sha256_hash] = number_str

    # Read the input file and check for matches
    with open(input_file_name, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[1] in hashed_numbers:
                matched_hashes[row[1]] = hashed_numbers[row[1]]

    # Write matched hashes and passwords to the output file
    with open(output_file_name, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Hash', 'Password'])  # Header row
        for hash_value, password in matched_hashes.items():
            writer.writerow([hash_value, password])

    # Print the matched hash/password pairs
    for hash_value, password in matched_hashes.items():
        print(f"{hash_value}: {password}")


if __name__ == '__main__':
    hash_password_hack('passwords.csv', 'hacked_passwords.csv')
