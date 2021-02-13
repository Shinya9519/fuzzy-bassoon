# -*- coding: utf-8 -*-
#　指定したpath内のファイルをすべてS3のバケットにUPloadする
import boto3
import os

s3 = boto3.resource('s3') #S3オブジェクトを取得
path = #local
bucket_name = #your AWS S3bucket

files = os.listdir(path)

for filenames_01 in files:
    print(filenames_01)

for filenames_01 in files:
    from_filename =path+"/"+filenames_01
    s3.meta.client.upload_file(from_filename,bucket_name,filenames_01)
    print("uploaded {0}".format(filenames_01))
