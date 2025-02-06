# made by https://github.com/maybekoi
def find_rom_boundaries(asm_file):
    rom_start = 0x08000000 
    end_of_code = None
    end_of_data = None
    
    highest_code = 0
    highest_data = 0
    
    with open(asm_file, 'r') as f:
        for line in f:
            if '@' in line and ':' in line:
                try:
                    addr = int(line.split('@')[1].strip()[:8], 16)
                    highest_code = max(highest_code, addr)
                except:
                    continue
                    
            if '.4byte' in line and '0x08' in line:
                try:
                    addr = int(line.split('0x08')[1].split()[0], 16) + 0x08000000
                    highest_data = max(highest_data, addr)
                except:
                    continue
    
    end_of_code = highest_code
    end_of_data = highest_data
    
    print(f"ROM boundaries found:")
    print(f"rom_start = 0x{rom_start:08X}")
    print(f"end_of_code = 0x{end_of_code:08X}")
    print(f"end_of_data = 0x{end_of_data:08X}")
    
    return rom_start, end_of_code, end_of_data

if __name__ == "__main__":
    find_rom_boundaries("../asm/code.s")