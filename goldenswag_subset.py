#!/usr/bin/env python3

import sys

from argparse import ArgumentParser

from datasets import load_dataset


def argparser():
    ap = ArgumentParser()
    ap.add_argument('source')
    ap.add_argument('subset')
    ap.add_argument('goldenswag')
    ap.add_argument('repo_id')
    return ap


def main(argv):
    args = argparser().parse_args(argv[1:])

    source = load_dataset(args.source, args.subset, split='validation')
    goldenswag = load_dataset(args.goldenswag, split='validation')

    get_id = lambda e: (e['ind'], e['source_id'])
    ids = { get_id(e) for e in goldenswag }

    subset = source.filter(lambda e: get_id(e) in ids)

    subset.push_to_hub(args.repo_id)


if __name__ == '__main__':
    sys.exit(main(sys.argv))
