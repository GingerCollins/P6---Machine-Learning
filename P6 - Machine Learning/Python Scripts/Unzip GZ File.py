import gzip
import shutil

with gzip.open('E:/GIT/Udacity/ud120-projects/enron_mail_20150507.tar.gz', 'rb') as f_in:
    with open('E:/Udacity/Data Analysis/P6 - Machine Learning/enron_mail_20150507.txt', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)