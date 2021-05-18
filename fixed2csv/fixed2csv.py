import sys

def parse_fixed_width_file(filename, col_vals):
    for line in filename:
        newline = []
        for col_val in col_vals:
            x, y = col_val
            new_line = line[x:y].strip()
            new_line = new_line.replace('"','""')
            if new_line.count(',') or new_line.count('"'):
                new_line = f'"{new_line}"'
            newline.append(new_line)
        yield newline

def parse_columns(col_str):
    return [
        tuple([
            int(coord)
            for coord in val.split(':')
        ])
        for val in col_str.split(',')
    ]

def main(args):
    cols_flag = '--cols='

    for arg in args:
        if arg[:7] == cols_flag:
           cols = arg
           args.remove(arg)
    txtfile, csvfile = args
    with open(csvfile, 'wt') as csv_fd:
        parsed_cols = parse_columns(cols.lstrip('--cols='))
        with open(txtfile, 'rt') as txt_fd:
          for line in parse_fixed_width_file(txt_fd, parsed_cols):
              csv_fd.writelines(','.join(line) + '\n')

if __name__ == "__main__":
    main(sys.argv[1:])
