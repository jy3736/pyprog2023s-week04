import os
import hashlib
import sys

def generate_hash(filename):
    sha256_hash = hashlib.sha256()
    with open(filename, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage: python hash_generator.py <directory_path> [--verify]")
        sys.exit(1)

    directory_path = sys.argv[1]
    if not os.path.isdir(directory_path):
        print("Error: {} is not a directory".format(directory_path))
        sys.exit(1)

    if len(sys.argv) == 3 and sys.argv[2] == "--verify":
        with open("hashes.txt", "r") as f:
            for line in f:
                filename, expected_hash = line.strip().split(" - ")
                file_path = os.path.join(directory_path, filename)
                if os.path.isfile(file_path):
                    file_hash = generate_hash(file_path)
                    if file_hash == expected_hash:
                        print("{}: OK".format(filename))
                    else:
                        print("{}: ERROR (expected {}, got {})".format(filename, expected_hash, file_hash))
                else:
                    print("{}: NOT FOUND".format(filename))
    else:
        with open("hashes.txt", "w") as f:
            for filename in os.listdir(directory_path):
                if os.path.isfile(os.path.join(directory_path, filename)):
                    file_path = os.path.join(directory_path, filename)
                    file_hash = generate_hash(file_path)
                    print("{} - {}".format(filename, file_hash))
                    f.write("{} - {}\n".format(filename, file_hash))
