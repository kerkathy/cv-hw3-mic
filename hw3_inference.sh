# Beware: only run this shell script under /hw3-mic folder

# run inference
python MIC/det/tools/test_net.py --config-file MIC/det/configs/da_faster_rcnn/my_test.yaml MODEL.WEIGHT MIC/det/model_final_teacher.pth &&

# convert output file to specific format
python format.py --bbox inference/my_cityscapes_test_no_label/bbox.json --id2name id2name_test.json --output output_test.json
