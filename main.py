import hashlib

data_path = "data.txt"

with open(data_path, "r") as f:
    data_list = [x.strip() for x in f.read().split("\n")]


def bit_hash(data):
    data = str(data)
    data = data.encode("utf-8")
    return hashlib.sha256(data).hexdigest()


def create_block(prior_block_hash, prior_block_number, data):
    # (prior_block_hash, block_number, data, hash)
    block_number = prior_block_number + 1
    block_hash = bit_hash((prior_block_hash, block_number, data))
    return (prior_block_hash, block_number, data, block_hash)


def append_block(chain, data):
    # [ prior block hash, block number, data, block hash ]
    if len(chain) == 0:
        block = create_block(0, -1, data)
    else:
        block = create_block(chain[-1][3], chain[-1][1], data)

    chain.append(block)
    return chain


def main(data_list):
    chain = []
    for data in data_list:
        chain = append_block(chain, data)
    return chain


if __name__ == "__main__":
    [print(block) for block in main(data_list)]
