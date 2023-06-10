

print("\\Clear");

// r - radius of window around pixel, =15
// Parameter 1: is the contrast threshold. The default value is 15. Any number different than 0 will change the default value.
// Parameter 2: ------

out_dir = "C:/Users/x/gs/masterBio/code/corneal_endothelium/result/result_with_sda/bernsen/";
for(r=5;r<=60;r+=4){
    for(par1=5;par1<=30;par1+=4){
        id=""+r+"_"+par1+"_0";
        path=out_dir+id+"/";
        string = path+" Bernsen "+r+ " "+par1+ " 0";
        runMacro("C:/Users/x/gs/masterBio/code/corneal_endothelium/macro/set/run_method.ijm", string);

        runMacro("C:/Users/x/gs/masterBio/code/corneal_endothelium/macro/set/run_bestfit.ijm", path);
	}
	print("-------------------------------");

}


selectWindow("Log");
saveAs("Text",out_dir + "logs.txt");