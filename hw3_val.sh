# Beware: only run this shell script under /hw3-mic folder

# run inference
python MIC/det/tools/test_net.py --config-file MIC/det/configs/da_faster_rcnn/e2e_da_faster_rcnn_R_50_FPN_masking_cs.yaml MODEL.WEIGHT MIC/det/model_final_teacher.pth &&

# convert output file to specific format
python format.py --bbox inference/my_cityscapes_test/bbox.json --id2name id2name_val.json --output output_val.json
