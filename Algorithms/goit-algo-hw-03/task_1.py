import os
import shutil
import argparse

def copy_files(source_dir, dest_dir):
    try:
        for root, _, files in os.walk(source_dir):
            for file in files:
                source_path = os.path.join(root, file)
                extension = os.path.splitext(file)[1]
                dest_subdir = os.path.join(dest_dir, extension[1:])
                
                # Create subdirectory if it doesn't exist
                os.makedirs(dest_subdir, exist_ok=True)
                
                # Copy the file to the appropriate subdirectory
                shutil.copy(source_path, os.path.join(dest_subdir, file))
        print(f"Files copied from {source_dir} to {dest_dir}")
    except PermissionError as pe:
        print(f"Permission error: {pe}")
    except OSError as oe:
        print(f"OS error: {oe}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
def main():
    parser = argparse.ArgumentParser(description="Recursive file copy and sorting")
    parser.add_argument("source_dir", help="Source directory path")
    parser.add_argument("dest_dir", nargs="?", default="dist", help="Destination directory path (default: dist)")
    args = parser.parse_args()

    source_dir = args.source_dir
    dest_dir = args.dest_dir

    copy_files(source_dir, dest_dir)

if __name__ == "__main__":
    main()
