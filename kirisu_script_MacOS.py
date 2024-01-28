import glob
from kirisu_util import convertFile
# Imports the library of tools needed for the code to work

def main(in_dir, out_dir):
    max_lambda = 700
    min_lambda = 400
    max_time = 1000
    min_time = 0
# Change the values of the max and min time and wavelength

 
    print glob.glob(in_dir + "/*.glb")
    for in_name in glob.glob(in_dir + "/*.glb"):
        print(in_name)
        print(in_name.split("/"))
        out_name = out_dir + "/%s.glb_t" % in_name.split("/")[-1][:-4]
        convertFile(min_lambda, max_lambda, min_time, max_time, True, in_name, out_name)
        print("Done. %s was successfully created" % out_name.split('/')[-1])



in_dir = "XXX/glb"
out_dir = "XXX/glb_t"
# Change XXX by the directory containing the glb folder with the unprocessed data and a new folder glb_t

main(in_dir, out_dir)
