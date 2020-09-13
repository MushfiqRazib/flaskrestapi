1. Initiate a migration folder using init command for alembic to perform the migrations.

python manage.py db init

2. Create a migration script from the detected changes in the model using the migrate command.

python manage.py db migrate --message 'initial database migration'

3. Apply the migration script to the database by using the upgrade command.

python manage.py db upgrade

4. If everything runs successfully, a new sqlLite database taskrestapi.db file generated inside the main package.

Each time the database model changes, repeat the migrate and upgrade commands


5. Run application: python manage.py run

6. Test application: python manage.py test

