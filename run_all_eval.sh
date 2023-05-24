# This script will run all models in <model_path> on [target evaluation set](../hw3/data/hw3_dataset/fog/public_test) and save results to results/
# Figures of mAP vs. # of iterations will be saved to current working directory
# Adjuct the model number in the for loop according to your needs before running this script
# /results 
# [Usage] run this shell script under /hw3-mic folder
# 	bash run_all_eval.sh <model_path>

# check arguments
if [ "$#" -ne 1 ]; then
	echo "Usage: bash run_all_eval.sh <path/to/model/folder>"
	exit 1
fi

# check if results folder already exists
if [ -d "results" ]; then
	echo "results folder already exists, please remove it before running this script"
	exit 1
fi
mkdir results && echo "results folder created"

# modify the for loop in format of for i in $(seq <start> <step> <end>)
for i in $(seq 6000 6000 60001)
do
	if [ $i -lt 10000 ]; then
		model="model_000${i}.pth"
	else
		model="model_00${i}.pth"
	fi
	echo "Evaluating model $model"
	mkdir results/$i && echo "results/$i folder created"
	if [ ! -f "$1/$model" ]; then
		echo "Model $1/$model not found"
		exit 1
	fi
	python MIC/det/tools/test_net.py --config-file MIC/det/configs/da_faster_rcnn/e2e_da_faster_rcnn_R_50_FPN_masking_cs.yaml MODEL.WEIGHT $1/$model OUTPUT_DIR results/$i
	echo "Results saved at results/$i"
done

python ./draw_map.py --model_path results
