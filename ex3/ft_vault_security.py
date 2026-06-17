#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_vault_security.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: tny-onin <tny-onin@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/10 11:18:35 by tny-onin            #+#    #+#            #
#   Updated: 2026/06/16 13:54:54 by tny-onin           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def secure_archive(filename: str, action: str) -> tuple[bool, str]:
    content = "Content successfully written to file"
    try:
        with open(filename, action) as f:
            if action == "r":
                content = f.read()
                result = (True, content)
            if action == "w":
                f.write(content)
                result = (True, content)
        print(f.closed)
        return result
        # return (False, "Error")
    except Exception as e:
        return (False, f'{e}')


def main() -> None:
    print("=== Cyber Archives Security ===\n")
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(f"{secure_archive('/not/existing/file', 'r')}\n")

    print("Using 'secure_archive' to read from an inaccessible file:")
    print(f"{secure_archive('password', 'r')}\n")

    print("Using 'secure_archive' to read from a regular file:")
    print(f"{secure_archive('ancient_file.txt', 'r')}\n")

    print("Using 'secure_archive' \
to write from previous content to a new file:")
    print(f"{secure_archive('./ex3/new_file.txt', 'w')}\n")


if __name__ == "__main__":
    main()
