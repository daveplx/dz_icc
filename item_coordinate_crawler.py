from sys import argv
from os import path, walk
from prettytable import PrettyTable
import glob


OUT_FILE_NAME = 'item_coordinate_result.txt' # this will be out output file - overridden on each run!
ALLOWED_COORD_DEVIATION = 5 # how much +/- deviation in the coordinate is allowed when searching
LOG_FILE_NAME = 'MAGItemLogger.log' # in case the log file name ever changes
DEFAULT_LOG_DIR_PATH = 'i:\\\\.shortcut-targets-by-id\\*\\logs_cherno'
FOLDERS_TO_SKIP = ['_current']
SKIP_FOLDERS = True


try:
    if len(argv) == 1:
        log_path_list = glob.glob(f'{DEFAULT_LOG_DIR_PATH}\\*\\{LOG_FILE_NAME}')
        crawl_item = input('Name of the item to search for >')
        crawl_x_coord = int(input('X coordinate you want to search for >'))
    elif len(argv) == 2:
        path_to_top_dir = argv[1]
        log_path_list = glob.glob(f'{path_to_top_dir}\\*\\{LOG_FILE_NAME}')
        crawl_item = input('Name of the item to search for >')
        crawl_x_coord = int(input('X coordinate you want to search for >'))
    elif len(argv) == 3:
        log_path_list = glob.glob(f'{DEFAULT_LOG_DIR_PATH}\\*\\{LOG_FILE_NAME}')
        crawl_item = str(argv[1])
        crawl_x_coord = int(argv[2])
    elif len(argv) == 4:
        path_to_top_dir = argv[1]
        log_path_list = glob.glob(f'{path_to_top_dir}\\*\\{LOG_FILE_NAME}')
        crawl_item = str(argv[2])
        crawl_x_coord = int(argv[3])
    else:
        raise SyntaxError('SyntaxError')
        exit(1)
except Exception as e:
    usage = PrettyTable()
    usage.field_names = ['Command', 'Result']
    usage.add_row([f'python {path.basename(__file__)}', 'Default log dir, asks for item / coordinate'])
    usage.add_row([f'python {path.basename(__file__)} <item_name> <x_coord>', 'Default log dir, parses item / coordinate'])
    usage.add_row([f'python {path.basename(__file__)} <path_to_log_folder>', 'Explicit log dir, asks for item / coordinate'])
    usage.add_row([f'python {path.basename(__file__)} <path_to_log_folder> <item_name> <x_coord>', 'Explicit log dir, parses item / coordinate'])
    usage.align['Command'] = 'l'
    usage.align['Result'] = 'l'
    print(str(usage))
    print(f'Error trying to parse arguments:\n{e}')
    exit(1)

output_buffer = []

for log in log_path_list:

    if SKIP_FOLDERS:
        if log.split('\\')[-2] in FOLDERS_TO_SKIP: continue

    lines = []
    
    try:
        with open(log, 'r') as f:
            for line in f.readlines():
                lines.append(str(line).strip())
    except Exception as e:
        print(f'Error trying to read log file {log}:\n{e}')
        exit(1)
    
    for line in lines:
        line_list = line.split()
        if not line_list[3] == 'moved': continue # only search lines where an item was moved
        item = line_list[4]
        if not item.lower() == crawl_item.lower(): continue # only search lines where items match
        x_coord = str(line_list[-3])[1:].split('.')[0]
        if not crawl_x_coord - ALLOWED_COORD_DEVIATION < int(x_coord) < crawl_x_coord + ALLOWED_COORD_DEVIATION: continue # only take lines where coordinates match according to allowed deviation
        user = ''.join(line_list[1:3])
        action = line_list[6]
        total_coords = ', '.join([c.split('.')[0].strip('<') for c in line_list[-3:]])
        dt = line_list[0]
        output_buffer.append([user, item, total_coords, action, dt, log])

pt = PrettyTable()
pt.field_names = ['User', 'Item', 'Coordinates', 'Action', 'Datetime', 'Log']

pt.add_rows(output_buffer)

with open(OUT_FILE_NAME, 'w') as f:
    f.write(str(pt))