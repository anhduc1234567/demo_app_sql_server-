/*USE master
DROP DATABASE IF EXISTS Students_management

CREATE DATABASE Students_management;

DROP TABLE IF EXISTS Students_management.dbo.Persons
CREATE TABLE Students_management.dbo.Persons (
	CCCD VARCHAR(20) PRIMARY KEY,
	First_Name NVARCHAR(25) NOT NULL,
	Mid_Name NVARCHAR(50),
	Last_Name NVARCHAR(25) NOT NULL,
	Birth DATE NOT NULL,
);

DROP TABLE IF EXISTS Students_management.dbo.Students
CREATE TABLE Students_management.dbo.Students (
	Student_ID VARCHAR(20) PRIMARY KEY,
	CCCD VARCHAR(20) NOT NULL UNIQUE,
	Email NVARCHAR(225),
	Address NVARCHAR(225) NOT NULL,
	Gpa FLOAT(2) NOT NULL,
	Major NVARCHAR(225) NOT NULL,
	FOREIGN KEY (CCCD) REFERENCES  Students_management.dbo.Persons(CCCD)
	ON UPDATE CASCADE
	ON DELETE CASCADE
);
DROP TABLE IF EXISTS Students_management.dbo.Subjects
CREATE TABLE Students_management.dbo.Subjects (
	Subject_Id INT PRIMARY KEY,
	Name NVARCHAR(255) NOT NULL,
	Credit INT NOT NULL,
	Lesson INT NOT NULL,
	Type NVARCHAR(255) NOT NULL
);

DROP TABLE IF EXISTS Students_management.dbo.Registers
CREATE TABLE Students_management.dbo.Registers (
	RegisterId INT PRIMARY KEY,
	Subject_Id INT NOT NULL,
	Student_ID VARCHAR(20),
	Time_register DATETIME2 ,
	FOREIGN KEY (Subject_Id) REFERENCES  Students_management.dbo.Subjects(Subject_Id)
	ON UPDATE CASCADE
	ON DELETE CASCADE,
	FOREIGN KEY (Student_ID) REFERENCES  Students_management.dbo.Students(Student_ID)
	ON UPDATE CASCADE
	ON DELETE CASCADE
);*/
/*INSERT INTO Students_management.dbo.Persons(CCCD,First_Name,Mid_Name,Last_Name,Birth) 
VALUES  ('01234567990',N'Nguyễn',N'Phong',N'Khắc','2005-8-12'),
		('01234567890',N'Nguyễn',N'Văn',N'Ngọc','2005-3-10'),
		('01234567891',N'Đỗ',N'Thị Mỹ',N'Linh','2005-6-23'),
		('01234567892',N'Nguyễn',N'Ngọc',N'Khánh','2005-1-21'),
		('01234567893',N'Lê',N'Công',N'Tuấn','2005-9-30'),
		('01234567894',N'Hoàng',N'Thanh',N'Tuấn','2004-7-27'),
		('01234567896',N'Đỗ',N'Quang',N'Duy','2005-5-5'),
		('01234567897',N'Phạm',N'Thị Như',N'Mai','2005-9-23'),
		('01234567898',N'Lê',N'Thị Quỳnh',N'Như','2005-8-18'),
		('09234567890',N'Trần',N'Thị Thu',N'Hương','2005-3-10'),
		('09234567891',N'Đinh',N'Tiến',N'Thành','2006-9-16'),
		('09234567892',N'Đỗ',N'Bình',N'Minh','2004-1-6'),
		('09234567893',N'Trương',N'Khánh',N'Luân','2005-11-1'),
		('09234567894',N'Phan',N'Sơn',N'Nam','2004-2-7'),
		('023154698747',N'Nguyễn',N'Ngọc',N'Hưng','2005-1-7')

/*		*/
INSERT INTO Students_management.dbo.Students(Student_ID,CCCD,Email,Address,Gpa,Major)
VALUES   ('SV1000','01234567990','phongkhac@xmail.com',N'Chùa Bộc, Ba Đình, Hà Nội',3.68,N'Quản trị nhân lực'),
		 ('SV1001','01234567890','minhngoc@xmail.com',N'Xuân Phương,Nam Từ Liêm, Hà Nội',3.25,N'Công nghệ thông tin'),
		 ('SV1002','01234567891','linhlinhdo@xmail.com',N'Minh Khai, Bắc Từ Liêm, Hà Nội',3.75,N'Công nghệ thông tin'),		
		 ('SV1003','01234567892','khanhngocnguyen@xmail.com',N'Cổ Nhuế, Bắc Từ Liêm, Hà Nội',3.45,N'Công nghệ thông tin'),		
		 ('SV1004','01234567893','congtuanle@xmail.com',N'Bách Khoa, Hai Bà Trưng, Hà Nội',3.15,N'Công nghệ thông tin'),		
		 ('SV1005','01234567894','thanhtuanhoang@xmail.com',N'Bách Khoa, Hai Bà Trưng, Hà Nội',3.18,N'Công nghệ thông tin'),		
		 ('SV1007','01234567896','quangduydeptrai@xmail.com',N'Ao Sen, Hà Đông, Hà Nội',3.65,N'Công nghệ thông tin'),		
		 ('SV1008','01234567897','nhumaipham@xmail.com',N'Mai Dịch, Cầu Giấy, Hà Nội',3.45,N'Công nghệ thông tin'),		
		 ('SV1009','01234567898','quynhnhule@xmail.com',N'Thanh Chương, Tây Hồ, Hà Nội',3.95,N'Công nghệ thông tin'),		
		 ('SV1010','09234567890','thuhuongcute@xmail.com',N'Mễ Trì Hạ, Nam Từ Liêm, Hà Nội',3.86,N'Công nghệ thông tin'),		
		 ('SV1011','09234567891','thanhtiendinh255@xmail.com',N'Mễ Trì Thượng, Nam Từ Liêm, Hà Nội',3.68,N'Công nghệ thông tin'),		
		 ('SV1012','09234567892','binhminh@xmail.com',N'Minh Khai, Bắc Từ Liêm, Hà Nội',2.54,N'Công nghệ thông tin'),		
		 ('SV1013','09234567893','khanhluan@xmail.com',N'Xa La, Hà Đông, Hà Nội',1.68,N'Công nghệ thông tin'),		
		 ('SV1014','09234567894','namphansao@xmail.com',N'Khuất Duy Tiến, Thanh Xuân, Hà Nội',3.21,N'Công nghệ thông tin'),		 		 
		 ('SV1016','023154698747','ngochung@gmail.com',N'Yên Nghĩa, Hà Đông, Hà Nội',3.85,N'Đa phương tiện')	*/
