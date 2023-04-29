

print("\\Clear");
// This is a modification of Sauvola's thresholding method to deal with low contrast images.
// In this method, the threshold t is computed as:   t = mean * (1 + p * exp(-q * mean) + k * ((stdev / r) - 1))
// radius  - radius of window around pixel
// Parameter 1: is the k value. The default value is 0.25. Any other number than 0 will change its value.
// Parameter 2: is the r value. The default value is 0.5. This value is different from Sauvola's because it uses the normalised intensity of the image. Any other number than 0 will change its value.

for(r=25;r<=70;r+=4){
    id=""+r+"_0_0";
	path="C:/Users/x/gs/masterBio/code/corneal_endothelium/result/phansalkar/"+id+"/";
	string = path+" Phansalkar "+r+ " 0 0";
	runMacro("C:/Users/x/gs/masterBio/code/corneal_endothelium/macro/set/run_method.ijm", string);

	runMacro("C:/Users/x/gs/masterBio/code/corneal_endothelium/macro/set/run_bestfit.ijm", path);
	
	print("-------------------------------");

}


selectWindow("Log");
saveAs("Text", "C:/Users/x/gs/masterBio/code/corneal_endothelium/result/phansalkar/logs.txt");