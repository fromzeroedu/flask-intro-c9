### Step #20

### Start the Mysql database:
```
mysql-ctl start
```

### Enter the Mysql terminal:
```
mysql-ctl cli
```

Once inside MySQL:
```
CREATE DATABASE my_flask_app;
USE my_flask_app;
CREATE TABLE user(
    user_id INT NOT NULL AUTO_INCREMENT,
    username VARCHAR(64) NOT NULL,
    password VARCHAR(64) NOT NULL,
    PRIMARY KEY(user_id)
    );
INSERT INTO user VALUES('', 'jorge', '12345');
```
### Add PyMySQL to requirements.txt and pip install:
```
pip install -r requirements.txt
```