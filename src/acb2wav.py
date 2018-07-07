#!/usr/bin/env python3

import argparse
import glob
import os
import pathlib
import sys
import time

import acbpy
import hcapy


def remove_words(str, *words):
    for word in words:
        str = str.replace(word, "")
    return str


parser = argparse.ArgumentParser()

parser.add_argument("-k", "--key", metavar="", default="00003657f27e3b22", help="Default: 00003657f27e3b22")
parser.add_argument("-e", "--extension", metavar="", default="acb.bytes", help="Default: acb.bytes")
parser.add_argument("-i", "--inputDir", metavar="", default="acb", help="Default: acb")
parser.add_argument("-o", "--outputDir", metavar="", default="wav", help="Default: wav")
parser.add_argument("-ns", "--noSubDir", action="store_true", help="Default: False")

args = parser.parse_args()

start = time.time()

if args.key.isnumeric():
    d = hcapy.Decoder(int(args.key))
else:
    d = hcapy.Decoder(args.key)
    
if args.extension != "*":
    args.extension = f"*.{args.extension}"

args.inputDir = remove_words(args.inputDir, "\**", "/**") + "/**"

path = os.path.join(args.inputDir, args.extension)

for i in filter(os.path.isfile, glob.iglob(path, recursive=True)):
    with open(i, "rb") as f:
        file_name = os.path.basename(f.name).split(".")[0]

        if args.noSubDir:
            dir_name = args.outputDir
        else:
            dir_name = os.path.join(args.outputDir, file_name)

        pathlib.Path(dir_name).mkdir(parents=True, exist_ok=True)

        try:
            for i in acbpy.parse_binary(f):
                track_name = i.track.name

                try:
                    with open(os.path.join(dir_name, f"{track_name}.wav"), "wb") as f:
                        f.write(d.decode(i.binary.read()).read())

                        print(f"{track_name}.wav")
                except hcapy.InvalidHCAError:
                    print(f"{track_name} is invalid hca!")
        except:
            print(f"{file_name} is invalid acb!")

            if not args.noSubDir:
                if not os.listdir(dir_name):
                    os.rmdir(dir_name)

    print()

end = time.time()

print(f"Time: {end - start:.3f}s")
