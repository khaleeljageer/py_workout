def remove_duplicates_from_file(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()
        f.close()

    # Use set to remove duplicates while preserving the order of appearance
    unique_lines = list(set(lines))

    with open(output_file, 'w') as f:
        f.writelines(unique_lines)
        f.close()


def main():
    input_file = "urls.txt"
    output_file = "unique_urls.txt"

    remove_duplicates_from_file(input_file, output_file)
    print("Duplicates removed and unique URLs saved to 'unique_urls.txt'")


if __name__ == '__main__':
    main()
