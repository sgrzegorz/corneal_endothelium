bernsen.ijm

print("\\Clear");

// Implements Niblack's thresholding method:
// pixel = ( pixel >  mean + k * standard_deviation - c) ? object : background
// r - radius of window around pixel
// Parameter 1: is the k value. The default value is 0.2 for bright objects and -0.2 for dark objects. Any other number than 0 will change the default value.
// Parameter 2: is the C value. This is an offset with a default value of 0. Any other number than 0 will change its value. This parameter was added in version 1.3 and is not part of the original implementation of the algorithm. The original algorithm is applied when C = 0.

for(r=25;r<=70;r+=4){
    id=""+r+"_0_0";
	path="C:/Users/x/gs/masterBio/code/corneal_endothelium/result/niblack/"+id+"/";
	string = path+" Niblack "+r+ " 0 0";
	runMacro("C:/Users/x/gs/masterBio/code/corneal_endothelium/macro/set/run_method.ijm", string);

	runMacro("C:/Users/x/gs/masterBio/code/corneal_endothelium/macro/set/run_bestfit.ijm", path);
	
	print("-------------------------------");

}


selectWindow("Log");
saveAs("Text", "C:/Users/x/gs/masterBio/code/corneal_endothelium/result/niblack/logs.txt");