

print("\\Clear");

// Implements a local version of Otsu's global threshold clustering. The algorithm searches for the threshold that minimizes the intra-class variance, defined as a weighted sum of variances of the two classes. The local set is a circular ROI and the central pixel is tested against the Otsu threshold found for that region.
// r - radius of window around pixel
// Parameter 1: ------
// Parameter 2: ------

for(r=29;r<=70;r+=4){
    id=""+r+"_0_0";
	path="C:/Users/x/gs/masterBio/code/corneal_endothelium/result/otsu/"+id+"/";
	string = path+" Otsu "+r+ " 0 0";
	runMacro("C:/Users/x/gs/masterBio/code/corneal_endothelium/macro/set/run_method.ijm", string);

	runMacro("C:/Users/x/gs/masterBio/code/corneal_endothelium/macro/set/run_bestfit.ijm", path);
	
	print("-------------------------------");

}


selectWindow("Log");
saveAs("Text", "C:/Users/x/gs/masterBio/code/corneal_endothelium/result/otsu/logs.txt");