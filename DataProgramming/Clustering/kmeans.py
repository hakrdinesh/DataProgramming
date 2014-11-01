#!/C/Python34/python.exe

import math
import random

def PrintPoint(point, prefix = ""):
	print(prefix, "{", 
		point["id"], 
		",", point["name"], 
		",", point["x"], 
		",", point["y"], 
		",", point["belongs_to_cluster_id"], 
		"}")

# End of PrintPoint

def MakePoint(id, name, x, y, cluster_id):
	debug = False
	p = {}

	p["id"] = id;
	p["name"] = name;
	p["x"] = x
	p["y"] = y
	p["belongs_to_cluster_id"] = cluster_id

	if (debug):
		PrintPoint(p, "MakePoint")

	return p

# End of MakePoint

POINTS = {}

def InitialisePoints(filename):
	datafile = open(filename, "r")
	npoints = 0
	for line in datafile:
		debug = True
		line = line.strip()
		if line.startswith("#"):
			continue
		if (line == ""):
			continue
		( name, donation, visitor ) = line.split(",")
		if (debug):
			print("line is ", line)
			print("Name is ", name)
			print("Donation Score is ", int(donation))
			print("Visitor Score is ", int(visitor))
		id = 1+npoints
		x = int(donation.strip())
		y = int(visitor.strip())
		cluster_id = -1
		point = MakePoint(id, name, x, y, cluster_id)
		POINTS[id] = point
		npoints += 1

	return npoints
# end of reading comma separated values in file

def GetNumberOfPoints(d):
	return len(list(d.keys()))

def PrintPoints(d, prefix = ""):
	npoints = GetNumberOfPoints(d)
	for id in range(1, npoints+1):
		PrintPoint(d[id], prefix+"Data Point-"+str(id))

def GenerateKRandomPoints(k, points):
	nrseen = 0		# number of random values seen
	random_min = 1
	random_max = k
	krandompointids = []	# local list of k random point ids
	npoints = GetNumberOfPoints(points)
	while not (nrseen == k):
		debug = False
		already_seen = {}	# dictionary to store if we have seen 
					# this random value or not
		if (debug):
			print("For nrseen = ", nrseen)
		random_value = random.randint(1, npoints)
		if (debug):
			print("Random Value is ", random_value)
		if (random_value not in already_seen.keys()):
			if (debug):
				print("DEBUG: new random value seen", random_value)
			# remember we have observed one more random point
			already_seen[random_value] = 1
			# increment the total number of random points generated
			nrseen += 1
			krandompointids.append(random_value)
		else:
			if (debug):
				print("DEBUG: old random value seen", random_value)
				print("DEBUG: not including this random value")
			# okay, we have seen this before
			# nothing new, so move on
			already_seen[random_value] += 1

	return krandompointids

# end of GenerateKRandomPointIds

def GenerateCentroids0(points, random_point_ids):
	debug = False
	global CENTROIDS
	CENTROIDS = {}
	cid = 0
	for i in random_point_ids:
		# copy value to centroid with name "centroid-1", "centroid-2"
		cid += 1			# centroid id
		if (debug):
			print("Generating Centroid", cid, "from Data Point", i)
			PrintPoint(points[i], "MotherDataPoint")
		point = points[i]

		cname 	= "centroid-" + str(cid)# centroid name
		cx 	= point["x"]		# centroid x coordinate
		cy 	= point["y"]		# centroid y coordinate
		cluster_id = 10001*cid		# cluster id of centroid

		centroid = MakePoint(cid, cname, cx, cy, cluster_id)
		if (debug):
			PrintPoint(centroid, "FirstCentroid")
		CENTROIDS[cname] = centroid		# store the centroid by name

def PrintCentroids(d):
	for k in d.keys():
		v = d[k]
		PrintPoint(v, "New Centroid")

# end of PrintCentroids

def DistanceBetween(a, b):
	debug = False
	x1 = float(a["x"])
	y1 = float(a["y"])
	x2 = float(b["x"])
	y2 = float(b["y"])
	dx = x1 - x2
	dy = y1 - y2
	distance = math.sqrt(dx*dx + dy*dy)
	if (debug):
		print("Distance is ", distance)
	return distance

# end of DistanceBetween

def PointGetX(point):
	return point["x"]

def PointGetY(point):
	return point["y"]

def PointGetClusterId(point):
	return point["belongs_to_cluster_id"]

def CentroidGetClusterId(centroid):
	return centroid["belongs_to_cluster_id"]

