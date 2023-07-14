from sqlalchemy import create_engine, text


db_connection_string = "mysql+pymysql://root:123456789@localhost/sql_invoicing?charset=utf8mb4"

# db_connection_string = "mysql+pymysql://ufo8l30tzndvoymlcbyx:pscale_pw_pPquCMt48QmheOAA4nn2yVe8GIbvvvHa5Snv7ioUhQ7@aws.connect.psdb.cloud/derba_trans?charset=utf8mb4"


# with engine.connect() as conn:
#     result = conn.execute(text("SELECT * FROM jobs"))
#     print(result.all())
engine = create_engine(db_connection_string)

# with engine.connect() as conn:
#     result = conn.execute(text("select * from clients"))

#     result_dicts = []
#     for row in result.all():
#         result_dicts.append(row._mapping)
#     print(result_dicts)

# print("type(result):", type(result))
# result_all = result.all()
# print("type(result.all()):", type(result_all))
# frist_result = result_all[0]
# print("type(first_result):", type(frist_result))
# first_result_dict = result_all[0]._mapping
# print("type(first_result_dict):", type(first_result_dict))
# print(first_result_dict)


# print("type(result):", type(result))
# result_all = result.all()
# print("type(result.all()):", type(result_all))
# print("result.all():", result_all)


# db_connection_string = "mysql+pymysql://sxt25slwydtbq7a299u0:pscale_pw_kV2eiTBwRbIfrZeKHvc2eRjRa00CBbedNKTCYSebAgl@aws.connect.psdb.cloud/derba_trans?charset=utf8mb4"

# engine = create_engine(
#     db_connection_string,
#     connect_args={
#         "ssl": {
#             "ca": "/etc/ssl/cert.pem",

#         }
#     })

# with engine.connect() as conn:
#     result = conn.execute(text("select * from jobs"))
#     print("type(result):", type(result))
#     result_all = result.all()
#     print("type(result.all()):", type(result_all))
#     print("result.all():", result_all)
