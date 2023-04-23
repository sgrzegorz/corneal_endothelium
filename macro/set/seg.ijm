close("*");
print("\\Clear");

setBatchMode("hide");

dir = "C:/Users/x/gs/masterBio/code/corneal_endothelium/"
dir_src = dir+"data/all/";
dir_seg = dir+"result/seg/";


function getName(i,name,directory){
	object = newArray(""+i+name, ""+i+name+".png",directory+i+name+".png");
	return object;
}

function process(i,src,seg) {
	Array.print(src);
	Array.print(seg);
    open(src[2]);
    rename("SRC");

    open(seg[2]);
    run("RGB Color");
    run("8-bit");
    rename("SEG");

    run("Duplicate...", "title=SEG_BESTFIT");
    run("BestFit IterativeThinning", "binary_or_segmentation=SEG_BESTFIT grayscale_source=SRC task=BFI_Thinning_and_Dilation/BFI_Thinning_cycles number_of_dilations=2 max_number_of_cycles=10");
    saveAs("PNG", dir_seg+seg[0]+".bestfit.png");
    rename("SEG_BESTFIT");

    run("Merge Channels...", "c1=SEG c5=SEG_BESTFIT keep");
    saveAs("PNG", dir_seg+seg[0]+"_compare.png");

	run("Close All");    
}


function processDataSet(i){
	src = getName(i,"",dir_src);
	seg = getName(i,"_seg",dir_src);
	print(i);

    process(i,src,seg);

}


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







print("Finished");




