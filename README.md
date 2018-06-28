# acb2wav
> Enjoy the Sound

## Dependencies
* [Python 3.5+](https://www.python.org/)
* [acbpy (Destrapier)](https://github.com/Destrapier/acbpy)
* [hcapy (Destrapier)](https://github.com/Destrapier/hcapy)

## Usage
```
acb2wav.exe [Options]

Options:
 -k1, --key1        Default: f27e3b22
 -k2, --key2        Default: 00003657
 -e, --extension    Default: acb.bytes
 -i, --inputDir     Default: acb
 -o, --outputDir    Default: wav
 -ns, --noSub       Default: False
```

```
acb2wav.exe -k1 00000000000022CE -k2 0 -e acb.txt -ns
```

## License
[MIT](https://github.com/KOZ39/acb2wav/blob/master/LICENSE)
