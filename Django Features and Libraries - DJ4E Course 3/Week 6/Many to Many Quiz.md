# Many to Many Quiz

### 1. As one-to-many relationship in a data model involved two database tables. How many tables are involved in representing a many-to-many relationship?
- [ ] 5
- [x] 3
- [ ] 2
- [ ] 1
- [ ] 4

### 2. If you were looking at a link in a data model diagram, which of these would represent a many-to-many relationship? 
- [ ] 2 -- 2
- [x] 0..* --- 1..*
- [ ] 1 -- 0..*
- [ ] 0 -- 0
- [ ] 1 -- 1

### 3. In Django, what type of field is used to represent a many-to-many relationship?
- [ ] models.ManyToManyRelationship
- [ ] models.ForeignKey
- [ ] models.ThroughKey
- [ ] models.IntField
- [x] models.ManyToManyField

### 4. Which of the following is NOT a common name for the additional table needed to represent a many-to-many relationship between two tables?
- [ ] Junction Table
- [ ] Through Table
- [ ] Join Table
- [ ] Bridge Table
- [x] Lookup Table
- [ ] Association Table

### 5. In models.py when you want to explicitly model a Junction Table, what is the attribute in the two lined table models used to indicated which Junction table to use to connect the two tables?
- [ ] join_through
- [ ] join
- [ ] on_delete
- [x] through
- [ ] junction

### 6. What kind of model fields will be found in every Junction table?
- [ ] models.ManyToManyField
- [x] models.ForeignKey
- [ ] models.JunctionFields
- [ ] models.OutboundKeys
- [ ] models.CharField

### 7. If you have a many-to-many relationship between books and authors and you are inserting a new author for a book, which of the following orders of operations will work?  
- [ ] insert the connection, insert the book, insert the author
- [ ] insert the connection, insert the author, insert the book
- [ ] insert the book, insert the connection, insert the author
- [x] insert the book, insert the author, insert the connection

### 8. You should never have any fields other than keys in a Junction table.  
- [ ] True
- [x] False
