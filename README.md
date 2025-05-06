# webapp_nurbek

**Full‑stack AWS Deployment**  
- **Static frontend** on S3  
- **Flask API** on EC2  
- **PostgreSQL** on RDS  

## Architecture

1. **S3** hosts `index_nurbek.html`.  
2. **EC2** runs `app.py` (Flask + CORS + psycopg2).  
3. **RDS** database `postgres`, table `tbl_nurbek_students`.

## Setup

### 1. Clone Repo

```bash
git clone https://github.com/nuravck/webapp_nurbek.git
cd webapp_nurbek
