from email.utils import parsedate
import os
import argparse
import yaml
import logging


if __name__=='__main__':
    args=argparse.ArgumentParser()
    args.add_argument("--config",default="default")
    args.add_argument("--data source",default=None)

    parsed_args = args.parse_args()
    print(parsed_args)  