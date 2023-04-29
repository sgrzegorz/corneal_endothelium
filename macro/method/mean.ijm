

print("\\Clear");
// Metoda Mean używa progu thresold jako lokalnej wartości skali szarości. Wariacja tej metody używa mean-C, gdzie C to stała
// pixel = ( pixel > mean - c ) ? object : background
// r - radius of window around pixel, =15
// Parameter 1: is the C value. The default value is 0. Any other number will change the default value.
// Parameter 2: ------

for(r=5;r<=60;r+=4){
    for(par1=0;par1<=30;par1+=4){
        id=""+r+"_"+par1 +"_0";
        path="C:/Users/x/gs/masterBio/code/corneal_endothelium/result/mean/"+id+"/";
        string = path+" Mean "+r+ " "+par1+ " 0";
        runMacro("C:/Users/x/gs/masterBio/code/corneal_endothelium/macro/set/run_method.ijm", string);

        runMacro("C:/Users/x/gs/masterBio/code/corneal_endothelium/macro/set/run_bestfit.ijm", path);

        print("-------------------------------");
    }
}


selectWindow("Log");
saveAs("Text", "C:/Users/x/gs/masterBio/code/corneal_endothelium/result/mean/logs.txt");