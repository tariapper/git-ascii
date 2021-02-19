import subprocess
import os


if __name__ == '__main__':
    # subprocess.run("")
    DATE = '12/16/20'
    os.system('touch test')
    os.system('git add test')
    os.system(f'git commit -m test --date {DATE}')
    os.system('git push')
