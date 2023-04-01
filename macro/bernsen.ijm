
dir = "C:/Users/x/gs/masterBio/dane/YG";
number_of_files = 5;

v = newArray("a","b");

for (i=1; i<number_of_files; i++){
	input_path = dir + "/" + i + "_s_max_SDAr6.png";
	open(input_path);
	run("Auto Local Threshold", "method=Bernsen radius=15 parameter_1=0 parameter_2=0 white");
	run("Invert LUT");
	output_path = dir + "/results/4/" + i + "_met.png";
	saveAs("PNG", output_path);
	run("Close All");
}




