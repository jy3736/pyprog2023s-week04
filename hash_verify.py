import os
import hashlib
import sys

class HashGenerator:
    def __init__(self, directory_path):
        self.directory_path = directory_path

    def generate_hash(self, filename):
        sha256_hash = hashlib.sha256()
        with open(filename, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()

    def generate_hashes(self):
        with open("hashes.txt", "w") as f:
            for filename in os.listdir(self.directory_path):
                if os.path.isfile(os.path.join(self.directory_path, filename)):
                    file_path = os.path.join(self.directory_path, filename)
                    file_hash = self.generate_hash(file_path)
                    print("{} - {}".format(filename, file_hash))
                    f.write("{} - {}\n".format(filename, file_hash))

    def verify_hashes(self):
        with open("hashes.txt", "r") as f:
            for line in f:
                filename, expected_hash = line.strip().split(" - ")
                file_path = os.path.join(self.directory_path, filename)
                if not os.path.isfile(file_path):
                    print("Error: {} does not exist".format(file_path))
                    return 1
                else:
                    file_hash = self.generate_hash(file_path)
                    if file_hash != expected_hash:
                        print("Error: {} has been modified".format(file_path))
                        return 1
        print("Verification successful")
        return 0

if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage: python hash_generator.py <directory_path> [--verify]")
        sys.exit(1)

    directory_path = sys.argv[1]
    if not os.path.isdir(directory_path):
        print("Error: {} is not a directory".format(directory_path))
        sys.exit(1)

    hash_generator = HashGenerator(directory_path)

    if len(sys.argv) == 3 and sys.argv[2] == "--verify":
        sys.exit(hash_generator.verify_hashes())
    else:
        hash_generator.generate_hashes()
