#!/usr/bin/env python3


def parse(ss_file):

    """Reads secondary structure file, ss2 or ss3
    @param  ss_file, ss2 or ss3 fasta-formated ss-file
    @return secondary structure string.
    """

    result = ''
    for line in ss_file:
        if line.startswith('>'):
            continue
        result = line.strip()
    return result
