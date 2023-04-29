

print("\\Clear");

// r - radius of window around pixel
// Parameter 1: is the contrast threshold. The default value is 15. Any number different than 0 will change the default value.
// Parameter 2: ------

for(r=25;r<=70;r+=4){
    id=""+r+"_0_0";
	path="C:/Users/x/gs/masterBio/code/corneal_endothelium/result/bernsen/"+id+"/";
	string = path+" Bernsen "+r+ " 0 0";
	runMacro("C:/Users/x/gs/masterBio/code/corneal_endothelium/macro/set/run_method.ijm", string);

	runMacro("C:/Users/x/gs/masterBio/code/corneal_endothelium/macro/set/run_bestfit.ijm", path);
	
	print("-------------------------------");

}


selectWindow("Log");
saveAs("Text", "C:/Users/x/gs/masterBio/code/corneal_endothelium/result/bernsen/logs.txt");