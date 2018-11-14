# Berkeley Class Stats
Abhishek Bollapragada, Fall 2018 VCG Dev.

### Description

Currently, Berkeley students have don't have a good idea of what their grade in a class is during the semester. For example, if I did 0.4 SDs above the mean in a class midterm how do I know what that means. This application attempts to solve that problem. I will be scraping berkeley time data to calculate statistics that would be useful to student during the semester to give them a better idea about their grades. 

### Timeline
**TODO**: Create a table outlining what you're going to work on step by step.

| # | Description   | Hours Estimated | 
| - | ------------- | --------------- | 
| 1 | Figure out where to scrape from the Berkeley Website | 2 Hours | 
| 2 | Design a Python approach to obtain xhr reponses from the berkeleytime website and parse them | 3 Hours |  
| 3 | Create a method to locally store all the data to increase runtime as opposed to scraping the website everytime | 2 Hour |
| 4 | Create a way to store course information by creating a Course class with all the relevant data | 1 Hours | 
| 5 | Find out how to generalize the code for any class as an input | 4 Hours |

### Technical Stack
**TODO**: Describe the languages, libraries, frameworks, and tools that went into your project. Make sure to add a brief description of its utility, unlike the list below.

* Python
* Requests ---> Allows interaction with berkeley time urls to fetch data
* JSON ---> Allows the parsing of JSON formatted files for ease of use
* Scipy ---> Will be helpful for statistics calculations
* Seleninum ---> An Automated Web Browser API that can be used for a wide range of functions
* Pickle ---> Provides local file storage and loading features that are compatible with JSON file formats 

### Implementation
**TODO**: Complete this while you're working on your project. Preferably, you're describing what steps you took for different parts of the project.

* Finding the data: I visited the berkeleytime website and inspected the network traffic to see where berkeley time is pulling its data from
* Find JSON link for test course (CS70) : I used COMPSCI 70 as my test course throughout the program implementation and backtracked what to do from there. The JSON link for this course contained alot of different number combinations and I was unsure about how to recreate a link for another course with those numbers.
* Wesbite Exploration: This was the most tedious part of the project because berkeleytime queries many different websites and databases for its information. To figure out how to get the JSON link I had to find the specific class and section ID's for each class.
* Creating a way to store classes: I made a class called Course.py and Course objects would contain all the relevant information one would need from that course such as the course id and course name.
* Parse JSON link into course objects: With the constructed JSON link for a class I had to take all the relevant information and store it in a Course object so I could use it later.
* Compile all sections of a course into 1 course: The way my program was written it scraped a course for each section it had on berkeleytime. So I created a set object of courses to store all the unique courses and their information. 
* Create a local file with courses for quick search: I used the pickle library to increase search speed by saving a copy of the course objects locally and searching through those instead of seraching through the website everytime. The website only changes every semester so pickle allows the application to be run on the website only when new data is released.
* Define function to calculate grade distributions for a course: I used the Scipy libraries here and created a function that took in a course object and outputted what exactly you would need in terms of SD's to get specific grades according to the history of the class data.
* Create basic input method for user experience: The way the program works for a user now is they just have to input a class name ex: COMPSCI 61A and then they can get back the distribution information for that class based on the past class data 

### Further Project Developments

* I will be including a more advanced user interface feature where users can input their midterm grades and get back what they need on other exams to get a certain grade in the class.

* I will develop feautures making enrollment easier such as finding classes that are near you that fulfill certain requirements ex: Finding a class close to Unit 3 that satisfies the historical sciences breadth. This can be done by a little additional scraping of the class addresses and the use of the geopy API to locate classes and calculate distances between them and you.

