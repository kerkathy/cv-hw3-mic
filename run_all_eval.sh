# run python for all models
for i in $(seq 10000 5000 20000)
do
	model="model_00${i}.pth"
	echo "Evaluating model $model"
	python MIC/det/tools/test_net.py --config-file MIC/det/configs/da_faster_rcnn/e2e_da_faster_rcnn_R_50_FPN_masking_cs.yaml MODEL.WEIGHT MIC/det/models/models_0520/$model > log/log_$i.txt
	cp inference/my_cityscapes_test/coco_results.pth results/$i.pth
	echo "Results saved at results/${i}.pth"
done
