

print("\\Clear");

// Metoda oparta na prostym przełączniku kontrastu. Ustawia wartość piksela na biały (255) lub czarny (0) w zależności od tego,
// czy jego bieżąca wartość jest najbliższa odpowiednio lokalnemu maksimum czy minimum.
// Procedura jest skrajnym przypadkiem "Toggle Contrast Enhancement"

// r - radius of window around pixel, =15
// Parameter 1: ------
// Parameter 2: ------
out_dir = "C:/Users/x/gs/masterBio/code/corneal_endothelium/result/result_with_sda/contrast/";
for(r=29;r<=70;r+=4){
    id=""+r+"_0_0";
	path=out_dir+id+"/";
	string = path+" Contrast "+r+ " 0 0";
	runMacro("C:/Users/x/gs/masterBio/code/corneal_endothelium/macro/set/run_method.ijm", string);

	runMacro("C:/Users/x/gs/masterBio/code/corneal_endothelium/macro/set/run_bestfit.ijm", path);

	print("-------------------------------");
}


selectWindow("Log");
saveAs("Text", out_dir + "/logs.txt");