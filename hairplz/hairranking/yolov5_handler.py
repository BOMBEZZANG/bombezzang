import subprocess

def run_yolov5_detection():
    yolov5_detect_script = "/Users/jongminkim/Desktop/project/hariranking/hairranking/hairranking/yolov5/detect.py"
    source_path = "/Users/jongminkim/Desktop/project/hariranking/hairranking/hairranking/yolov5/data/images"
    weights_path = "/Users/jongminkim/Desktop/project/hariranking/hairranking/hairranking/yolov5/runs/train/hair_experiment3/weights/best.pt"
    conf = 0.6

    command = f"python {yolov5_detect_script} --source {source_path} --weights {weights_path} --conf {conf} --save-crop"
    subprocess.run(command, shell=True, check=True)


