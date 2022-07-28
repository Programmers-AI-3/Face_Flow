<div align="center">
<p>
   <a align="left" href="https://ultralytics.com/yolov3" target="_blank">
   <img width="550" src="https://user-images.githubusercontent.com/20294786/166425546-33849dcf-8596-48ce-85b5-adcb7ec022f1.png"></a>
</p>
<br>
<div>
   <a href="https://colab.research.google.com/drive/1psWi3GFC8kHSyYdsyAUNG0ONfVPmBQE3#scrollTo=fdpslOHa6XSK"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"></a>
</div>
<br>
<div align="center">
   <img width="%" />
   <a href="https://youtu.be/YYRLcmTpfbM">
   <img src="https://github.com/ultralytics/yolov5/releases/download/v1.0/logo-social-youtube.png" width="10%"/>
   </a>
   <img width="2%" />
   <a href="https://drive.google.com/drive/folders/1-6pJ0ffOLqMQtK0EmWnkKxp107rAVFrR?usp=sharing">
   <img src="https://user-images.githubusercontent.com/20294786/166430750-e6dea8b4-460f-4813-9a91-5495b628ba40.png" width="8%"/>
   </a>
</div>

<br>
<p>
카메라 감독이 일일이 수백명의 방청객(청중)을 바라보며 감정을 분석하고 실시간으로 상황에 맞는 감정을 파악해서 카메라 감독을 보조할 수 있는 AI 카메라 시스템을 구축하는 것이 목표입니다.
</p>
</div>
<br>


## <div align="center">Datasets and Models</div>
<div>
   <p>
모델 학습에 사용된 데이터셋과 모델 파일은 상단 아이콘을 통해 다운로드 가능합니다. 
제공된 데이터셋과 모델 파일은 모델 학습 및 추론에 사용가능합니다. <br>
(활용 데이터셋 : AIHub 한국인 감정 데이터, widerface 데이터)
   </p>
</div>

    datasets/
        AIHub/
        widerface/
        AIHub_widerface/
    models/
        AIHub.pt
        AIHub_widerface.pt
        AIHub_widerface_tuning.pt


## <div align="center">Quick Start Examples</div>

<details open>
   <summary><b>Install</b></summary>

[**Python>=3.6.0**](https://www.python.org/) is required with all
[requirements.txt](https://github.com/ultralytics/yolov3/blob/master/requirements.txt)   
installed including
[**PyTorch>=1.7**](https://pytorch.org/get-started/locally/):
<!-- $ sudo apt update && apt install -y libgl1-mesa-glx libsm6 libxext6 libxrender-dev -->

```bash
$ git clone https://github.com/Programmers-AI-3/Face_Flow --recurse-submodules 
$ pip install -r requirements.txt
$ cd Face_Flow
```
</details>

<details open>
<summary><b>Prerequisites</b></summary>
모델 테스트 시 공유폴더에 저장된 모델 파일을 로컬에 다운받아 놓아야 한다. 아래 3가지 파일 중 선택하여 다운로드 할 수 있다.
   <ul>
      <li>AIHub.pt : AIHub 데이터로만 학습한 모델</li>
      <li>AIHub_widerface.pt : AIHub 데이터와 widerface 데이터로 학습한 모델</li>
      <li>AIHub_widerface_tuning.pt : AIHub 데이터와 widerface 데이터로 학습하고 하이퍼파라미터 튜닝을 한 모델로 가장 정확도가 높음.</li>
   </ul>
   
```bash
$ mv {다운받은 .pt 파일} {프로젝트 경로}/Face_Flow/
```
</details>

<details open>
<summary><b>Inference</b></summary>
django 프로젝트를 실행시켜 서버를 동작시키고  
비디오를 업로드하여 사전에 학습된 모델을 통해서 추론된 동영상을 다운로드 할 수 있다.

```bash
$ python manage.py runserver
```
</details>


<details open>
<summary><b>Web Tutorials</b></summary>
   
- [Face Flow WIKI](https://github.com/Programmers-AI-3/Face_Flow/wiki)
   
</details>


## <div align="center">Why Face Flow?</div>

<details open>
<summary><b>Sample outputs</b></summary>
   
- Class 1: Happy
<img width="400" src="https://user-images.githubusercontent.com/4311289/167237734-93f0248d-666b-4d13-8046-7acc2dabd4f0.png">
   
- Class 3: Neutral
<img width="400" src="https://user-images.githubusercontent.com/4311289/167237741-eedb0bf9-3b4c-4de3-b7c9-8c51b7594751.png">

</details>

<details open>
<summary><b>Training Results</b></summary>
   
- Confusion matrix
<img width="800" src="https://user-images.githubusercontent.com/93199081/166864110-61bc406f-1516-47b2-b8d2-3114a5d80669.png">

- Metrics
<img width="800" src="https://user-images.githubusercontent.com/93199081/166864147-6ea85c7f-7c42-43d6-bba5-381fcf3100b7.png">

- Inference Time
<img width="800" src="https://user-images.githubusercontent.com/93199081/166864310-cab614a0-7dd3-42af-a4c8-783e79f10de4.jpg">

- mAP comparison
<img width="800" src="https://user-images.githubusercontent.com/93199081/166864377-90f7fc13-a08d-451f-a22f-11aef40526b8.jpg">

</details>


## <div align="center">Environments</div>
<div align="center">
    <img src="https://user-images.githubusercontent.com/93199081/166865453-5589da37-851b-4549-9e23-5f14157c8663.jpg" width="100%"/>

</div>



## <div align="center">Reference</div>
<div>
   <ul>
      <li>datasets
         <ul>
            <li>widerface : http://shuoyang1213.me/WIDERFACE/</li>
            <li>AIHub : https://aihub.or.kr/aidata/27716</li>
         </ul>
      </li>
      <li>code
         <ul>
            <li>widerface label converter : https://github.com/zlmo/Face-Detection</li>
            <li>ultralytics yolov3 : https://github.com/ultralytics/yolov3</li>
         </ul>
      </li>
   </ul>
</div>


