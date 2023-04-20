close("*");
print("\\Clear");

close("ROI Manager");
close("Results");



function getName(i,name,directory){
	object = newArray(""+i+name,               // 1_image
	                  ""+i+name+".png",        // 1_image.png
	                  directory+i+name+".png", // dir/path/1_image.png
	                  directory,               // dir/path/
	                  directory+i+name         // dir/path/1_image
	                  );
	return object;
}





function openAs(path,name){
    open(path);
    rename(name);
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
	Array.print(src);
	Array.print(met);
    openAs(src[2],"SRC");
    print(getTitle());


	openAs(met[2],"MET");
	run("RGB Color");
    run("8-bit");

    run("Duplicate...", "title=MET_BESTFIT");
    run("BestFit IterativeThinning", "binary_or_segmentation=MET_BESTFIT grayscale_source=SRC task=BFI_Thinning_and_Dilation/BFI_Thinning_cycles number_of_dilations=2 max_number_of_cycles=10");

    print(""+met[4]+".bestfit.png");
    saveImg("PNG",""+met[4]+".bestfit.png");
//	save(""+met[4]+".bestfit.png");
//
	

    run("Merge Channels...", "c1=MET c5=MET_BESTFIT keep");
    saveImg("PNG",""+ met[4]+"_compare.png");
//	save(met[4]+"_compare.png");


}


dir = "C:/Users/x/gs/masterBio/code/corneal_endothelium/"


//setBatchMode("hide");

for(i=101;i<=101;i++){ // yg

	src = getName(i,"",dir+"data/all/");
	met = getName(i,"_met",dir+"result/bernsen/2/");
	print(i);

    process(i,src, met);
}







print("Finished");




