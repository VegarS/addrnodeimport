#!/usr/bin/env python3
#
# addrnodeimport.py
#
# (c) Ruben Undheim 2014
#
#   This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 2 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program; if not, write to the Free Software
#   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

munipfirst=False

import os
import sys
import glob
import re

if len(sys.argv) != 3 and len(sys.argv) != 4:
	print ("Missing command line argument.\nUsage: "+sys.argv[0]+" <top-zip-file> <municipality number>")
	sys.exit()

if len(sys.argv) == 4 and sys.argv[3] == "1":
	network=False
else:
	network=True

topzipfile = sys.argv[1]
munipnumber = sys.argv[2]
munipnumberpadded = "%04d" % (int(munipnumber))
basenametopzipfile = os.path.basename(topzipfile)
prefix = basenametopzipfile.split('.')[0]

#apiurl = "http://overpass-api.de/api"
apiurl = "http://overpass.osm.rambler.ru/cgi"

if not os.path.isdir(prefix):
	os.system("unzip "+topzipfile+" -d "+prefix+"")

if not os.path.isfile(prefix+"/"+str(munipnumberpadded)+"Adresser.SOS"):
	ret = os.system("cd "+prefix+" ; unzip "+str(munipnumberpadded)+"Elveg.zip");
	if ret != 0:
		print ("Failed to find this municipality")
		sys.exit()

os.system("sosi2osm "+prefix+"/"+str(munipnumberpadded)+"Adresser.SOS adresser.lua > "+prefix+"/"+str(munipnumberpadded)+"Adresser.osm")

osmfilename = prefix+"/"+str(munipnumberpadded)+"Adresser.osm"

if not os.path.isdir("/tmp/osm_temp"):
	os.system("mkdir -p /tmp/osm_temp");


boundarea = os.popen("getedges -m 0.01 "+osmfilename).read()
if network:
	os.system("rm -rf /tmp/osm_temp/ways_"+munipnumberpadded+".osm")
	os.system("rm -rf /tmp/osm_temp/nodes_"+munipnumberpadded+".osm")
	if not os.path.isfile("/tmp/osm_temp/ways_"+munipnumberpadded+".osm" ):
		os.system(" wget \""+apiurl+"/interpreter?data=((way[\\\"addr:housenumber\\\"] "+boundarea+";>;);(way[\\\"abandoned:addr:housenumber\\\"] "+boundarea+";>;););out meta;\" -O /tmp/osm_temp/ways_"+munipnumberpadded+".osm")
	if not os.path.isfile("/tmp/osm_temp/nodes_"+munipnumberpadded+".osm" ):
		os.system(" wget \""+apiurl+"/interpreter?data=((node[\\\"addr:housenumber\\\"] "+boundarea+";<;);(node[\\\"abandoned:addr:housenumber\\\"] "+boundarea+";<;););out meta;\" -O /tmp/osm_temp/nodes_"+munipnumberpadded+".osm")
