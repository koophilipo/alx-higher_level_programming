#!/usr/bin/python3
import hidden_4


def main():
    names = dir(hidden_4)
    for x, name in enumerate(names):
        if name[0] == '_' and name[1] == '_':
            continue
        print("{}".format(name))


if __name__ == '__main__':
    main()
exit(0)
