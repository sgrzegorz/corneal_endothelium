close("*");
print("\\Clear");

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
	print(title);
	run("Duplicate...", "title="+title);
	saveAs(format, path);
	close();
	selectWindow(title);

}



function process(i,src,met) {

    openImg(src[2],"SRC");
    
	openBinImg(met[2],"MET");

    run("Duplicate...", "title=MET_BESTFIT");
    run("BestFit IterativeThinning", "binary_or_segmentation=MET_BESTFIT grayscale_source=SRC task=BFI_Thinning_and_Dilation/BFI_Thinning_cycles number_of_dilations=2 max_number_of_cycles=10");

	
    saveImg("PNG",""+met[4]+".bestfit.png");

	openBinImg(""+src[3]+i+"_seg.bestfit.png","SEG_BESTFIT");

    run("Merge Channels...", "c1=SEG_BESTFIT c5=MET_BESTFIT keep");
    rename("SEG_BESTFIT_vs_MET_BESTFIT");
    saveImg("PNG",""+ met[4]+"_compare.png");
}



function processDataSet(i){
	src = getName(i,"",dir+"data/all/");
	met = getName(i,"_met",dir+"result/bernsen/2/");
	print(i);

    process(i,src, met);
}


function runForAll(){
	for(i=101;i<=130;i++){ // yg
		processDataSet(i);
	}
	
	for(i=201;i<=252;i++){ // bs
		processDataSet(i);
	}
	for(i=301;i<=307;i++){ // ygs
		processDataSet(i);
	}
	for(i=401;i<=430;i++){ // ar
		processDataSet(i);
	}

}

dir = "C:/Users/x/gs/masterBio/code/corneal_endothelium/";
runForAll();







print("Finished");