else:
	os.system("rm -rf /tmp/osm_temp/ways_"+munipnumberpadded+".osm")
	os.system("rm -rf /tmp/osm_temp/nodes_"+munipnumberpadded+".osm")
	print (boundarea)
	boundareamatch = re.compile("\((\d+\.\d+),(\d+\.\d+),(\d+\.\d+),(\d+\.\d+)\)")
	matches = boundareamatch.match(boundarea)
	bottomcoord = matches.group(1)
	leftcoord = matches.group(2)
	topcoord = matches.group(3)
	rightcoord = matches.group(4)
	if munipfirst:
		print ("\nExtracting municipality from pbf:")
		os.system("osmosis --read-pbf file=\"/home/ruben/norway-latest.osm.pbf\" --bounding-box bottom="+bottomcoord+" left="+leftcoord+" top="+topcoord+" right="+rightcoord+" --write-pbf file=\"/tmp/osm_temp/objects_"+munipnumberpadded+".pbf\"")
		print ("\nExtracting address nodes:")
		os.system("osmosis --read-pbf file=\"/tmp/osm_temp/objects_"+munipnumberpadded+".pbf\" --tf accept-nodes \"addr:housenumber\"=* --tf reject-ways --tf reject-relations --write-xml file=\"/tmp/osm_temp/nodes_"+munipnumberpadded+"-tmp1.osm\"")
		os.system("osmosis --read-pbf file=\"/tmp/osm_temp/objects_"+munipnumberpadded+".pbf\" --tf accept-nodes \"abandoned:addr:housenumber\"=* --tf reject-ways --tf reject-relations --write-xml file=\"/tmp/osm_temp/nodes_"+munipnumberpadded+"-tmp2.osm\"")
		os.system("osmosis --rx \"/tmp/osm_temp/nodes_"+munipnumberpadded+"-tmp1.osm\" --rx \"/tmp/osm_temp/nodes_"+munipnumberpadded+"-tmp2.osm\" --merge --wx \"/tmp/osm_temp/nodes_"+munipnumberpadded+".osm\"")
		print ("\nExtracting address ways:")
		os.system("rm -rf /tmp/osm_temp/nodes_"+munipnumberpadded+"-tmp1.osm /tmp/osm_temp/nodes_"+munipnumberpadded+"-tmp2.osm")
		os.system("osmosis --read-pbf file=\"/tmp/osm_temp/objects_"+munipnumberpadded+".pbf\" --tf accept-ways \"addr:housenumber\"=* --tf reject-relations --used-node idTrackerType=Dynamic --write-xml file=\"/tmp/osm_temp/ways_"+munipnumberpadded+"-tmp1.osm\"")
		os.system("osmosis --read-pbf file=\"/tmp/osm_temp/objects_"+munipnumberpadded+".pbf\" --tf accept-ways \"abandoned:addr:housenumber\"=* --tf reject-relations --used-node idTrackerType=Dynamic --write-xml file=\"/tmp/osm_temp/ways_"+munipnumberpadded+"-tmp2.osm\"")
		os.system("osmosis --rx \"/tmp/osm_temp/ways_"+munipnumberpadded+"-tmp1.osm\" --rx \"/tmp/osm_temp/ways_"+munipnumberpadded+"-tmp2.osm\" --merge --wx \"/tmp/osm_temp/ways_"+munipnumberpadded+".osm\"")
		os.system("rm -rf /tmp/osm_temp/ways_"+munipnumberpadded+"-tmp1.osm /tmp/osm_temp/ways_"+munipnumberpadded+"-tmp2.osm /tmp/osm_temp/objects_"+munipnumberpadded+".pbf")
	else:
		if not os.path.isfile("/tmp/osm_temp/nodes.pbf") or not os.path.isfile("/tmp/osm_temp/ways.pbf"):
			print ("\nExtracting all way addresses:")
			os.system("osmosis --read-pbf file=\"/home/ruben/norway-latest.osm.pbf\" --tf accept-ways \"addr:housenumber\"=* --tf reject-relations --used-node idTrackerType=Dynamic --write-pbf file=\"/tmp/osm_temp/ways-tmp1.pbf\"")
			os.system("osmosis --read-pbf file=\"/home/ruben/norway-latest.osm.pbf\" --tf accept-ways \"abandoned:addr:housenumber\"=* --tf reject-relations --used-node idTrackerType=Dynamic --write-pbf file=\"/tmp/osm_temp/ways-tmp2.pbf\"")
			os.system("osmosis --read-pbf \"/tmp/osm_temp/ways-tmp1.pbf\" --read-pbf \"/tmp/osm_temp/ways-tmp2.pbf\" --merge --write-pbf \"/tmp/osm_temp/ways.pbf\"")
			print ("\nExtracting all node addresses:")
			os.system("osmosis --read-pbf file=\"/home/ruben/norway-latest.osm.pbf\" --tf accept-nodes \"addr:housenumber\"=* --tf reject-ways --tf reject-relations --write-pbf file=\"/tmp/osm_temp/nodes-tmp1.pbf\"")
			os.system("osmosis --read-pbf file=\"/home/ruben/norway-latest.osm.pbf\" --tf accept-nodes \"abandoned:addr:housenumber\"=* --tf reject-ways --tf reject-relations --write-pbf file=\"/tmp/osm_temp/nodes-tmp2.pbf\"")
			os.system("osmosis --read-pbf \"/tmp/osm_temp/nodes-tmp1.pbf\" --read-pbf \"/tmp/osm_temp/nodes-tmp2.pbf\" --merge --write-pbf \"/tmp/osm_temp/nodes.pbf\"")
		print ("\nGet ways for municipality:")
		os.system("osmosis --read-pbf file=\"/tmp/osm_temp/ways.pbf\" --bounding-box bottom="+bottomcoord+" left="+leftcoord+" top="+topcoord+" right="+rightcoord+" --write-xml file=\"/tmp/osm_temp/ways_"+munipnumberpadded+".osm\"")
		print ("\nGet nodes for municipality:")
		os.system("osmosis --read-pbf file=\"/tmp/osm_temp/nodes.pbf\" --bounding-box bottom="+bottomcoord+" left="+leftcoord+" top="+topcoord+" right="+rightcoord+" --write-xml file=\"/tmp/osm_temp/nodes_"+munipnumberpadded+".osm\"")

