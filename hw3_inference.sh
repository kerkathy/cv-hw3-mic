# Beware: only run this shell script under /hw3-mic folder
# models model_{0,1,2,3,final}.pth should already be put in checkpoint/
# Usage: bash hw3_inference.sh $1 $2 $3
# $1: test dataset dir (without subdir)
# $2: path to output file
# $3: int [0,3], indicating checkpoint to use (0%, 33%, 66%, 100%)

# check arguments
if [ "$#" -ne 3 ]; then
    echo "Usage: bash hw3_inference.sh \$1 \$2 \$3"
    echo "\$1: test dataset dir (!!without subdir!!)"
    echo "\$2: path to output file"
    echo "\$3: int [0,3], indicating checkpoint to use (0%, 33%, 66%, 100%)"
    exit 1
fi

# decide checkpoint to use
if [ $3 -eq 0 ]; then
    echo "Using 0% checkpoint"
    model=checkpoint/model_0.pth
elif [ $3 -eq 1 ]; then
    echo "Using 33% checkpoint"
    model=checkpoint/model_1.pth
elif [ $3 -eq 2 ]; then
    echo "Using 66% checkpoint"
    model=checkpoint/model_2.pth
elif [ $3 -eq 3 ]; then
    echo "Using 100% checkpoint"
    model=checkpoint/model_3.pth
elif [ $4 -eq 4 ]; then
    echo "Using 100% checkpoint"
    model=checkpoint/model_final.pth
else
    echo "Invalid checkpoint"
    exit 1
fi

# create dummy test.json and id2name_test.json
# python create_test_json.py --dataset $1 --subdir fog/public_test --output_json test.json --output_id2name id2name_test.json &&
echo "Running create_test_json_for_all_subdir.py ..." &&
python create_test_json_for_all_subdir.py --dataset $1 --output_json test.json --output_id2name id2name_test.json &&

# run inference using above specified checkpoint, output to inference/my_cityscapes_test_no_label/bbox.json
# continue only if this line succeeds
echo "Running test_net.py ..." &&
python MIC/det/tools/test_net.py --config-file MIC/det/configs/da_faster_rcnn/my_test.yaml MODEL.WEIGHT $model &&

# convert output file to specific format
echo "Running format.py ..." &&
python format.py --bbox inference/my_cityscapes_test_no_label/bbox.json --id2name id2name_test.json --output $2