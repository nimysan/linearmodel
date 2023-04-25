import boto3
import os

s3_client = boto3.client("s3")

dir = '/tmp/b123/k123'

if not os.path.exists(dir):
    os.makedirs(dir)

s3_client.download_file('media.cuteworld.top', 'webwxgetmsgimg.jpg', dir + '/abc.jpg')

print( dir + '/abc.jpg')