/*INSERT INTO Students_management.dbo.Subjects(Subject_Id,Name,Credit,Lesson,Type) 
VALUES ('1001',N'C#','4','45',N'Cơ sở ngành'),
		('1002',N'Ngôn ngữ lập trình C','2','25',N'Cơ bản'),
		('1003',N'Phân tích thiết kế hệ thống','3','36',N'Chuyên ngành'),
		('1004',N'Lập trình Android','4','45',N'Nâng cao'),
		('1005',N'Lập trình IOS','3','42',N'Chuyên ngành'),
		('1006',N'Nhập môn công nghệ phần mền','3','36',N'Chuyên ngành'),
		('1007',N'Thiết kế giao diện web','2','25',N'Cơ sở ngành'),
		('1008',N'Lập trình nhúng','3','35',N'Chuyên ngành'),
		('1009',N'Các hệ thống phân tán','3','36',N'Chuyên ngành'),
		('1010',N'Cơ sở dữ liệu phân tán','4','46',N'Cơ sở ngành'),
		('1011',N'Lập trình hướng đối tượng','4','46',N'Cơ bản'),
		('1012',N'SQL','3','32',N'Cơ sở ngành')*/
INSERT INTO Students_management.dbo.Registers(RegisterId,Subject_Id,Student_ID,Time_register) 
VALUES 
 (1002,1002,'SV1001','2023-3-1 00:01:26'),
 (1003,1003,'SV1001','2023-3-1 00:01:25'),
 (1004,1004,'SV1001','2023-3-1 00:01:29'),
 (1005,1001,'SV1002','2023-3-1 00:02:56'),
 (1006,1002,'SV1002','2023-3-1 00:03:05'),
 (1007,1001,'SV1003','2023-3-2 10:11:25'),
 (1008,1002,'SV1004','2023-3-2 10:01:25'),
 (1009,1004,'SV1005','2023-3-3 09:34:25'),
 (1010,1004,'SV1007','2023-3-3 09:24:25'),
 (1011,1002,'SV1007','2023-3-3 10:01:25')