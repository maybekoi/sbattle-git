import csv

def convert_csv_to_cfg():
    with open('functions.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        
        with open('disasm.cfg', 'w') as outfile:
            for row in reader:
                addr = row['Location']
                name = f"sub_{addr.upper()}"
                
                outfile.write(f"thumb_func 0x{addr} {name}\n")

if __name__ == "__main__":
    convert_csv_to_cfg()