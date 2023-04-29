

print("\\Clear");

// Implements Sauvola's thresholding method, which is a variation of Niblack's method
// pixel = ( pixel > mean * ( 1 + k * ( standard_deviation / r - 1 ) ) ) ? object : background
// radius  - radius of window around pixel, =15
// Parameter 1: is the k value. The default value is 0.5. Any other number than 0 will change the default value.
// Parameter 2: is the r value. The default value is 128. Any other number than 0 will change the default value

for(r=5;r<=60;r+=5){
    for(par1=0.1;par1<=1;par1+=0.1){
        for(par2=50;par2<=200;par2+=20){
            id=""+r+"_"+par1+"_"+par2;
            path="C:/Users/x/gs/masterBio/code/corneal_endothelium/result/sauvola/"+id+"/";
            string = path+" Sauvola "+r+ " "+par1+" "+par2;
            runMacro("C:/Users/x/gs/masterBio/code/corneal_endothelium/macro/set/run_method.ijm", string);

            runMacro("C:/Users/x/gs/masterBio/code/corneal_endothelium/macro/set/run_bestfit.ijm", path);

            print("-------------------------------");
        }
    }
}


selectWindow("Log");
saveAs("Text", "C:/Users/x/gs/masterBio/code/corneal_endothelium/result/sauvola/logs.txt");