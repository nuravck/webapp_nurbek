# webapp_nurbek

**Full‑stack AWS Deployment**  
- **Static frontend** on S3: https://ap-south-1.console.aws.amazon.com/s3/buckets/nurbek2t?region=ap-south-1&bucketType=general&tab=properties
- **Flask API** on EC2: https://ap-south-1.console.aws.amazon.com/ec2/home?region=ap-south-1#InstanceDetails:instanceId=i-0e6a58009c69784e2
- **PostgreSQL** on RDS: https://ap-south-1.console.aws.amazon.com/rds/home?region=ap-south-1#database:id=nurbek2t;is-cluster=false;tab=connectivity

## Architecture

1. **S3** hosts `index_nurbek.html`.  
2. **EC2** runs `app.py` (Flask + CORS + psycopg2).  
3. **RDS** database `postgres`, table `tbl_nurbek_students`.

## Setup

1. Turn on EC2, RDS in AWS
2. Connect to EC2 Instance
3. ```source venv/bin/activate``` then ```cd webapp``` and run ```python app.py```
4. Go to the link: http://nurbek2t.s3-website.ap-south-1.amazonaws.com

### 1. Clone Repo

```bash
git clone https://github.com/nuravck/webapp_nurbek.git
cd webapp_nurbek
```
