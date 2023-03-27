open("C:/Users/x/gs/masterBio/srodblonek-rogowki/DATASET_SDA/YG_ready/1_s_max_SDAr6.png");
run("Auto Local Threshold", "method=Bernsen radius=15 parameter_1=0 parameter_2=0 white");
run("Invert LUT");
saveAs("PNG", "C:/Users/x/gs/masterBio/srodblonek-rogowki/DATASET_SDA/YG_ready/1_s_max_SDAr6_bernsen.png");