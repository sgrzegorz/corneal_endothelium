

print("\\Clear");
// Metoda Mean używa progu thresold jako lokalnej wartości skali szarości. Wariacja tej metody używa mean-C, gdzie C to stała
// pixel = ( pixel > mean - c ) ? object : background
// r - radius of window around pixel
// Parameter 1: is the C value. The default value is 0. Any other number will change the default value.
// Parameter 2: ------

for(r=25;r<=70;r+=4){
    id=""+r+"_0_0";
	path="C:/Users/x/gs/masterBio/code/corneal_endothelium/result/mean/"+id+"/";
	string = path+" Mean "+r+ " 0 0";
	runMacro("C:/Users/x/gs/masterBio/code/corneal_endothelium/macro/set/run_method.ijm", string);

	runMacro("C:/Users/x/gs/masterBio/code/corneal_endothelium/macro/set/run_bestfit.ijm", path);
	
	print("-------------------------------");

}


selectWindow("Log");
saveAs("Text", "C:/Users/x/gs/masterBio/code/corneal_endothelium/result/mean/logs.txt");