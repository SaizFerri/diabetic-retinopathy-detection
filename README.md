## Diabetic Retinopathy Detection

This is a course project for the HTW Berlin and its finality is to analyze and classify with the help of a Residual Neuronal Network (50), a state-of-the-art architecture of Convolutional Neuronal Network,  images of retinas which could be healthy or present some kind of sign of diabetic retinopathy.

This challenge was presented in [Kaggle](https://www.kaggle.com/c/diabetic-retinopathy-detection/).

In this notebook you will find a custom implementation of [ResNet-50](https://arxiv.org/pdf/1512.03385.pdf), which was used, in help with the pretrained ImageNet weights, to classify the images.

### Usage

All the image/label files can be found at the challenge in [here](https://www.kaggle.com/c/diabetic-retinopathy-detection/data). Download and extract the `trainLabels.csv` and save it as `train_labels.csv` . The test labels can be found [here](https://www.kaggle.com/c/diabetic-retinopathy-detection/discussion/16149), download it and save it as `test_labels.csv`

To preprocess the images please refer to the implementation of my project partner in this [repository](https://gitlab.com/_ts/diabetic-retinopathy-detection/tree/master#preprocessing). After you have followed his steps you should have a `train_dst.zip` and a `test_dst.zip`.

To be able to run this notebook you have to have a Google Drive account. The project structure in Google Drive should be as follow:

```
/retina_images
	--/pretrained
		--resnet50_weights_imagenet_no_dense.h5
	--/history
	--/checkpoints
		--resnet50_dense_regression_last_384_final.h5
	--train_labels.csv
	--test_labels.csv
	--train_dst.zip
	--test_dst.zip
```

### Run

Open the notebook in [Google Colab](https://colab.research.google.com/) and start running it. At the 4th cell you will be prompted to enter a token for your Google Drive account, so the Notebook has access to the files you just uploaded.

## Acknowledgments

Thanks to [EyePACS](http://www.eyepacs.com/) for providing the retinal images for the [original competition](https://www.kaggle.com/c/diabetic-retinopathy-detection).

Cuadros, J., & Bresnick, G. (2009). EyePACS: an adaptable telemedicine system for diabetic retinopathy screening. *Journal of diabetes science and technology*, *3*(3), 509–516.

Thanks to [Tobias](https://gitlab.com/_ts/) for providing the preprocessed images.