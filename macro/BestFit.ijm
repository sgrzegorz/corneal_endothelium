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


// Uses/requires: 
// Morphology (Gabriel Landini)
// https://sites.imagej.net/Landini/
// to install you can use Imagej/Fiji:   Help->Update...


// #################################################
// ##                                             ##
// ##  HO TO USE - EXAMPLES                       ##
// ##                                             ##
// #################################################

// to avoid miss-selection of processed window and to speed up:
 setBatchMode("hide");		// and save the images at the end.

// images - from bestfit www site
//
//open("yg9_src.png");
//rename("SRC");
//
//open("yg9_khbin.png");
//rename("BIN");
//Check8bit0255BinaryFile();
//
//open("yg9_seg.png");
//rename("MANUAL");
//Check8bit0255BinaryFile();


// your image selections - uncommment to use :

open( File.openDialog("SOURCE_IMAGE") );
rename("SRC");

open( File.openDialog("BINARY_IMAGE") );
rename("BIN");
Check8bit0255BinaryFile();

open( File.openDialog("MANUAL_SEGMENTATION") );
rename("MANUAL");
Check8bit0255BinaryFile();


// ##################################################
// ##                                              ##
// ##  EXAMPLE #1 - Flood-based Iterative Thinning ##
// ##                                              ##
// ##################################################
 BestFit_FloodBasedIterativeThinning("SRC", "BIN");

rename("yg9_khbin_floodbaseditth.png");


// ##################################################
// ##                                              ##
// ##  EXAMPLE #2 - Best-Fit adaptation            ##
// ##                                              ##
// ##################################################
 selectWindow("MANUAL");

run("Duplicate...", "title=MANUAL_BESTFIT");
 BestFit_DilatateThinning_cycles_opt("SRC", "MANUAL_BESTFIT", 2);



// #####################
// comparison of outputs
// #####################
path = "C:/Users/x/gs/masterBio/dane/YG/results/bernesen_yg_1/";
// differences of two methods of segmentation
run("Merge Channels...", "c1=yg9_khbin_floodbaseditth.png c5=MANUAL keep");
rename("MANUAL_C_vs_KH_bestfit_R");
save(path+"MANUAL_C_vs_KH_bestfit_R.png");
 // changes of iterative thinning for manual segmentation
run("Merge Channels...", "c1=MANUAL_BESTFIT c5=MANUAL keep");
rename("MANUAL_C_AFTER_BESTFIT_R");
save(path+"MANUAL_C_AFTER_BESTFIT_R.png");
 // overlay of two different method after BestFit (the aim of BestFit)
run("Merge Channels...", "c1=MANUAL_BESTFIT c5=yg9_khbin_floodbaseditth.png keep");
rename("Overlay_of_KH_Bestfit_C_and_Manual_Bestfit_R");
save(path+"Overlay_of_KH_Bestfit_C_and_Manual_Bestfit_R.png");

// ##############################################################################################################################################

// #################################################
// ##                                             ##
// ##  BESTFIT SOURCE FUNCTIONS - DO NOT MODIFY   ##
// ##                                             ##
// #################################################


var BestFit_print_comments = 1;		// 0 - to silent mode - disable log output


// dilatation_count - number of dilatations - 1 - may be not enough, but is safe; try 2; higher - can fill holes (cells)

function BestFit_DilatateThinning_cycles(source_image_name, segmentation_name, dilatation_count)
{
	for(it = 0; it < 10; it++)
	{
		selectWindow(segmentation_name);
		for(l=0;l<dilatation_count; l++)
			run("Options...", "iterations=1 count=1 black do=Dilate");
		BestFit_FloodBasedIterativeThinning(source_image_name, segmentation_name);	
	}
}


// dilatation_count - number of dilatations - 1 - may be not enough, but is safe; try 2; higher - can fill holes (cells)

