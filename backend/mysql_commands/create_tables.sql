CREATE TABLE Admin (
    AdminId INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    AdminUser VARCHAR(128) NOT NULL,
    AdminPass VARCHAR(128) NOT NULL
);

CREATE TABLE Recordings (
    VideoId INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    VideoName VARCHAR(128) NOT NULL,
    VideoDir VARCHAR(256) NOT NULL,
    VideoTaken DATETIME NOT NULL
);

CREATE TABLE UserData (
    UserId INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(128) NOT NULL,
    LastName VARCHAR(128),
    Gender VARCHAR(12),
    Role VARCHAR(128),
    LastScan DATETIME NOT NULL,
    LastTemperature FLOAT NOT NULL
);

CREATE TABLE UserPhoto (
    PhotoId INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    PhotoName VARCHAR(128) NOT NULL,
    PhotoDir VARCHAR(256) NOT NULL
);

CREATE TABLE UserDataset (
    UserId INT NOT NULL,
    PhotoId INT NOT NULL,
    PhotoTaken DATETIME NOT NULL,
    FOREIGN KEY (UserId) REFERENCES UserData(UserId),
    FOREIGN KEY (PhotoId) REFERENCES UserPhoto(PhotoId)
);

CREATE TABLE UserScan (
    UserId INT NOT NULL,
    FirstName VARCHAR(128) NOT NULL,
    LastName VARCHAR(128),
    Gender VARCHAR(12),
    Role VARCHAR(128),
    ScanDate DATETIME NOT NULL,
    Temperature FLOAT,
    FOREIGN KEY (UserId) REFERENCES UserData(UserId)
);

CREATE TABLE UserScanPhoto (
    PhotoScanId INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    UserId INT NOT NULL,
    PhotoName VARCHAR(128) NOT NULL,
    PhotoDir VARCHAR(256) NOT NULL,
    FOREIGN KEY (UserId) REFERENCES UserData(UserId)
);


/* TABLE RESULT
Admin
+-----------+--------------+------+-----+---------+----------------+
| Field     | Type         | Null | Key | Default | Extra          |
+-----------+--------------+------+-----+---------+----------------+
| AdminId   | int(11)      | NO   | PRI | NULL    | auto_increment |
| AdminUser | varchar(128) | NO   |     | NULL    |                |
| AdminPass | varchar(128) | NO   |     | NULL    |                |
+-----------+--------------+------+-----+---------+----------------+

Recordings
+------------+--------------+------+-----+---------+----------------+
| Field      | Type         | Null | Key | Default | Extra          |
+------------+--------------+------+-----+---------+----------------+
| VideoId    | int(11)      | NO   | PRI | NULL    | auto_increment |
| VideoName  | varchar(128) | NO   |     | NULL    |                |
| VideoDir   | varchar(256) | NO   |     | NULL    |                |
| VideoTaken | datetime     | NO   |     | NULL    |                |
+------------+--------------+------+-----+---------+----------------+

UserData
+-----------+--------------+------+-----+---------+----------------+
| Field     | Type         | Null | Key | Default | Extra          |
+-----------+--------------+------+-----+---------+----------------+
| UserId    | int(11)      | NO   | PRI | NULL    | auto_increment |
| FirstName | varchar(128) | NO   |     | NULL    |                |
| LastName  | varchar(128) | YES  |     | NULL    |                |
| Gender    | varchar(12)  | YES  |     | NULL    |                |
| Age       | int(11)      | YES  |     | NULL    |                |
| Address   | varchar(256) | YES  |     | NULL    |                |
| Role      | varchar(128) | YES  |     | NULL    |                |
| LastScan  | datetime     | NO   |     | NULL    |                |
+-----------+--------------+------+-----+---------+----------------+

UserDataset
+------------+----------+------+-----+---------+-------+
| Field      | Type     | Null | Key | Default | Extra |
+------------+----------+------+-----+---------+-------+
| UserId     | int(11)  | NO   | MUL | NULL    |       |
| PhotoId    | int(11)  | NO   | MUL | NULL    |       |
| PhotoTaken | datetime | NO   |     | NULL    |       |
+------------+----------+------+-----+---------+-------+

UserPhoto
+-----------+--------------+------+-----+---------+----------------+
| Field     | Type         | Null | Key | Default | Extra          |
+-----------+--------------+------+-----+---------+----------------+
| PhotoId   | int(11)      | NO   | PRI | NULL    | auto_increment |
| PhotoName | varchar(128) | NO   |     | NULL    |                |
| PhotoDir  | varchar(256) | NO   |     | NULL    |                |
+-----------+--------------+------+-----+---------+----------------+

UserScan
+-----------+--------------+------+-----+---------+-------+
| Field     | Type         | Null | Key | Default | Extra |
+-----------+--------------+------+-----+---------+-------+
| UserId    | int(11)      | NO   | MUL | NULL    |       |
| FirstName | varchar(128) | NO   |     | NULL    |       |
| LastName  | varchar(128) | YES  |     | NULL    |       |
| Gender    | varchar(12)  | YES  |     | NULL    |       |
| Age       | int(11)      | YES  |     | NULL    |       |
| Address   | varchar(256) | YES  |     | NULL    |       |
| Role      | varchar(128) | YES  |     | NULL    |       |
| ScanDate  | datetime     | NO   |     | NULL    |       |
+-----------+--------------+------+-----+---------+-------+

UserScanPhoto
+-------------+--------------+------+-----+---------+----------------+
| Field       | Type         | Null | Key | Default | Extra          |
+-------------+--------------+------+-----+---------+----------------+
| PhotoScanId | int(11)      | NO   | PRI | NULL    | auto_increment |
| UserId      | int(11)      | NO   | MUL | NULL    |                |
| PhotoName   | varchar(128) | NO   |     | NULL    |                |
| PhotoDir    | varchar(256) | NO   |     | NULL    |                |
+-------------+--------------+------+-----+---------+----------------+
*/
