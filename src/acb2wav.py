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

parser.add_argument("-k", "--key", metavar="", default="00003657f27e3b22", help="Default: 00003657f27e3b22")
parser.add_argument("-e", "--extension", metavar="", default="acb.bytes", help="Default: acb.bytes")
parser.add_argument("-i", "--inputDir", metavar="", default="acb", help="Default: acb")
parser.add_argument("-o", "--outputDir", metavar="", default="wav", help="Default: wav")
parser.add_argument("-ns", "--noSubDir", action="store_true", help="Default: False")

args = parser.parse_args()

start = time.time()

d = hcapy.Decoder(args.key)

if args.extension != "*":
    args.extension = "*." + args.extension

for file in glob.iglob(f"{args.inputDir}/**/{args.extension}", recursive=True):
    with open(file, "rb") as f:
        fileName = os.path.basename(file)

        if args.noSubDir:
            dirName = args.outputDir
        else:
            dirName = os.path.join(args.outputDir, fileName.split(".")[0])

        pathlib.Path(dirName).mkdir(parents=True, exist_ok=True)

        try:
            for i in acbpy.parse_binary(f):
                trackName = i.track.name + ".wav"

                print(f"{trackName}")

                try:
                    with open(f"{dirName}/{trackName}", "wb") as s:
                        s.write(d.decode(i.binary.read()).read())
                except hcapy.InvalidHCAError:
                    print("Invalid hca!\n")
        except:
            print(f"{fileName} is invalid acb!\n")

            if not args.noSubDir:
                os.rmdir(dirName)

            continue

        print()

end = time.time()

print(f"Time: {end - start:.3f}s\n")

os.system("pause")