if not os.path.isfile("munip_borders/"+str(munipnumberpadded)+".osm"):
	alreadyextracted = glob.glob("munip_borders/"+munipnumberpadded+"/"+str(munipnumberpadded)+"*_Adm*.sos")
	if alreadyextracted == None or len(alreadyextracted) == 0:
		print (alreadyextracted)
		zipfiles = glob.glob("/home/ruben/n50/Kartdata_"+str(munipnumber)+"_*N50_SOSI.zip")
		if zipfiles != None and len(zipfiles) > 0:
			zipfile = zipfiles[0]
			print ("there is"+zipfile)
			os.system("mkdir -p munip_borders")
			os.system("unzip "+zipfile+" -d munip_borders/"+munipnumberpadded+"")

			adminfiles = glob.glob("munip_borders/"+munipnumberpadded+"/"+str(munipnumberpadded)+"*_Adm*.sos")
			if adminfiles != None and len(adminfiles) > 0:
				adminfile = adminfiles[0]
				print ("here now "+adminfile)
				os.system("sosi2osm "+adminfile+" default.lua > munip_borders/"+munipnumberpadded+".osm")
			os.system("osmosispolygon -o munip_borders/"+str(munipnumberpadded)+"-tmp.osm munip_borders/"+munipnumberpadded+".osm")
			os.system("sed -i 's/>/>\\n/g' munip_borders/"+munipnumberpadded+"-tmp.osm")
			os.system("mv munip_borders/"+str(munipnumberpadded)+"-tmp.osm munip_borders/"+munipnumberpadded+".osm")

if os.path.isfile("munip_borders/"+str(munipnumberpadded)+".osm"):
	os.system("perl ../perl/osm2poly.pl munip_borders/"+str(munipnumberpadded)+".osm > munip_borders/"+str(munipnumberpadded)+".txt")
	os.system("osmosis --read-xml enableDateParsing=no file=\"/tmp/osm_temp/ways_"+munipnumberpadded+".osm\" --bounding-polygon file=\"munip_borders/"+str(munipnumberpadded)+".txt\" --write-xml file=/tmp/osm_temp/ways_"+munipnumberpadded+"-tmp.osm")
	os.system("mv /tmp/osm_temp/ways_"+munipnumberpadded+"-tmp.osm /tmp/osm_temp/ways_"+munipnumberpadded+".osm")
	os.system("osmosis --read-xml enableDateParsing=no file=\"/tmp/osm_temp/nodes_"+munipnumberpadded+".osm\" --bounding-polygon file=\"munip_borders/"+str(munipnumberpadded)+".txt\" --write-xml file=/tmp/osm_temp/nodes_"+munipnumberpadded+"-tmp.osm")
	os.system("mv /tmp/osm_temp/nodes_"+munipnumberpadded+"-tmp.osm /tmp/osm_temp/nodes_"+munipnumberpadded+".osm")
	os.system("osmosis --read-xml enableDateParsing=no file=\""+osmfilename+"\" --bounding-polygon file=\"munip_borders/"+str(munipnumberpadded)+".txt\" --write-xml file=/tmp/osm_temp/newnodeswithin_"+munipnumberpadded+"-tmp.osm")
	beforenumber = os.popen("countnodes "+osmfilename+"").read()
	afternumber = os.popen("countnodes /tmp/osm_temp/newnodeswithin_"+munipnumberpadded+"-tmp.osm").read()
	reportfile3 = open("reports/report3_"+munipnumberpadded+".txt","w")
	reportfile3.write("Before: "+beforenumber+"After: "+afternumber+"")
	reportfile3.close()


os.system("mkdir -p reports")
print ("Processing "+munipnumberpadded+"...")
reportcontent = os.popen("getmissingandreport -s -t reports/veivegfixes_"+munipnumberpadded+".osm -n reports/notmatched_"+munipnumberpadded+".osm -d reports/duplicates_"+munipnumberpadded+".osm -e reports/otherobjects_"+munipnumberpadded+".osm -o reports/newnodes_"+munipnumberpadded+".osm -w /tmp/osm_temp/ways_"+munipnumberpadded+".osm -c ../xml/corrections.xml  /tmp/osm_temp/nodes_"+munipnumberpadded+".osm "+osmfilename+"").read()
reportcontent2 = os.popen("fillinpostcode -c ../xml/corrections.xml -o reports/postcodecityfixes_"+munipnumberpadded+".osm -n reports/onlynumber_"+munipnumberpadded+".osm -s /tmp/osm_temp/nodes_"+munipnumberpadded+".osm -w /tmp/osm_temp/ways_"+munipnumberpadded+".osm "+osmfilename+"").read()

reportfile = open("reports/report_"+munipnumberpadded+".txt","w")
reportfile.write(reportcontent)
reportfile.close()

reportfile2 = open("reports/report2_"+munipnumberpadded+".txt","w")
reportfile2.write(reportcontent2)
reportfile2.close()

