import os 
from sqlalchemy import create_engine

engine = create_engine(os.environ('BUILD_ENGINE'))
r = engine.execute('SELECT 1 as hi;')

print('it worked!')
print(r.fetchall())