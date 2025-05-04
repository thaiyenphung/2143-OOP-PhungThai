import sys
import os
from myKwargs import MyKwargs  # custom function to parse command-line arguments

if __name__ == "__main__":
    # Get the full path to this file 
    current_file_path = os.path.abspath(__file__)

    # Get the directory where this file is located
    current_dir = os.path.dirname(current_file_path)

    # Print the directory path (for debugging)
    print(current_dir)
    
    # Replace argv[0] with the full path of this file
    sys.argv[0] = current_file_path

    # Use our custom parser to split arguments into args and key:value pairs
    args, kargs = MyKwargs(sys.argv[1:])

    # Show the parsed arguments
    print(args)
    print(kargs)