# extractfq

## 1 Introduction

`extractfq` is a tool to extract some fastq reads from the beginning of the files.

## 2 Installation

    pip install extractfq

There will be a command `extractfq` created under the same directory as your `pip` command.

## 3 Usage

    $ extractfq
    usage: extractfq.py [-h] [-fq1 <str>] [-fq2 <str>] [-outfq1 <str>]
                        [-outfq2 <str>] [-size_required <float>] [-rl <int>] [-gz]
                        [-cache_num <int>]

    Extract some fastq reads from the beginning of the files. Author: Guanliang
    Meng, see https://github.com/linzhi2013/extractfq. This script is part of the
    package `MitoZ`, when you use the script in your work, please cite: MitoZ: A
    toolkit for mitochondrial genome assembly, annotation and visualization with
    NGS data. Guangliang Meng, Yiyuan Li, Chentao Yang, Shanlin Liu (in
    manuscript)

    optional arguments:
      -h, --help            show this help message and exit
      -fq1 <str>            input fastq 1 file
      -fq2 <str>            input fastq 2 file
      -outfq1 <str>         output fastq 1 file
      -outfq2 <str>         output fastq 2 file
      -size_required <float>
                            size required in Gigabase. [3]
      -rl <int>             read length required. discard the smaller ones, and
                            cut the longer ones to this length [None]
      -gz                   gzip output. [False]
      -cache_num <int>      the cache number of reads before writing to the file,
                            to speed up. the larger of cache_num, the more memory
                            (default is ca. 2G) will be used. [1500000]

## Author
Guanliang MENG

## Citation
This script is part of the package `MitoZ`, when you use the script in your work, please cite:

    Guanliang Meng, Yiyuan Li, Chentao Yang, Shanlin Liu. MitoZ: A toolkit for mitochondrial genome assembly, annotation and visualization; doi: https://doi.org/10.1101/489955







