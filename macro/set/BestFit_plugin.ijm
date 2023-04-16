close("*");
print("\\Clear");

// #################################################
// ##                                             ##
// ##  https://home.agh.edu.pl/~pioro/bestfit     ##
// ##                                             ##
// ##  BestFit                                    ##
// ##  Flood-based Iterative Thinning             ##
// ##  2023.03.24, Adam Piorkowski                ##
// ##  pioro@agh.edu.pl                           ##
// ##                                             ##
// #################################################
// cite:
// Piorkowski A.: Best-fit Segmentation Created Using Flood-based Iterative Thinning. Springer, AISC Vol. 525, pp 61-68, 2017
// 
// NOTE: the output segmentation may be slightly different than that achieved by BestFit.exe 
// because of different masks and different sequences used in these implementations

// NOTE:2 Do not change window/image selection during processing (it can be a cause of errors)
// to avoid miss-selection of processed window and to speed up - use:
 setBatchMode("hide");		
// and save the images at the end, e.g.:
// saveAs("PNG", "output_bestfit.png");




// #################################################
// ##                                             ##
// ##  HOW TO USE - EXAMPLES                      ##
// ##                                             ##
// #################################################


// images - from bestfit www site
dir = "C:/Users/x/gs/masterBio/code/corneal_endothelium/data/default/";

open(dir+"yg9_src.png");
rename("SRC");

open(dir+"yg9_khbin.png");
rename("BIN");
Check8bit0255BinaryFile();


open(dir+"yg9_seg.png");
rename("MANUAL");
Check8bit0255BinaryFile();


// ##################################################
// ##                                              ##
// ##  EXAMPLE #1 - Flood-based Iterative Thinning ##
// ##                                              ##
// ##################################################




run("BestFit IterativeThinning", "grayscale=SRC segmentation=BIN");


selectWindow("BIN");
rename("yg9_khbin_floodbaseditth.png");

saveAs("PNG", dir+"output_binary_bestfit.png");


selectWindow("MANUAL");

run("Duplicate...", "title=MANUAL_BESTFIT");

BestFit_DilatateThinning_cycles_opt_plugin("SRC", "MANUAL_BESTFIT", 2);



saveAs("PNG", dir+"output_manual_bestfit.png");




// ##############################################################################################################################################


// #################################################
// ##                                             ##
// ##  BESTFIT SOURCE FUNCTIONS - DO NOT MODIFY   ##
// ##                                             ##
// #################################################

var BestFit_print_comments = 1;		// 0 - to silent mode - disable log output


// dilatation_count - number of dilatations - 1 - may be not enough, but is safe; try 2; higher - can fill holes (cells)

function BestFit_DilatateThinning_cycles_opt_plugin(source_image_name, segmentation_name, dilatation_count)
{
	for(it = 0; it < 10; it++)
	{
		selectWindow(segmentation_name);
		run("Duplicate...", "title=" + segmentation_name +"_previous");
		selectWindow(segmentation_name);
		
		for(l=0;l<dilatation_count; l++)
			run("Options...", "iterations=1 count=1 black do=Dilate");

		//BestFit_FloodBasedIterativeThinning(source_image_name, segmentation_name);	
		run("BestFit IterativeThinning", "segmentation="+segmentation_name+" grayscale="+source_image_name+"");
			
		// checking if there were changes 
		imageCalculator("Difference create", segmentation_name, segmentation_name +"_previous");
		selectWindow("Result of " + segmentation_name);
		getHistogram(values, counts, 256);
		
		close("Result of " + segmentation_name);
		close(segmentation_name +"_previous");

		selectWindow(segmentation_name);
		
		if(BestFit_print_comments > 0)		
				print("BESTFIT CYCLE #" +it + "   PIX CHANGES: "+  (getWidth() * getHeight() - counts[0]) );
		
		if(counts[0] == getWidth() * getHeight() )	// no changes
			break;		
	}
}


function Check8bit0255BinaryFile()
{
	if(bitDepth() != 8)
		run("8-bit");

	getHistogram(values, counts, 256);

	// removing 1bit palette 0/1
	if( counts[0] + counts[255] != getWidth() * getHeight() )
	{
		run("RGB Color");
		run("8-bit");
	}

	getHistogram(values, counts, 256);

	// not enough? hard rewrite
	if(counts[0] + counts[255] != getWidth() * getHeight() )
		for (i_ = 0; i_ < getWidth(); i_++) 
			for(j_ = 0; j_ < getHeight(); j_++)
				if(getPixel(i_, j_) > 0)
					setPixel(i_, j_, 255);	
}

