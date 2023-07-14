from sqlalchemy import create_engine, text
# import MySQLdb
# import os
# from dotenv import load_dotenv
# load_dotenv()

# connection = MySQLdb.connect(
#     host=os.getenv("HOST"),
#     user=os.getenv("USERNAME"),
#     passwd=os.getenv("PASSWORD"),
#     db=os.getenv("DATABASE"),
#     autocommit=True,
#     ssl_mode="VERIFY_IDENTITY",
#     ssl={
#         "ca": "/etc/ssl/cert.pem"
#     }
# )


# connection = MySQLdb.connect(
#     host=os.getenv("aws.connect.psdb.cloud"),
#     user=os.getenv("ufo8l30tzndvoymlcbyx"),
#     passwd=os.getenv("pscale_pw_pPquCMt48QmheOAA4nn2yVe8GIbvvvHa5Snv7ioUhQ7"),
#     db=os.getenv("derba_trans"),
#     autocommit=True,
#     ssl_mode="VERIFY_IDENTITY",
#     ssl={
#         "ca": "/etc/ssl/cert.pem"
#     }
# )

db_connection_string = "mysql+pymysql://ufo8l30tzndvoymlcbyx:pscale_pw_pPquCMt48QmheOAA4nn2yVe8GIbvvvHa5Snv7ioUhQ7@aws.connect.psdb.cloud/derba_trans?charset=utf8mb4"

engine = create_engine(
    db_connection_string,
    connect_args={
        "ssl": {
            "ca": "/etc/ssl/cert.pem"
        }
    }
)

with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs"))
    print(result.all())
