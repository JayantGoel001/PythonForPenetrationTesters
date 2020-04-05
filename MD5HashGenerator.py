import hashlib
import argparse

parser = argparse.ArgumentParser(description="MD5 Cracker")
parser.add_argument("-md5", dest="hash", help="md5 hash", required=True)
parser.add_argument("-w", dest="wordlist", help="wordlist", required=True)
parsed_args = parser.parse_args()


def main():
    hash_cracked = ""
    with open(parsed_args.wordlist) as file:
        for line in file:
            line = line.strip()
            if hashlib.md5(bytes(line, encoding="utf-8")).hexdigest() == parsed_args.hash:
                hash_cracked = line
                print("\nMD5-hash has been successfully cracked. The value is " + hash_cracked)
    if hash_cracked == "":
        print("\nFailed to crack the hash. Try using a bigger dictionary")


if __name__ == "__main__":
    main()


# py -3 MD5HashGenerator.py -md5 5ebe2294ecd0e0f08eab7690d2a6ee69 -w dic.txt
