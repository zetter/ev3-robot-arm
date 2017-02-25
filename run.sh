# Upload and run the file after validating syntax.
# Takes the filename as first argument, such as:
#   ./run.sh move.py

python -m py_compile $1
scp $1 robot@ev3dev.local:/home/robot
ssh robot@ev3dev.local "python3 /home/robot/$1"