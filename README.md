# Parked Cars API

<p>This is a cool practice project my senior gave me when I began my current role in August 2021. I was new to flask but I would never turn down a challenge. It handles CRUD operations using a REST API with Python Flask and SQLite. I used SQLAlchemy for Object-Relational Mapping. I decided redo this project using JavaScript a few months later and refactored it, using a different project structure. <a href='https://github.com/Stanico-Knowles/parking-garage-api'>Check it out here.</a></p>

### Requirements.

<p>I am developing an API for a biased parking garage owner. If he likes a car, they get free parking. He likes all red, green, and black cars but hates everything else. However, he may like the car but if it's dirty, then it's half off not free. If he hates the car, it's full price. If he hates the car and it's dirty, double price. Base parking charge is $7.</p>

### The API will:

<ol>
    <li>Accept the license plate number, which will serve as primary key, car color, hours parked, and whether or not it is dirty.</li>
    <li>Return the same info that's accepted plus the price.</li>
    <li>Delete by PK</li>
    <li>Update the accpeted info</li>
</ol>

### db will include:

<ul>
    <li>licensePlateNumber str</li>
    <li>carColor str</li>
    <li>isDirty bool</li>
    <li>hoursParked int</li>
    <li>price float</li>
</ul>

### Want To Try It Out?

<p>No need to install any databases or community server packages. Everything required is inside the project. Simply open your code editor and terminal, then run the following commands.</p>

``` venv\Scripts\activate.bat ```

``` pip install -r requirements.txt ```

``` python app.py ```

<p>You can test this API with postman or create your frontend.</p>