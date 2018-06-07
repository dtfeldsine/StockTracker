# Define your tables below (or better in another model file) for example
#
# >>> db.define_table('mytable', Field('myfield', 'string'))
#
# Fields can be 'string','text','password','integer','double','boolean'
#       'date','time','datetime','blob','upload', 'reference TABLENAME'
# There is an implicit 'id integer autoincrement' field
# Consult manual for more options, validators, etc.

db.define_table('stock',
                Field('name'),
                Field('price', 'integer'),
                Field('quantity', 'integer', default=1),
                Field('favorite', 'boolean', default=False),
                Field('user_email', default=auth.user.email if auth.user else None),
                Field('is_public', 'boolean', default=False),
                
                Field('company_name', 'text'),
                Field('company_symbol', 'text'),
                Field('company_description', 'text'),
                
                Field('day_open', 'text'),
                Field('day_high', 'text'),
                Field('day_low', 'text'),
                Field('day_close', 'text'),
                Field('day_volume', 'integer')
                
                Field('personal_open', 'text'),
                Field('personal_high', 'text'),
                Field('personal_low', 'text'),
                Field('personal_close', 'text'),
                Field('personal_volume', 'integer'),
                )

# after defining tables, uncomment below to enable auditing
# auth.enable_record_versioning(db)
