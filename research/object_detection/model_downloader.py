#copied from https://github.com/BenGreenfield825
import wget
model_link = "blank" #<model_gz_url>
wget.download(model_link)
import tarfile
tar = tarfile.open('blank') #<model_gz>
tar.extractall('.')
tar.close()