#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_stream_management.py                              :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: tny-onin <tny-onin@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/29 12:06:14 by tny-onin            #+#    #+#            #
#   Updated: 2026/06/16 11:51:17 by tny-onin           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import sys


def file_handle(file_name: str) -> None:
    f = None
    try:
        print(f"Accessing file '{file_name}'")
        f = open(file_name, "r")
        print("---\n")
        contain = f.read()
        print(contain)

        print("\n---")
        print(f"File '{file_name}' closed.\n")
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

        print("Enter new file name (or empty): ")
        sys.stdout.write(" ")
        file_saved_name = sys.stdin.readline().strip()
        if file_saved_name == '':
            print("Not saving data.")
        else:
            f = None
            print(f"Saving data to '{file_saved_name}'")
            try:
                f = open(file_saved_name, 'w')
                f.write(transformed)
                print(f"Data saved in file '{file_saved_name}'")
            except OSError as e:
                print(f"Error opening file '{file_name}': {e}")
            finally:
                if f is not None:
                    f.close()
    except OSError as e:
        sys.stderr.write(f"Error opening file '{file_name}': {e}")
    except KeyboardInterrupt:
        sys.stderr.write("keybordInterrupt\n")
    finally:
        if f is not None:
            f.close()


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
