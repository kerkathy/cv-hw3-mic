python id2name_from_coco.py --coco ../hw3/data/hw3_dataset/fog/val.coco.json --output id2name_val.json
python create_test_json.py --dataset ../hw3/data/hw3_dataset --subdir fog/public_test --output_json test.json --output_id2name id2name_test.json
python create_test_json.py --dataset ../hw3/data/hw3_dataset --subdir fog/train --output_json train_fog.json --output_id2name id2name_train_fog.json --path_subdir
