

print("\\Clear");
// This is a modification of Sauvola's thresholding method to deal with low contrast images.
// In this method, the threshold t is computed as:   t = mean * (1 + p * exp(-q * mean) + k * ((stdev / r) - 1))
// radius  - radius of window around pixel, =15
// Parameter 1: is the k value. The default value is 0.25. Any other number than 0 will change its value.
// Parameter 2: is the r value. The default value is 0.5. This value is different from Sauvola's because it uses the normalised intensity of the image. Any other number than 0 will change its value.
out_dir = "C:/Users/x/gs/masterBio/code/corneal_endothelium/result/result_with_sda/phansalkar/";
for(r=5;r<=60;r+=5){
    for(par1=0.1;par1<=0.4;par1+=0.05){
        for(par2=0.2;par2<=1;par2+=0.1){
            id=""+r+"_"+par1+"_"+par2;
            path=out_dir+id+"/";
            string = path+" Phansalkar "+r+" "+par1+" "+par2;
            runMacro("C:/Users/x/gs/masterBio/code/corneal_endothelium/macro/set/run_method.ijm", string);

            runMacro("C:/Users/x/gs/masterBio/code/corneal_endothelium/macro/set/run_bestfit.ijm", path);

            print("-------------------------------");
        }
    }
}


selectWindow("Log");
saveAs("Text", out_dir + "logs.txt");