function BestFit_DilatateThinning_cycles_opt(source_image_name, segmentation_name, dilatation_count)
{
	for(it = 0; it < 10; it++)
	{
		selectWindow(segmentation_name);
		run("Duplicate...", "title=" + segmentation_name +"_previous");
		selectWindow(segmentation_name);
		
		for(l=0;l<dilatation_count; l++)
			run("Options...", "iterations=1 count=1 black do=Dilate");

		BestFit_FloodBasedIterativeThinning(source_image_name, segmentation_name);	
		
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


function BestFit_FloodBasedIterativeThinning(source_image_name, binary_image_name)
{
	selectWindow(source_image_name);
	
	w = getWidth();
	h = getHeight();

	BestFit_source_image = newArray(w*h);
	BestFit_tmp_image = newArray(w*h);
	src_histogram = newArray(256);

	for(ii=0;ii<w;ii++)
		for(jj=0;jj<h;jj++)
		{
			src_val = getPixel(ii, jj);
			BestFit_source_image[ii+jj*w] = src_val;
			src_histogram[src_val]++;
		}
			
	selectWindow(binary_image_name);
	
	if(w != getWidth() || 	h != getHeight())
		return;
		
	Check8bit0255BinaryFile();

	// to detect no changes in loop (and break)
	Bestfit_pix_count = 0;
	Bestfit_pix_count_prev = 0;
	
	for(level = 255; level >=0; level--)
	{
		// time optimization for empty loops
		if(src_histogram[level] == 0)
			continue;
			
		MAX_NUMBER_OF_MORPH_ITERATIONS = 50;	//	should be enough for corneal endothelium images
	
		
		for(N=0;N<MAX_NUMBER_OF_MORPH_ITERATIONS;N++)
		{
			for(k=0;k<BestFit_kernels_thinning.length;k++)
			{	
					BestFit_store(BestFit_tmp_image, w, h);
					run("BinaryThin ", "kernel_a=" + BestFit_kernels_thinning[k] + " rotations=none iterations=1 white");
					BestFit_recover_lower_points(BestFit_tmp_image, BestFit_source_image, w, h, level);
			}
			
			for(k=0;k<BestFit_kernels_branches.length;k++)
			{	
					BestFit_store(BestFit_tmp_image, w, h);
					run("BinaryThin ", "kernel_a=" + BestFit_kernels_branches[k] + " rotations=none iterations=1 white");
					BestFit_recover_lower_points(BestFit_tmp_image, BestFit_source_image, w, h, level);
			}
			
			for(k=0;k<BestFit_kernels_smooth.length;k++)
			{	
				BestFit_store(BestFit_tmp_image, w, h);
				run("BinaryThin ", "kernel_a=" + BestFit_kernels_smooth[k] + " rotations=none iterations=1 white");
				BestFit_recover_lower_points(BestFit_tmp_image, BestFit_source_image, w, h, level);
			}
		
			getHistogram(values, counts, 256);
			Bestfit_pix_count = counts[255];
			
			if(Bestfit_pix_count == Bestfit_pix_count_prev)
				break;	// no changes
			
			if(BestFit_print_comments > 0)		
				print("Level: " + level + " (" + src_histogram[level] + " pix)  iteration: " + N + "  changes: " + (Bestfit_pix_count_prev - Bestfit_pix_count));
			
			Bestfit_pix_count_prev = Bestfit_pix_count;		
		}
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


function BestFit_store(imgtab, BestFit_w, BestFit_h)
{
	for(_i=0;_i<BestFit_w;_i++)
		for(_j=0;_j<BestFit_h;_j++)
			imgtab[_i+_j*BestFit_w] = getPixel(_i, _j);
}

function BestFit_recover_lower_points(img_tab, srcimgtab, BestFit_w, BestFit_h, BestFit_flood_level)
{
	for(_i=0;_i<BestFit_w;_i++)
		for(_j=0;_j<BestFit_h;_j++)
			if( img_tab[_i+_j*BestFit_w] != 0 && getPixel(_i, _j) == 0 && srcimgtab[_i+_j*BestFit_w] < BestFit_flood_level)
				setPixel(_i, _j, 255);
}

var BestFit_kernels_thinning = newArray(
"[2 1 1 0 1 1 0 0 2]",
"[0 2 1 0 1 1 0 2 1]",
"[0 0 2 0 1 1 2 1 1]",
"[0 0 0 2 1 2 1 1 1]",
"[2 0 0 1 1 0 1 1 2]",	
"[1 2 0 1 1 0 1 2 0]",
"[1 1 2 1 1 0 2 0 0]",
"[1 1 1 2 1 2 0 0 0]"
);


var BestFit_kernels_smooth = newArray(
"[2 1 2 2 1 2 0 0 0]",
//"[2 2 1 0 1 2 0 0 2]",
"[0 2 2 0 1 1 0 2 2]",
//"[0 0 2 0 1 2 2 2 1]",
"[0 0 0 2 1 2 2 1 2]",	
//"[2 0 0 2 1 0 1 2 2]",
"[2 2 0 1 1 0 2 2 0]"
//"[1 2 2 2 1 0 1 2 2]"
);


var BestFit_kernels_branches = newArray(
"[0 0 0 0 1 0 0 2 2]",
"[0 0 0 0 1 2 0 0 2]",
"[0 0 2 0 1 2 0 0 0]",
"[0 2 2 0 1 0 0 0 0]",
"[2 2 0 0 1 0 0 0 0]",
"[2 0 0 2 1 0 0 0 0]",
"[0 0 0 2 1 0 2 0 0]",
"[0 0 0 0 1 0 2 2 0]"
);

