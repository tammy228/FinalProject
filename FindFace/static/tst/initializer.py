import sys
sys.path.insert(0, './packages')
from preprocess import preprocesses
import time

start_time = time.time()

if (len(sys.argv) < 2):
	print("Forgot directory name argument. Please try again.")
	sys.exit()

input_datadir = sys.argv[1]
output_datadir = "Output_dlib" + "_" + sys.argv[1]

if not os.path.exists(OUTPUT_DIR):
	os.mkdir(OUTPUT_DIR)

obj=preprocesses(input_datadir,output_datadir)
nrof_images_total,nrof_successfully_aligned=obj.collect_data()

print('Total number of images: %d' % nrof_images_total)
print('Number of successfully aligned images: %d' % nrof_successfully_aligned)
print("{} takes --- {} seconds to --- find faces".format( sys.argv[0], (time.time() - start_time) ) )


