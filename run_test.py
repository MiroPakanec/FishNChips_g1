import mappy 
import editdistance
import h5py
import sys

print('loaded libs.')

if __name__ == "__main__":
    config_file = sys.argv[1]
    if len(sys.argv) > 1:
        run_name = sys.argv[2]
    else:
        run_name = datetime.datetime.now().strftime('%m%d%Y-%H%M%S')
    print(f'config:{config_file}')
    print(f'run name: {run_name}')
print('done.')
