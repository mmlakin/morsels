import sys

def replace_file(infile, outfile, oldsep, newsep):
    with open(infile, mode="rt", encoding="utf-8") as ifile:
        with open(outfile, mode="wt", encoding="utf-8") as ofile:
            ofile.writelines(line.replace(oldsep,newsep) for line in ifile)

def print_file(infile):
    with open(infile, mode="rt", encoding="utf-8") as ifile:
        sys.stdout.writelines(ifile)

def main(*args):
    _,infile,outfile,oldsep,newsep = args

    print("Replacing {} with {} in {}, saving to {}".format(oldsep,newsep,infile,outfile))

    replace_file(infile,outfile,oldsep,newsep)

    print("\nOriginal:")
    print_file(infile)

    print("\nFixed:")
    print_file(outfile)


if __name__ == "__main__":
    main(*sys.argv)
