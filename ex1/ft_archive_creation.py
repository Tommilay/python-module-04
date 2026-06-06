#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_archive_creation.py                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: tny-onin <tny-onin@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/19 14:40:34 by tny-onin            #+#    #+#            #
#   Updated: 2026/05/29 15:48:38 by tny-onin           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import sys


def file_handle(file_name: str) -> None:
    try:
        print(f"Accessing file '{file_name}'")
        f = open(file_name, "r")
        print("---\n")
        contain = f.read()
        print(contain)

        print("\n---")
        print(f"File '{file_name}' closed.\n")
        f.close()

        transformed = ""
        for letter in contain:
            if letter == '\n':
                transformed += f"#{letter}"
            else:
                transformed += letter
        transformed += '#'

        print("Transform data:")
        print("---\n")
        print(transformed)
        print("\n---")

        file_saved_name = input("Enter new file name (or empty): ")
        if file_saved_name == '':
            print("Not saving data.")
        else:
            print(f"Saving data to '{file_saved_name}'")
            f = open(file_saved_name, 'w')
            f.write(transformed)
            print(f"Data saved in file '{file_saved_name}'")
            f.close()

    except OSError as e:
        print(f"Error opening file '{file_name}': {e}")


def main() -> None:
    print("=== Cyber Archives Recovery & Preservation ===")

    av = sys.argv
    ac = len(av)
    if ac == 2:
        file_handle(av[1])
    else:
        print(f"Usage: {av[0]} <file>")


if __name__ == "__main__":
    main()
