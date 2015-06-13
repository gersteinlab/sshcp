#!/usr/bin/python 

import subprocess, sys, os, getopt
from subprocess import call

def main(argv):
        chunk = 20
        keyfile = ''
        hostname = ''
        path = ''
        filename = ''

        if len(argv) != 8:
                print 'sshcp.py needs the following arguments!'
                print 'sshcp.py -f <filename> -h <hostname> -p <targetpath> -k <keyfile>'
                sys.exit(2)
        try:
                opts, args = getopt.getopt(argv,"f:h:k:p:",[""])
        except getopt.GetoptError:
                print 'sshcp.py -f <filename> -h <hostname> -p <targetpath> -k <keyfile>'
                sys.exit(2)
        for opt, arg in opts:
                if opt in ("-f"):
                        filename = arg
                elif opt in ("-h"):
                        hostname = arg
                elif opt in ("-p"):
                        path = arg
                elif opt in ("-k"):
                        keyfile = arg
                else:
                        print 'sshcp.py -f <filename> -h <hostname> -p <targetpath> -k <keyfile>'
                        sys.exit(2)

        filesize = os.stat(filename).st_size
        counter = 0
        gbyte = 1024*1024*1024
        print ("filesize: %s" % filesize)
        while ( counter*gbyte < filesize):
                index=counter*gbyte
                print ("counter x gbyte: %s" % index) 
                call ( "dd bs=1024 if=%s skip=%sM count=%sM | ssh -i %s %s \"cat >> %s%s.tmp \" " % ( filename, counter, chunk, keyfile, hostname, path, filename ), shell=True )  
                counter = counter + chunk

        call ("ssh -i %s %s \"mv %s%s.tmp %s%s \"" % (keyfile, hostname, path, filename, path, filename), shell=True )


if __name__ == "__main__":
        main(sys.argv[1:])
