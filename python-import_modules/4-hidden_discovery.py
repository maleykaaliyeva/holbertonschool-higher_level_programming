#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    def_names = sorted(dir(hidden_4))
    for name in def_names:
        if name[:2] != "__":
            print(name)