def DoPointAssignmentToClusters():
	global POINTS
	global CENTROIDS
	debug = False
	nreassignments = 0
	for p in list(POINTS.keys()):
		point = POINTS[p]
		dmin = -1.0
		closest = None
		# closest_centroid_id = -1
		# find shortest distance to all centroids
		for c in list(CENTROIDS.keys()): 
			centroid = CENTROIDS[c]
			d = DistanceBetween(point, centroid)
			if (debug):
				print("Distance Computation between Point P and Centroid C")
				PrintPoint(point, "Point P")
				PrintPoint(centroid, "Centroid C")
				print("Distance Between P and C is ", d)
			if (dmin < 0.0):
				dmin = d
				# closest_centroid_id = centroid["id"]
				closest = centroid
			else:
				if (d < dmin):
					dmin = d
					# closest_centroid_id = centroid["id"]
					closest = centroid

		# found closest centroid
		if (debug):
			PrintPoint(point, "For Candidate Point P")
			PrintPoint(closest, "Closest Centroid")
			print("Shortest Distance Between P and C is ", d)

		# set point to closest centroid
		oldclusterid = PointGetClusterId(point)
		newclusterid = CentroidGetClusterId(closest)
		if (debug):
			print("Centroid C has New Cluster Id", newclusterid)

		# update point to this cluster 
		if (newclusterid == oldclusterid):
			if (debug):
				print("Point P already in correct Cluster C")
		else:
			nreassignments += 1
			point["belongs_to_cluster_id"] = newclusterid

		if (debug):
			PrintPoint(point, 
				"Point P assigned"+
				" from Old Cluster "+str(oldclusterid)+
				" to New Cluster "+str(newclusterid))
	
	print("Cluster Assignmnent Score", nreassignments)
	return (nreassignments > 0)

# end of DoPointAssignmentToClusters

def ComputeDistance(ox, oy, nx, ny):
	dx = nx - ox
	dy = ny - oy
	return math.sqrt(dx*dx + dy*dy)

def ComputeNewCentroids():
	debug = False
	centroidsMoved = False
	for key in list(CENTROIDS.keys()):
		if (debug):
			print("Compute New Centroid Key is", key)
		centroid = CENTROIDS[key]
		cluster_id = CentroidGetClusterId(centroid)
		print("Compute New Centroid Cluster Id is", cluster_id)
		sumx = 0.0
		sumy = 0.0
		npoints = 0
		for p in list(POINTS.keys()):
			point = POINTS[p]
			if not (cluster_id == PointGetClusterId(point)):
				continue
			if (debug):
				print("Compute New Centroid Cluster Point is")
				PrintPoint(point, "ClusterPoint")
			x = float(PointGetX(point))
			y = float(PointGetY(point))
			sumx += x
			sumy += y
			npoints += 1
		
		if (npoints == 0):
			# we will deal with this later
			print("HOUSTON, we have a problem")
			exit(1)
		else:
			oldx = float(PointGetX(centroid))
			oldy = float(PointGetY(centroid))
			newx = sumx/npoints
			newy = sumy/npoints
			d = ComputeDistance(oldx, oldy, newx, newy)
			if (d < 0.0000001):
				if (debug):
					print("The Centroid is now stable")
			else:
				centroidsMoved = True
			if (debug):
				print("New X,Y is (", newx, ",", newy, ")")
			if (debug):
				PrintPoint(centroid, "Old1")
			CENTROIDS[key]["x"] = newx			
			CENTROIDS[key]["y"] = newy			
			if (debug):
				PrintPoint(centroid, "New2")

	PrintCentroids(CENTROIDS)
	return centroidsMoved

# end of ComputeNewCentroids

POINTS = {}
CENTROIDS = {}

# main algorithm
def KMeans(k, filename):
	debug = False
	global POINTS
	POINTS = {}
	InitialisePoints(filename)
	PrintPoints(POINTS)
	KRANDOMPOINTIDS = []	# list of random point ids
	KRANDOMPOINTIDS = GenerateKRandomPoints(k, POINTS)
	GenerateCentroids0(POINTS, KRANDOMPOINTIDS)
	if (debug):
		PrintPoints(POINTS)
	PrintCentroids(CENTROIDS)

	iterations = 0
	done = False
	assignmentsStillHappening = True
	centroidsAreMoving = True

	# only when both 
	#	1. cluster assignment is stable
	#	2. and centroids are stable
	# should we declare we are in steady state

	while assignmentsStillHappening or centroidsAreMoving:
		debug = False
		iterations += 1
		if (DoPointAssignmentToClusters()):
			# assignments happened so continue 
			assignmentsStillHappening = True
			if (debug):
				PrintPoints(POINTS, "Iteration"+str(iterations))
		else:
			# assignments stopped, so stabilised, so stop
			assignmentsStillHappening = False

		centroidsAreMoving = ComputeNewCentroids()

	print("After", iterations, "iterations")
	PrintPoints(POINTS, "Final Assignment")

# end of KMeans

KMeans(3, "kmeans0.csv")


