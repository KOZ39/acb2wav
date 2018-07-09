# acb2wav
> Enjoy the Sound

## System Requirements
* Windows 7 or later
* [Microsoft Visual C++ Redistributable 2015](https://www.microsoft.com/en-us/download/details.aspx?id=48145)

## Release
[Here](https://github.com/KOZ39/acb2wav/releases)

## Run from Source
* [Python 3.5+](https://www.python.org/)
* [acbpy (Destrapier)](https://github.com/Destrapier/acbpy)
* [hcapy (Destrapier)](https://github.com/Destrapier/hcapy)

## Usage
```
acb2wav.exe [Options]

Options:
 -v, --version      show version and exit
 -k, --key          Default: 00003657f27e3b22
 -e, --extension    Default: acb.bytes
 -i, --inputDir     Default: acb
 -o, --outputDir    Default: wav
 -ns, --noSubDir    Default: False
```

```
acb2wav.exe -k 00000000000022CE -e acb.txt -ns
acb2wav.exe -k 8910 -e acb.txt -ns
```

## Other Tools
* [AssetStudio](https://github.com/Perfare/AssetStudio)
* [DereTore](https://github.com/OpenCGSS/DereTore)
* [HxD](https://mh-nexus.de/en/hxd/)

## License
[MIT](https://github.com/KOZ39/acb2wav/blob/master/LICENSE)
