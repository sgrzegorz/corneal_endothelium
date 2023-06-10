close("*");

close("ROI Manager");
close("Results");

setBatchMode("hide");



function getName(i,name,directory){
	object = newArray(""+i+name,               // 1_image
	                  ""+i+name+".png",        // 1_image.png
	                  directory+i+name+".png", // dir/path/1_image.png
	                  directory,               // dir/path/
	                  directory+i+name         // dir/path/1_image
	                  );
	return object;
}





function openImg(path,name){
    open(path);
    rename(name);
}

function openBinImg(path,name){
	openImg(path,name);
	run("RGB Color");
    run("8-bit");
}


function saveImg(format, path){
	title = getTitle();
	run("Duplicate...", "title="+title);
	saveAs(format, path);
	close();
	selectWindow(title);

}


function processImage(i,path){
	src = getName(i,"",dir+"data/all/");
	met = getName(i,"_met",path);

    openImg(src[2],"SRC");

	openBinImg(met[2],"MET");

    run("Duplicate...", "title=MET_BESTFIT");
    run("BestFit IterativeThinning", "binary_or_segmentation=MET_BESTFIT grayscale_source=SRC task=BFI_Thinning_and_Dilation/BFI_Thinning_cycles number_of_dilations=2 max_number_of_cycles=10");


    saveImg("PNG",""+met[4]+".bestfit.png");

	openBinImg(""+src[3]+i+"_seg.bestfit.png","SEG_BESTFIT");

    run("Merge Channels...", "c1=SEG_BESTFIT c5=MET_BESTFIT keep");
    rename("SEG_BESTFIT_vs_MET_BESTFIT");
    saveImg("PNG",""+ met[4]+"_compare.png");
    run("Close All");
}


function processIfNotCached(i,path){
    met = getName(i,"_met",path);
    output_path = ""+met[4]+".bestfit.png";
	if(File.exists(output_path) == 0){
		processImage(i,path);
	}else{
		print("File " + output_path +" exists, bestfit skipping...");
	}
}


function runForAll(path){
	for(i=101;i<=130;i++){ // yg
		processIfNotCached(i,path);
	}
	
	for(i=201;i<=252;i++){ // bs
		processIfNotCached(i,path);
	}
	for(i=301;i<=307;i++){ // ygs
		processIfNotCached(i,path);
	}
//	for(i=401;i<=430;i++){ // ar
//		processImage(i,path);
//	}


}

// Example of usage:
// runMacro("C:/Users/x/gs/masterBio/code/corneal_endothelium/macro/set/run_bestfit.ijm", "C:/Users/x/gs/masterBio/code/corneal_endothelium/result/bernsen/2/");

dir = "C:/Users/x/gs/masterBio/code/corneal_endothelium/";

dirpath = getArgument();
print("[Parameter received: ", dirpath, "]"); // "C:/Users/x/gs/masterBio/code/corneal_endothelium/result/result_with_sda/bernsen/2"

runForAll(dirpath);







print("Finished");




