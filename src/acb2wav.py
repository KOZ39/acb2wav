#!/usr/bin/env python3

import argparse
import time
import sys
import glob
import os
import pathlib

import acbpy
import hcapy

parser = argparse.ArgumentParser()

parser.add_argument("-k1", "--key1", metavar="", default="f27e3b22", help="Default: f27e3b22")
parser.add_argument("-k2", "--key2", metavar="", default="00003657", help="Default: 00003657")
parser.add_argument("-e", "--extension", metavar="", default="acb.bytes", help="Default: acb.bytes")
parser.add_argument("-i", "--inputDir", metavar="", default="acb", help="Default: acb")
parser.add_argument("-o", "--outputDir", metavar="", default="wav", help="Default: wav")
parser.add_argument("-ns", "--noSubDir", action="store_true", help="Default: False")

args = parser.parse_args()

start = time.time()

d = hcapy.Decoder(args.key1, args.key2)

for i in glob.iglob(f"{args.inputDir}/**/*.{args.extension}", recursive=True):
    with open(i, "rb") as f:
        if args.noSubDir:
            dirName = args.outputDir
        else:
            dirName = os.path.join(args.outputDir, os.path.basename(i).split(".")[0])

        pathlib.Path(dirName).mkdir(parents=True, exist_ok=True)
 
        for i in acbpy.parse_binary(f):
            print(f"{i.track.name}.wav")

            try:
                with open(f"{dirName}/{i.track.name}.wav", "wb") as s:
                    s.write(d.decode(i.binary.read()).read())
            except hcapy.InvalidHCAError:
                print("Invalid hca!")

        print()

end = time.time()

print(f"Time: {end - start:.3f}s\n")

os.system("pause")
