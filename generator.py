import hashlib


def to_hash(file):
    with open(file, encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            hash_line = hashlib.md5(line.encode())
            yield hash_line.hexdigest()


def type_hash(file):
    for hashed_data in to_hash(file):
        print(hashed_data)


type_hash('countries_with_links.txt')
