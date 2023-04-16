close("*");
print("\\Clear");

setBatchMode("hide");


dir = "C:/Users/x/gs/masterBio/code/corneal_endothelium/data/default/";
dir_out = dir;

open(dir+"yg9_src.png");
rename("SRC");

open(dir+"yg9_khbin.png");
rename("BIN");
run("RGB Color");
run("8-bit");
run("BestFit IterativeThinning", "binary_or_segmentation=BIN grayscale_source=SRC task=BestFit_Iterative_Thinning_only number_of_dilations=2 max_number_of_cycles=10");
saveAs("PNG", dir_out+name+".bestfit.png");



open(dir+"yg9_seg.png");
rename("MANUAL");
run("RGB Color");
run("8-bit");
run("BestFit IterativeThinning", "binary_or_segmentation=MANUAL grayscale_source=SRC task=BFI_Thinning_and_Dilation/BFI_Thinning_cycles number_of_dilations=2 max_number_of_cycles=10");
saveAs("PNG", dir_out+name+".bestfit.png");






