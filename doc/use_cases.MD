# Use Case #1:
## Filter images for use in Fourier transforms to give basic protein localization data.

Components:
```
* Fast-Fourier transform package
* Image upload
```


# Use Case #2
## Create a multi-resolution histogram to describe further protein 
patterning.

Components:
```
* Model
* Image upload
* Gaussian Blur package
* Difference Histogram package
* Multi-resolution histogram package
* Patterening transforms
```

# Use Case #3
## Use edge and object statistics to classify objects and proteins and their 
localization patterns.

Components:
```
* Object Count
* Centroids
* Euler Distance package
* 10-bin histogram
* Object Area package
* 
```

# Use Case #4
## Generate a set of images and train the neural network in charge of 
classifying images.

Components:
* Image editor package
* Neural Network setup
* Image generator package




# Use Case #5
## Classify protein domains and localization for a given image supplied by 
the user based on the trained model 

Components:
``` 
* Model
* Image set
```
