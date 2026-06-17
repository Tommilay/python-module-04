#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_ancient_text.py                                   :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: tny-onin <tny-onin@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/19 14:08:59 by tny-onin            #+#    #+#            #
#   Updated: 2026/06/13 15:59:39 by tny-onin           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import sys


def file_handle(file_name: str) -> None:
    f = None
    try:
        print(f"Accessing file '{file_name}'")
        f = open(file_name, "r")
        print("---")
        print()
        print(f.read())
        print()
        print("---")
    except Exception as e:
        print(f"Error opening file '{file_name}': {e}")
    finally:
        if f is not None:
            f.close()
            print(f"File '{file_name}' closed")


def main() -> None:
    print("=== Cyber Archive Recovery ===")
    av = sys.argv
    ac = len(sys.argv)
    if ac == 2:
        file_handle(av[1])
    else:
        print(f"Usage: {av[0]} <file>")


if __name__ == "__main__":
    main()
