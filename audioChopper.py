#!/usr/local/bin/python

import argparse
import subprocess

ap = argparse.ArgumentParser(description='Chop up an audio file using ffmpeg')
ap.add_argument(dest='ifile', type=str, help='Input audio file')
ap.add_argument('-p', '--pieces', dest='pieces', type=int, required=True, help='How many pieces')
ap.add_argument('-s', '--size', dest='size', type=int, default=1, required=False, help='The duration of each piece in hours')
ap.add_argument('-t', '--title', dest='title', type=str, required=False, help='Overwrite title in output tracks')
args = ap.parse_args()


for ii in xrange(0, args.pieces):
  ofile = args.ifile.rsplit('.')[0] + '-' + str(ii+1).zfill(3) + "." + args.ifile.rsplit('.')[1]
  s = "/usr/local/bin/ffmpeg -ss " + str(ii*args.size) + ":00:00 -i " + args.ifile + " -acodec copy -to 0" + str(args.size) + ":00:00"
  s += " -metadata track=" + str(ii+1) + "/" + str(args.pieces) + " "
  if args.title != None:
    s += "-metadata title=" + args.title + " "
  s += ofile
  #print(s)
  print(str(subprocess.check_output(s.split(), stderr=subprocess.STDOUT)))

