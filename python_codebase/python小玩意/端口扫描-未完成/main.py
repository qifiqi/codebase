import optparse

parser = optparse.OptionParser(
    'usage %prog -H' + '<target host> -P <target port>'
)

parser.add_option(
    '-H',
    dest="tgtHost",
    type="string",
    help="specify target host"
)
parser.add_option(
    "-P",
    dest="tgtPort",
    type="int",
    help="specify target port"
)
options, args = parser.parse_args()


tgtHost = options.tgtHost
tgtPort = options.tgtPort

if tgtHost==None or tgtPort ==None:
    print(parser.usage)
    exit(0)

