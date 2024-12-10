import sys
from typing import List

# Read the filename from the command-line arguments or default to "test.txt"
FILE = sys.argv[1] if len(sys.argv) > 1 else "test.txt"

# Function to read lines from the file and return them as a list of strings
def read_lines_to_list() -> List[str]:
    lines: List[str] = []
    with open(FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()  # Remove leading/trailing whitespace
            lines.append(line)  # Add the cleaned line to the list
    print(lines)  # Debug: print the read lines
    return lines

# Function to solve part one of the problem
def part_one():
    lines = read_lines_to_list()
    vals = [int(val) for val in list(lines[0])]  # Convert the first line to a list of integers
    print(f"Vals: {vals}")  # Debug: print the parsed values
    answer = 0

    # Initialize variables
    id = 0  # Identifier for block sections
    strip = []  # List representing the arrangement of blocks and gaps
    is_block = True  # Toggle between block and gap processing

    # Build the strip with block IDs and gaps
    for i in range(len(vals)):
        if is_block:
            strip.extend([id] * vals[i])  # Add block ID multiple times
            id += 1  # Increment block ID
        else:
            strip.extend([None] * vals[i])  # Add gaps (None values)

        is_block = not is_block  # Alternate between block and gap

    # Find the first free space (None value) in the strip
    free_space = strip.index(None)
    print(f"free space: {free_space}")  # Debug: print the index of the free space

    # Rearrange blocks to fill gaps
    for i in reversed(range(0, len(strip))):
        if strip[i] is not None:  # If it's a block
            strip[free_space] = strip[i]  # Move it to the free space
            strip[i] = None  # Mark the original position as free
            print(f"Strip: {strip}")  # Debug: print the strip after adding blocks
            while strip[free_space] is not None:  # Find the next free space
                free_space += 1
            if i - free_space <= 1:  # Stop if the remaining space is too small
                break

    # Calculate the answer based on the final arrangement
    answer = sum(val * itx if val is not None else 0 for (itx, val) in enumerate(strip))
    print(f"Part 1: {answer}")  # Output the result for part one

# Function to solve part two of the problem
def part_two():
    lines = read_lines_to_list()
    vals = [int(val) for val in list(lines[0])]  # Convert the first line to a list of integers
    answer = 0

    # Initialize variables
    id = 0  # Identifier for block sections
    strip = []  # List representing the arrangement of blocks and gaps
    gaps = []  # List of gap lengths and positions
    blocks = []  # List of block positions, IDs, and lengths
    is_block = True  # Toggle between block and gap processing

    # Build the strip and record block/gap details
    for i in range(len(vals)):
        if is_block:
            blocks.append((len(strip), id, vals[i]))  # Store block info
            strip.extend([id] * vals[i])  # Add block ID multiple times
            id += 1  # Increment block ID
        else:
            gaps.append((vals[i], len(strip)))  # Store gap info
            strip.extend([None] * vals[i])  # Add gaps (None values)

        is_block = not is_block  # Alternate between block and gap

    # Rearrange blocks to fill gaps
    for block in reversed(blocks):  # Process blocks in reverse order
        (position, id, length) = block
        for itx, (gap_length, gap_position) in enumerate(gaps):
            if gap_position > position:  # Only consider gaps after the block
                                    
            
                print(f"Strip: {strip}")  # Debug: print the strip after adding blocks
                break

            if gap_length >= length:  # If the gap is big enough
                for l in range(length):  # Move the block to the gap
                    strip[position + l] = None  # Clear the original position
                    strip[gap_position + l] = id  # Place the block in the gap

                # Update or remove the gap entry
                diff = gap_length - length
                if diff > 0:
                    gaps[itx] = (diff, gap_position + length)  # Update gap length and position
                else:
                    gaps.pop(itx)  # Remove the gap if fully filled
                break

    # Calculate the answer based on the final arrangement
    answer = sum(val * itx if val is not None else 0 for (itx, val) in enumerate(strip))
    print(f"Part 2: {answer}")  # Output the result for part two

# Execute part one and part two
part_one()
part_two()
