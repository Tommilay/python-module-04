# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_vault_security.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tny-onin <tny-onin@student.42antananari    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/06/10 11:18:35 by tny-onin          #+#    #+#              #
#    Updated: 2026/06/10 11:18:35 by tny-onin         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def secure_archive(filename: str, action: str) -> tuple[bool, str]:
    content = "'Content successfully written to file"
    try:
        with open(filename, action) as f:
            if action == "r":
                content = f.read()
                return (True, content)
            if action == "w":
                f.write(content)
                return (True, content)
    except Exception as e:
        return(False, e)

def main():
    print("=== Cyber Archives Security ===\n")
    print("Using 'secure_archive' to read from an inaccessible file:")
    print(f"{secure_archive("abc.txt", "r")}\n")
    print("Using 'secure_archive' to read from a regular file:")
    print(f"{secure_archive("./ex3/file.txt", "r")}\n")
    print("Using 'secure_archive' to write from previous content to a new file:")
    print(f"{secure_archive("./ex3/new_file.txt", "w")}\n")
    print(f"{secure_archive("./ex3/new_file.txt", "z")}\n")


if __name__ == "__main__":
    main()
