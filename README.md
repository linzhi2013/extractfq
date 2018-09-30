# depth_stat

## 1 Introduction

`depth_stat` is a tool to extract the sequence depth from depthfile and do some statstics.

see `https://github.com/linzhi2013/depth_stat`.

## 2 Installation

    pip install depth_stat

There will be a command `depth_stat` created under the same directory as your `pip` command.

## 3 Usage

### 3.1 command line

    $ depth_stat
    usage: depth_stat [-h] -i <file> [-q <str>] [-a <int>] [-b <int>]
                         [-f <file>]

    To extract the sequence depth from depthfile.

    The depthfile content format:
    seqid1 depth1 depth2 depth3 ...
    seqid2 depth1 depth2 depth3 ...

    This script is part of the MitoZ project, by Guanliang MENG.
    See https://github.com/linzhi2013/depth_stat.


    optional arguments:
      -h, --help  show this help message and exit
      -i <file>   input depthfile
      -q <str>    sequence id
      -a <int>    the start position, Python-style (0-leftmost)
      -b <int>    the end position, Python-style for slicing
      -f <file>   a file of 'seqid start end' list on each line


### 3.2 in a Python3 script

    In [1]: from depth_stat import SeqDepth

    In [2]: sdj = SeqDepth('DRR095708_mitoscaf.fa.fsa.depth')

    In [3]: sdj.extract_range_depth(seqid='scaffold44450', start=0, end=20)
    Out[3]: [1, 1, 1, 1, 4, 4, 4, 4, 5, 5, 5, 6, 7, 7, 8, 8, 8, 8, 8, 8]

    In [4]: sdj.range_depth_stat(seqid='scaffold44450', start=0, end=20)
    Out[4]: ('scaffold44450', 0, 20, 1, 5.15, 8)

    In [5]: sdj.range_depth_freq(seqid='scaffold44450', start=0, end=20)
    Out[5]: [(1, 4), (4, 4), (5, 3), (6, 1), (7, 2), (8, 6)]



## Author
Guanliang MENG

## Citation
This script is part of the package `MitoZ`, when you use the script in your work, please cite:
    
    MitoZ: A toolkit for mitochondrial genome assembly, annotation and visualization with NGS data. Guangliang Meng, Yiyuan Li, Chentao Yang, Shanlin Liu (in manuscript)






