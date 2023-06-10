
print("\\Clear");

// Implements Niblack's thresholding method:
// pixel = ( pixel >  mean + k * standard_deviation - c) ? object : background
// r - radius of window around pixel, =15
// Parameter 1: is the k value. The default value is 0.2 for bright objects and -0.2 for dark objects. Any other number than 0 will change the default value.
// Parameter 2: is the C value. This is an offset with a default value of 0. Any other number than 0 will change its value. This parameter was added in version 1.3 and is not part of the original implementation of the algorithm. The original algorithm is applied when C = 0.
out_dir = "C:/Users/x/gs/masterBio/code/corneal_endothelium/result/result_with_sda/niblack/";
for(r=5;r<=60;r+=5){
    for(par1=0.1;par1<=0.4;par1+=0.05){
        for(par2=0;par2<=0.4;par2+=0.05){
            id=""+r+"_"+par1+"_"+par2;
            path=out_dir+id+"/";
            string = path+" Niblack "+r+ " " +par1 +" "+par2;
            runMacro("C:/Users/x/gs/masterBio/code/corneal_endothelium/macro/set/run_method.ijm", string);

            runMacro("C:/Users/x/gs/masterBio/code/corneal_endothelium/macro/set/run_bestfit.ijm", path);

            print("-------------------------------");
        }
    }
}


selectWindow("Log");
saveAs("Text", out_dir + "logs.txt");