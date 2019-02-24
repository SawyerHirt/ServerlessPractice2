import boto3
import zipfile
import io
import mimetypes

s3 = boto3.resource('s3')

portfolio_bucket = s3.Bucket('serverlesswebsitesawyertutorial')
build_bucket = s3.Bucket('serverless.company-practice-portfolio')

portfolio_zip = io.BytesIO()
build_bucket.download_fileobj('serverless.company-practice-portfolio-artifacts.zip', portfolio_zip)

with zipfile.ZipFile(portfolio_zip) as myzip:
    for nm in myzip.namelist():
        obj = myzip.open(nm)
        portfolio_bucket.upload_fileobj(obj, nm,
          ExtraArgs={'ContentType': mimetypes.guess_type(nm)[0]})
        portfolio_bucket.Object(nm).Acl().put(ACL='public-read')
