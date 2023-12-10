'''This is the Final assignment for python for networking security
    Created By Torrance Mooradian Student #000279721
    This was created using AI help and tutorials from class
    Date created: December 9th 2023'''

import argparse, FileFindFunction
parser=argparse.ArgumentParser(
    description='Enter arguments to blacklist a dns entry',
)

parser.add_argument(
    '-FQDN',
    default=0,
    help="Enter the fully qualified domain name of the site you wish to blacklist"
)
parser.add_argument(
    "-read",
    action="store_true",
    help="Read the current host file"
)
DnsBHargs=parser.parse_args()
FileFindFunction.OSdetail()
if DnsBHargs.read == True:
    FileFindFunction.Readfile()

if DnsBHargs.FQDN != 0:
    FQDN = str(DnsBHargs.FQDN)
    FileFindFunction.fileappend(FQDN)
    
