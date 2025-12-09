"""
Batch process zone styling for multiple Tecplot layout files.

This script takes a directory path as an argument, processes all .plt files
in that directory by:
1. Loading the .plt layout file
2. Applying zone styling based on ZoneType aux data
3. Saving the result as a .lpk layout file
4. Deleting the original .plt file
"""

import sys
import os
import tecplot
from pathlib import Path
from apply_zone_styles import apply_zone_styles


def process_directory(directory_path):
    """
    Process all .plt files in a directory.
    
    For each .plt file:
    1. Load the layout
    2. Apply zone styling
    3. Save as .lpk file
    4. Delete the original .plt file
    
    Args:
        directory_path: Path to directory containing .plt files
    """
    path = Path(directory_path)
    
    if not path.is_dir():
        print(f"Error: {directory_path} is not a valid directory.")
        sys.exit(1)
    
    # Find all .plt files
    plt_files = sorted(path.glob("*.plt"))
    
    if not plt_files:
        print(f"No .plt files found in {directory_path}")
        return
    
    print(f"Found {len(plt_files)} .plt files to process.")
    print()
    
    # Connect to Tecplot 360 session
    tecplot.session.connect()
    
    # Change to the directory so relative paths work
    os.chdir(str(path))
    
    for i, plt_file in enumerate(plt_files, 1):
        print(f"[{i}/{len(plt_files)}] Processing: {plt_file.name}")
        
        try:
            # New layout (clears previous)
            tecplot.new_layout()
            
            # Load the layout
            print("  Loading layout...")
            tecplot.data.load_tecplot(str(plt_file))
            
            # Apply zone styling
            print("  Applying zone styles...")
            apply_zone_styles()
            
            # Save as .lpk file
            lpk_file = plt_file.with_suffix(".lpk")
            print(f"  Saving to: {lpk_file.name}")
            tecplot.save_layout(str(lpk_file))
            
            # Delete the original .plt file
            print(f"  Deleting: {plt_file.name}")
            plt_file.unlink()
            
            print("  ✓ Complete")
            
        except Exception as e:
            print(f"  ✗ Error: {e}")
            continue
        
        print()
    
    print(f"Batch processing complete. {len(plt_files)} files processed.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python apply_zone_styles_batch.py <directory_path>")
        print()
        print("Processes all .plt files in the specified directory:")
        print("  1. Loads each .plt layout file")
        print("  2. Applies zone styling based on ZoneType")
        print("  3. Saves result as .lpk file")
        print("  4. Deletes the original .plt file")
        sys.exit(1)
    
    directory = sys.argv[1]
    process_directory(directory)
