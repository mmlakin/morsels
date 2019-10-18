#!/usr/bin/env/python3

import csv, argparse

def replace_file(infile, outfile, delim, quote):
    with open(infile, mode="rt", encoding="utf-8") as ifile:
        with open(outfile, mode="wt", encoding="utf-8") as ofile:
            if delim == None or quote == None:
                sniffed = csv.Sniffer().sniff(ifile.read())
                if delim == None: delim = sniffed.delimiter
                if quote == None: quote = sniffed.quotechar
                ifile.seek(0)

            csv.register_dialect('dynamic',
                                 delimiter=delim,
                                 quotechar=quote)
            csvwriter = csv.writer(ofile)
            for row in csv.reader(ifile, dialect='dynamic'):
                csvwriter.writerow(row)

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('infile')
    parser.add_argument('outfile')
    parser.add_argument('--in-delimiter', dest='delim', type=str)
    parser.add_argument('--in-quote', dest='quote', type=str)
    
    return parser.parse_args()

def main():
    args = parse_arguments()
    replace_file(args.infile, args.outfile, args.delim, args.quote)

if __name__ == "__main__":
    main()
