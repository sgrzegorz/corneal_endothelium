setBatchMode("hide");


function processDataSet(i,string){
	all_path = "C:/Users/x/gs/masterBio/code/corneal_endothelium/data/all/";
	input_path = all_path + i + "_SDAr6.png";
	open(input_path);
	run("Auto Local Threshold", string);
	run("Invert LUT");
	output_path = path + i + "_met.png";
	saveAs("PNG", output_path);
	run("Close All");
}


function runForAll(){
	string = "method=" +method+" radius="+radius +" parameter_1="+parameter_1+" parameter_2="+parameter_2+ " white";
	print(string);
	
	for(i=101;i<=130;i++){ // yg
		processDataSet(i,string);
	}

	for(i=201;i<=252;i++){ // bs
		processDataSet(i,string);
	}
	for(i=301;i<=307;i++){ // ygs
		processDataSet(i,string);
	}
	for(i=401;i<=430;i++){ // ar
		processDataSet(i,string);
	}

}

function getVal(value){
	n = parseFloat(value);
	if (isNaN(n))
	   exit("'" + a[i] + "' is not a number");
	return n
}

// Example of usage:
// string = "C:/Users/x/gs/masterBio/code/corneal_endothelium/result/otsu/1/ Otsu 15 0 0"
// runMacro("C:/Users/x/gs/masterBio/code/corneal_endothelium/macro/set/run_method.ijm", string);

values = getArgument()
if (lengthOf(values)==0)
  return 0;
arguments = split(values, "");
path = arguments[0];
method = arguments[1];
radius = getVal(arguments[2]);
parameter_1 = getVal(arguments[3]);
parameter_2 = getVal(arguments[4]);

print(path);
File.makeDirectory(path);
runForAll();