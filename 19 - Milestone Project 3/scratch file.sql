CREATE TABLE [user] AS
( user_name                  VARCHAR(255)
, display_name               VARCHAR(255)  UNIQUE
, user_idno                  INT           PRIMARY
, public_key                 VARCHAR(MAX)
, public_key_expiration_date DATETIME
, public_key_deletion_date   DATETIME
, notes                      VARCHAR(1023)
, activation_date            DATETIME
, expiration_date            DATETIME
, update_date                DATETIME
)

CREATE TABLE [device] AS
( user_idno                  INT
, device_name                VARCHAR(255)
, device_idno                INT
, is_this_device_flag        INT
, public_key_expiration_date DATETIME
, public_key_deletion_date   DATETIME
, notes                      VARCHAR(1023)
, update_date                DATETIME
, sync_to_date               DATETIME
, sync_from_date             DATETIME
, )

CREATE TABLE [keys] AS
( device_or_user  CHAR(1)
, public_key      VARCHAR(MAX)
, private_key     VARCHAR(MAX)
, activation_date DATETIME
, expiration_date DATETIME
, deletion_date   DATETIME
)

CREATE TABLE [share] AS
( user_idno        INT
, account_idno     INT
, activation_date  DATETIME
, expiration_date  DATETIME
)

CREATE TABLE [account] AS
( account_name               VARCHAR(255)
, account_idno               INT
, user_name                  VARCHAR(255)
, local_flag                 INT
, notes                      VARCHAR(1023)
, activation_date            DATETIME
, public_key_expiration_date DATETIME
, updated_date               DATETIME
)

CREATE TABLE [password] AS
( password_idno   INT
, account_idno    INT
, password        VARCHAR(255)
, activation_date DATETIME
, expiration_date DATETIME
)

CREATE TABLE [user_friend] AS
SELECT * FROM [user] WHERE 1 = 2;

CREATE TABLE [device_friend] AS
SELECT * FROM [device] WHERE 1 = 2;

CREATE TABLE [keys_friend] AS
SELECT * FROM [keys] WHERE 1 = 2;

CREATE TABLE [share_friend] AS
SELECT * FROM [share] WHERE 1 = 2;

CREATE TABLE [account_friend] AS
SELECT * FROM [account] WHERE 1 = 2;

CREATE TABLE [password_friend] AS
SELECT * FROM [password] WHERE 1 = 2;