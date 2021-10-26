
![](.github/assets/images/cover.jpg)

<div align="center">
<b>Tabulas</b> . Mission planning modules and the applications of path-finding algorithms in Self-Driving Cars (Analysis, Implementation)


</div>

<br>


---

<br>

## 💎 **Repository structure**
The architecture of consists of five **directories** [analysis, data, src, static, templates]


| Service | Type | Description |
----------|-----|------------|
[**analysis**](./analysis/analysis.md)  | Algorithms |   In-detail analysis, explanation and implementation of `Dijkstra's, A*` Algorithms
[**data**](./data/)   | Data Structures | The implemented data structures will be used in the Algorithms
[**src**](./src/)    | Algorithms | The implementation of [`Dijkstra's`](./analysis/dijkstra/README.md), [`A*`](./analysis/a*/README.md) that will be used when a user sends a request for calculating the distance between two points
[**static**](./static/) | Assets |  Styles, Automatically rendered/generated Algorithms results
[**templates**](./templates/)   | UI | Following Flask's Architecture style in this folder, you can find all the UI relevant files



<br>
<br>

## 📦 **Setup**
 

1. ### **Setting up environment**
   
   The following instructions work for <small>[Mac, Linux, Windows]</small>

   ---
 

   1 - Install virtual env to be able to create Python environments

   ```bash
   sudo pip3 install virtualenv 
   ```

   2 - Create a new environment

   ```bash
   virtualenv env
   ```
   
   3 - Active the virtual environment:

   ```bash
   virtualenv env
   ```


   ---

 

2. ###  **Modules Setup**
   After setting up your development environment, make sure to install the app's required packages by running:
   ```
   pip3 install -r requirements.txt
   ```

   ---
 
3. ###  **Setting up environment variables**

 
   1 - Naming the flask App:
   ```
   export FLASK_APP=tabulas
   ```
 

   2 - Setting up development mode:
   ```
   export FLASK_ENV=development
   ```
 

   ---


4. ###  🚀 **Run**
   And now you can finally run the app using: 
   ```
   flask run
   ```

---

<br>

## 🐳 **Running with Docker**
If you already have Docker installed, feel free to run the app and set it up in one command:

```
docker-compose up  
```

**Tabulas** will be running on [http://localhost:5000](http://localhost:5000) 🚀


---



<div align="center">

**Thanks for reading 🎉**

</div>
