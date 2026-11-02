
# Virtual to Physical Address Translation

PAGE_SIZE = 1024

# Page table
page_table = {
    0: 5,
    1: 2,
    2: None,  # Page not present
    3: 7
}

# Given virtual addresses
virtual_addresses = [500, 1500, 2500, 3500]

print("Virtual Address Translation")
print("-" * 85)

print(f"{'Virtual Address':<18}{'Page No.':<12}"
      f"{'Offset':<12}{'Frame No.':<12}"
      f"{'Physical Address / Status'}")

print("-" * 85)

for va in virtual_addresses:

    # Calculate page number and offset
    page_number = va // PAGE_SIZE
    offset = va % PAGE_SIZE

    # Check page table
    frame_number = page_table.get(page_number)

    if frame_number is not None:
        # Calculate physical address
        physical_address = (
            frame_number * PAGE_SIZE + offset
        )

        print(f"{va:<18}{page_number:<12}"
              f"{offset:<12}{frame_number:<12}"
              f"{physical_address}")
    else:
        print(f"{va:<18}{page_number:<12}"
              f"{offset:<12}{'-':<12}"
              f"Page fault")

print("-" * 85)
