import os
import random
import storytracker
from pprint import pprint


if __name__ == '__main__':
    this_dir = os.path.dirname(os.path.realpath(__file__))
    gz_dir = os.path.join(this_dir, 'screenshots')
    csv_dir = os.path.join(this_dir, 'hyperlinks')
    gz_list = os.listdir(gz_dir)
    random.shuffle(gz_list)
    for gz in gz_list:
        gz_path = os.path.join(gz_dir, gz)
        csv_path = os.path.join(csv_dir, gz.replace(".gz", ".csv"))
        if not os.path.exists(csv_path):
            print "Extracting hyperlinks from %s" % gz
            obj = storytracker.open_archive_filepath(gz_path)
            obj.write_hyperlinks_csv_to_path(csv_path)
