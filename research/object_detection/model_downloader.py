#copied from https://github.com/BenGreenfield825
import wget
model_link = ""
wget.download(model_link)
import tarfile
tar = tarfile.open('')
tar.extractall('.')
tar.close()