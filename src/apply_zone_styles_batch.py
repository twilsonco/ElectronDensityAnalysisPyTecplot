"""
Process zone styling for Tecplot layout files in batch mode.

Supports two workflows:

1. SINGLE FILE (batch mode):
   - Usage: python apply_zone_styles_batch.py /path/to/file.plt
   - Processes a single .plt file in batch mode
   - Output: creates file.lpk in same directory

2. DIRECTORY (batch mode):
   - Usage: python apply_zone_styles_batch.py /path/to/directory
   - Processes all .plt files in directory, each in batch mode
   - For each .plt file:
     1. Loads the layout file
     2. Applies zone styling based on ZoneType aux data
     3. Saves the result as a .lpk layout file
     4. Deletes the original .plt file

No running Tecplot instance required (pure batch mode processing).
"""

import sys
import tecplot
from pathlib import Path
from apply_zone_styles import apply_zone_styles


def process_single_file_batch(plt_path):
    """
    Process a single .plt file using batch mode (no GUI connection needed).
    
    Workflow:
    1. Load the .plt file
    2. Apply zone styling based on ZoneType aux data
    3. Save the result as a .lpk file
    4. Delete the original .plt file
    
    Args:
        plt_path: Path to the .plt file to process
    """
    plt_file = Path(plt_path)
    
    if not plt_file.exists():
        print(f"Error: {plt_path} does not exist.")
        sys.exit(1)
    
    if not plt_file.suffix.lower() == ".plt":
        print(f"Error: {plt_path} is not a .plt file.")
        sys.exit(1)
    
    print(f"Processing (Batch Mode): {plt_file.name}")
    print(f"  Input:  {plt_file}")
    
    try:
        # Create new layout
        print("  Loading layout...")
        tecplot.new_layout()
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
        
        print(f"  Output: {lpk_file}")
        print("  ✓ Complete")
        
    except Exception as e:
        print(f"  ✗ Error: {e}")
        sys.exit(1)


def process_directory_batch(directory_path):
    """
    Process all .plt files in a directory using batch mode.
    
    No running Tecplot instance needed. Each file is processed independently
    in batch mode, then the original .plt file is deleted.
    
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
    
    print(f"Found {len(plt_files)} .plt files to process in batch mode.")
    print()
    
    for i, plt_file in enumerate(plt_files, 1):
        print(f"[{i}/{len(plt_files)}] Processing: {plt_file.name}")
        
        try:
            # Create new layout
            print("  Loading layout...")
            tecplot.new_layout()
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
        print("Usage:")
        print()
        print("  SINGLE FILE (batch mode, no Tecplot instance needed):")
        print("    python apply_zone_styles_batch.py <path_to_file.plt>")
        print()
        print("  DIRECTORY (batch mode, no Tecplot instance needed):")
        print("    python apply_zone_styles_batch.py <directory_path>")
        print()
        print("SINGLE FILE MODE:")
        print("  - Processes a single .plt file using PyTecplot batch mode")
        print("  - No running Tecplot 360 instance required")
        print("  - Output: <file>.lpk in same directory")
        print()
        print("DIRECTORY MODE:")
        print("  - Processes all .plt files in a directory using batch mode")
        print("  - No running Tecplot 360 instance required")
        print("  - For each .plt file:")
        print("    1. Loads the layout file")
        print("    2. Applies zone styling based on ZoneType")
        print("    3. Saves result as .lpk file")
        print("    4. Deletes the original .plt file")
        sys.exit(1)
    
    arg = sys.argv[1]
    path = Path(arg)
    
    # Determine mode based on argument
    if arg.lower().endswith('.plt') or (path.exists() and path.is_file() and path.suffix.lower() == '.plt'):
        # SINGLE FILE MODE: single file in batch mode
        process_single_file_batch(arg)
    elif path.is_dir() or not path.exists():
        # DIRECTORY MODE: all .plt files in directory, in batch mode
        # This allows typos to fail gracefully in process_directory_batch
        process_directory_batch(arg)
    else:
        print(f"Error: {arg} is neither a .plt file nor a directory")
        sys.exit(1)
