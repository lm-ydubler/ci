import json
import yaml
import sys
from glob import glob
from collections import OrderedDict

EXCHANGE_NAME = "StackStorm-Exchange"
EXCHANGE_PREFIX = "stackstorm"


def build_index(path):
    packs = OrderedDict()

    generator = sorted(glob('%s/packs/*.yaml' % path))
    for filename in generator:
        with open(filename, 'r') as pack:
            pack_meta = yaml.load(pack)

        pack_meta['repo_url'] = 'https://github.com/%s/%s-%s' % (
            EXCHANGE_NAME, EXCHANGE_PREFIX, pack_meta['name']
        )
        packs[pack_meta['name']] = pack_meta

    with open('%s/index.json' % path, 'w') as outfile:
        json.dump(packs, outfile, indent=4, sort_keys=True)

if __name__ == '__main__':
    path = sys.argv[1]
    build_index(path)
