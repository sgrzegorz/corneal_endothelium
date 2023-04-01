
dir = "C:/Users/x/gs/masterBio/code/corneal_endothelium/data/yg";
number_of_files = 30;

v = newArray("a","b");

function niblack(){
    run("Auto Local Threshold", "method=Niblack radius=15 parameter_1=0 parameter_2=0 white");
}

function bernsen(){
	run("Auto Local Threshold", "method=Bernsen radius=15 parameter_1=0 parameter_2=0 white");
}

for (i=1; i<=number_of_files; i++){
	input_path = dir + "/" + i + "_SDAr6.png";
	open(input_path);
	niblack();
	run("Invert LUT");
	output_path = dir + "/" + i + "_met.png";
	saveAs("PNG", output_path);
	run("Close All");
}




