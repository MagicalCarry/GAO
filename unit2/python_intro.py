def count_char(fn):
    import os.path
    if os.path.isfile(fn):
        with open(fn, 'r') as fh:
            total = 0
            for line in fn:
                total += len(line)
            return total
        
count_char('C:/Users/Administrator/Desktop/git/ghy/SES2020spring/unit2/readme.md')

