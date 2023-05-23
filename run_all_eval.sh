# This script will run all models in <model_path> and save results to results/
# Figures of mAP vs. # of iterations will be saved to current working directory
# Adjuct the model number in the for loop according to your needs before running this script
# [Usage] run this shell script under /hw3-mic folder
# 	bash run_all_eval.sh <model_path>

# check arguments
if [ "$#" -ne 1 ]; then
	echo "Usage: bash run_all_eval.sh <path/to/model/folder>"
	exit 1
fi

# modify the for loop in format of for i in $(seq <start> <step> <end>)
for i in $(seq 10000 5000 30000)
do
	model="model_00${i}.pth"
	echo "Evaluating model $model"
	mkdir results/$i
	python MIC/det/tools/test_net.py --config-file MIC/det/configs/da_faster_rcnn/e2e_da_faster_rcnn_R_50_FPN_masking_cs.yaml MODEL.WEIGHT $1/$model OUTPUT_DIR results/$i
	echo "Results saved at results/$i"
done

python ./draw_map.py --model_path results