#!/usr/bin/env python3

import time
import glob
import pathlib
import os

import acbpy
import hcapy

start = time.time()

d = hcapy.Decoder(6306816832864825)

for i in glob.iglob("acb/**/*.acb.bytes", recursive=True):
    with open(i, "rb") as f:
        dirName = os.path.join("wav", os.path.basename(i).split(".")[0])

        pathlib.Path(dirName).mkdir(parents=True, exist_ok=True)
        
        for i in acbpy.parse_binary(f):
            print(i.track.name)

            try:
                with open(f"{dirName}/{i.track.name}.wav", "wb") as s:
                    s.write(d.decode(i.binary.read()).read())
            except hcapy.InvalidHCAError:
                print("Invalid hca!")

end = time.time()

print(f"Time: {end - start:.3f}s\n")

os.system("pause")
