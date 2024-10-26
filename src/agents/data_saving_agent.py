import boto3

class DataSavingAgent:
    def save_to_s3(self, data, filename):
        s3 = boto3.client('s3')
        s3.put_object(Bucket='your-bucket-name', Key=filename, Body=data)
