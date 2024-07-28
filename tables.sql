CREATE TABLE Users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL
);

CREATE TABLE Directories (
    directory_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    parent_directory_id INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (parent_directory_id) REFERENCES Directories(directory_id)
);

CREATE TABLE Files (
    file_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    directory_id INT,
    size BIGINT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (directory_id) REFERENCES Directories(directory_id)
);

CREATE TABLE Permissions (
    permission_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    file_id INT,
    directory_id INT,
    can_read BOOLEAN DEFAULT TRUE,
    can_write BOOLEAN DEFAULT FALSE,
    can_execute BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (file_id) REFERENCES Files(file_id),
    FOREIGN KEY (directory_id) REFERENCES Directories(directory_id)


);
INSERT INTO Users (username, password) VALUES ('user1', 'password1'), ('user2', 'password2');

INSERT INTO Directories (name, parent_directory_id) VALUES 
('root', NULL), 
('home', 1), 
('user1', 2), 
('user2', 2);

INSERT INTO Files (name, directory_id, size) VALUES 
('file1.txt', 3, 1024), 
('file2.txt', 3, 2048), 
('file3.txt', 4, 4096);
