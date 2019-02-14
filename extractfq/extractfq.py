#!/usr/bin/python3
"""
Copyright (c) 2017-2018 Guanliang Meng <mengguanliang@foxmail.com>.

This file is part of MitoZ.

MitoZ is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

MitoZ is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with MitoZ.  If not, see <http://www.gnu.org/licenses/>.

"""

import sys
import argparse
import gzip


def get_para():
    description = '''
Extract some fastq reads from the beginning of the files. Author: Guanliang Meng, see https://github.com/linzhi2013/extractfq. This script is part of the package `MitoZ`, when you use the script in your work, please cite: Guanliang Meng, Yiyuan Li, Chentao Yang, Shanlin Liu. MitoZ: A toolkit for mitochondrial genome assembly, annotation and visualization; doi: https://doi.org/10.1101/489955.

    v0.0.3: single-end data support.

    '''
    parser = argparse.ArgumentParser(description=description)

    parser.add_argument("-fq1", metavar="<str>", help="input fastq 1 file")

    parser.add_argument("-fq2", metavar="<str>", help="input fastq 2 file")

    parser.add_argument("-outfq1", metavar="<str>", help="output fastq 1 file")

    parser.add_argument("-outfq2", metavar="<str>", help="output fastq 2 file")

    parser.add_argument("-size_required", type=float, default=3,
        metavar="<float>", help="size required in Gigabase. [%(default)s]")

    parser.add_argument("-rl", type=int, metavar="<int>", default=0,
        help="read length required. discard the smaller ones, and cut the longer ones to this length")

    parser.add_argument("-gz", action="store_true", default=False,
        help="gzip output. [%(default)s]")

    parser.add_argument('-cache_num', type=int, metavar='<int>',
        default=1500000, help='the cache number of reads before writing to the file, to speed up. the larger of cache_num, the more memory (default is ca. 2G) will be used. [%(default)s]')

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()

    return parser.parse_args()


def extract_fq(fq1=None, fq2=None, outfq1=None, outfq2=None, size_required=None, rl_required=None, gz=True, cache_num=2000000):

    size_required = size_required * (10**9)

    if fq1.endswith(".gz"):
        fh1 = gzip.open(fq1, 'rt')
        fh2 = gzip.open(fq2, 'rt')
    else:
        fh1 = open(fq1, 'rt')
        fh2 = open(fq2, 'rt')

    if gz:
        if not outfq1.endswith(".gz"):
            outfq1 += ".gz"
        if not outfq2.endswith(".gz"):
            outfq2 += ".gz"
        fhout1 = gzip.open(outfq1, 'wt')
        fhout2 = gzip.open(outfq2, 'wt')
    else:
        fhout1 = open(outfq1, 'wt')
        fhout2 = open(outfq2, 'wt')

    size_got = 0

    flines = []
    rlines = []
    for f_title in fh1:
        # fastq 1
        f_title = f_title.rstrip()
        f_seq = fh1.readline().rstrip()
        f_third = fh1.readline().rstrip()
        f_quality = fh1.readline().rstrip()

        # fastq 2
        r_title = fh2.readline().rstrip()
        r_seq = fh2.readline().rstrip()
        r_third = fh2.readline().rstrip()
        r_quality = fh2.readline().rstrip()

        f_seq_len = len(f_seq)
        r_seq_len = len(r_seq)
        if rl_required:
            if (f_seq_len < rl_required) or (r_seq_len < rl_required):
                continue
            f_seq = f_seq[0:rl_required]  # the seq line
            f_quality = f_quality[0:rl_required]  # the quality line

            r_seq = r_seq[0:rl_required]  # the seq line
            r_quality = r_quality[0:rl_required]  # the quality line

            # now reset the seq length, v3 version fixed.
            f_seq_len = r_seq_len = rl_required

        # stat length
        size_got += f_seq_len + r_seq_len

        fline = "\n".join([f_title, f_seq, f_third, f_quality])
        rline = "\n".join([r_title, r_seq, r_third, r_quality])
        flines.append(fline)
        rlines.append(rline)

        if len(flines) >= cache_num:
            print('\n'.join(flines), file=fhout1)
            print('\n'.join(rlines), file=fhout2)
            flines = []
            rlines = []

        if size_got >= size_required:
            # the last parts
            if len(flines) >= 1:
                print('\n'.join(flines), file=fhout1)
                print('\n'.join(rlines), file=fhout2)
                flines = []
                rlines = []
            break

    # if the data is not enough as size_required
    if len(flines)>0 and len(rlines)>0:
        print('\n'.join(flines), file=fhout1)
        print('\n'.join(rlines), file=fhout2)
        flines = []
        rlines = []

    fh1.close()
    fh2.close()
    fhout1.close()
    fhout2.close()

    size_required = int(size_required)
    print("Base required:", format(size_required, ","))
    print("Base got:", format(size_got, ","))

    return size_got


def extract_se_fq(fq1=None, outfq1=None, size_required=None, rl_required=None, gz=True, cache_num=2000000):

    size_required = size_required * (10**9)

    if fq1.endswith(".gz"):
        fh1 = gzip.open(fq1, 'rt')
    else:
        fh1 = open(fq1, 'rt')

    if gz:
        if not outfq1.endswith(".gz"):
            outfq1 += ".gz"
        fhout1 = gzip.open(outfq1, 'wt')
    else:
        fhout1 = open(outfq1, 'wt')

    size_got = 0

    flines = []
    for f_title in fh1:
        # fastq 1
        f_title = f_title.rstrip()
        f_seq = fh1.readline().rstrip()
        f_third = fh1.readline().rstrip()
        f_quality = fh1.readline().rstrip()

        f_seq_len = len(f_seq)
        if rl_required:
            if f_seq_len < rl_required:
                continue
            f_seq = f_seq[0:rl_required]  # the seq line
            f_quality = f_quality[0:rl_required]  # the quality line

            # now reset the seq length, v3 version fixed.
            f_seq_len = rl_required

        # stat length
        size_got += f_seq_len

        fline = "\n".join([f_title, f_seq, f_third, f_quality])
        flines.append(fline)

        if len(flines) >= cache_num:
            print('\n'.join(flines), file=fhout1)
            flines = []

        if size_got >= size_required:
            # the last parts
            if len(flines) >= 1:
                print('\n'.join(flines), file=fhout1)
                flines = []
            break

    # if the data is not enough as size_required
    if len(flines)>0:
        print('\n'.join(flines), file=fhout1)
        flines = []

    fh1.close()
    fhout1.close()

    size_required = int(size_required)
    print("Base required:", format(size_required, ","))
    print("Base got:", format(size_got, ","))

    return size_got



def main():
    args = get_para()

    if args.fq1 and args.fq2:
        extract_fq(fq1=args.fq1, fq2=args.fq2, outfq1=args.outfq1,
                   outfq2=args.outfq2, size_required=args.size_required,
                   rl_required=args.rl, gz=args.gz, cache_num=args.cache_num)
        return (args.outfq1, args.outfq2, args.size_required)

    else:
        if not args.fq1 and args.fq2:
            args.fq1 = args.fq2

        if not args.outfq1 and args.outfq2:
            args.outfq1 = args.outfq2

        extract_se_fq(fq1=args.fq1, outfq1=args.outfq1,
                    size_required=args.size_required,
                   rl_required=args.rl, gz=args.gz, cache_num=args.cache_num)

        return (args.outfq1, args.size_required)


if __name__ == "__main__":
    main()
