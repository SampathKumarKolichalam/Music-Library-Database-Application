### 🎵 **Music Library Database Application**  
 **A lightweight and efficient music library with full CRUD operations!**
![image](https://github.com/user-attachments/assets/b95747fd-bf7b-4f88-b55f-be3bb6bddfb5)

---

## **About the Project**  
The **Music Library Database Application** is a **database-driven** system that allows users to store, retrieve, update, and delete music records. It is built using **Python, SQLite, and the Bottle Framework**, with a RESTful API for seamless interactions.

---

## **Tech Stack**
| Technology  | Usage |
|------------|--------------------------------|
| **Programming Language** | Python |
| **Web Framework** | Bottle |
| **Database** | SQLite |
| **API Type** | RESTful APIs |


---

## **Key Features**
- **Full CRUD Functionality** – Add, view, update, and delete songs.  
- **SQLite Database** – Lightweight, efficient, and scalable.  
- **RESTful API** – Seamless interaction between frontend and backend.  
- **Optimized Query Performance** – Fast data retrieval and storage. 
- **Minimal Dependencies** – Lightweight and easy to deploy.  

---

## **Installation & Setup**
### **1.Clone the Repository**
```sh
git clone https://github.com/SampathKumarKolichalam/Music-Library-Database-Application.git
cd Music-Library-Database
```

### **2.Install Dependencies**
```sh
pip install bottle
```

### **3.Run the Application**
```sh
python app.py
```
Now, open **http://127.0.0.1:8080/** in your browser. 

---

## **API Endpoints**
### **1.Get All Songs**
```sh
GET /songs
```
#### **Response:**
```json
[
    {"id": 1, "title": "Song Name", "artist": "Artist Name", "album": "Album Name", "year": 2022}
]
```

### **2.Add a New Song**
```sh
POST /songs
```
#### **Request Body:**
```json
{
    "title": "New Song",
    "artist": "New Artist",
    "album": "New Album",
    "year": 2023
}
```

### **3.Update a Song**
```sh
PUT /songs/{id}
```
#### **Request Body:**
```json
{
    "title": "Updated Song",
    "artist": "Updated Artist",
    "album": "Updated Album",
    "year": 2024
}
```

### **4.Delete a Song**
```sh
DELETE /songs/{id}
```

---

---

## **Contributing**
**Want to improve this project?**  
Fork the repo, make your changes, and submit a pull request!  

```sh
git clone https://github.com/SampathKumarKolichalam/Music-Library-Database-Application.git
git checkout -b feature-branch
git commit -m "Added new feature"
git push origin feature-branch
```

---

## **License**
This project is free and access to all. Feel free to use and modify it.  

---

## **Connect with Me**
**Email:** [sampathkumarkolichalam@gmail.com]  

**LinkedIn:** [https://www.linkedin.com/in/sampath-kumar-kolichalam-18b57b1ab/]

---
