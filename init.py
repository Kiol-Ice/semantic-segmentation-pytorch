import os 
import wget

# Image and model names
TEST_IMG = 'ADE_val_00001519.jpg'
MODEL_NAME = 'ade20k-resnet50dilated-ppm_deepsup'
MODEL_PATH = f'./ckpt/{MODEL_NAME}'
RESULT_PATH = './'

ENCODER = f'{MODEL_NAME}/encoder_epoch_20.pth'
DECODER = f'{MODEL_NAME}/decoder_epoch_20.pth'


os.makedirs(MODEL_PATH, exist_ok=True)

if not os.path.exists(f'./ckpt/{ENCODER}'):
    print('Encoder download ...')
    wget.download(f'http://sceneparsing.csail.mit.edu/model/pytorch/{ENCODER}', MODEL_PATH)
    
if not os.path.exists(f'./ckpt/{DECODER}'):
    print('Decoder download ...')
    wget.download(f'http://sceneparsing.csail.mit.edu/model/pytorch/{DECODER}', MODEL_PATH)
    
if not os.path.exists(f'./{TEST_IMG}'):
    print('Test image download ...')
    wget.download(f'http://sceneparsing.csail.mit.edu/data/ADEChallengeData2016/images/validation/{TEST_IMG}')

# wget.download("https://nyc3.digitaloceanspaces.com/ml-files-distro/v1/sentiment-analysis-is-bad/data/sentiment140-subset.csv.zip")