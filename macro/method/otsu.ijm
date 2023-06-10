

print("\\Clear");

// Implements a local version of Otsu's global threshold clustering. The algorithm searches for the threshold that minimizes the intra-class variance, defined as a weighted sum of variances of the two classes. The local set is a circular ROI and the central pixel is tested against the Otsu threshold found for that region.
// r - radius of window around pixel, =15
// Parameter 1: ------
// Parameter 2: ------
out_dir = "C:/Users/x/gs/masterBio/code/corneal_endothelium/result/result_with_sda/otsu/";
for(r=8;r<=8;r+=4){
    id=""+r+"_0_0";
	path=out_dir+id+"/";
	string = path+" Otsu "+r+ " 0 0";
	runMacro("C:/Users/x/gs/masterBio/code/corneal_endothelium/macro/set/run_method.ijm", string);

	runMacro("C:/Users/x/gs/masterBio/code/corneal_endothelium/macro/set/run_bestfit.ijm", path);
	
	print("-------------------------------");

}


selectWindow("Log");
saveAs("Text", out_dir + "logs.txt");