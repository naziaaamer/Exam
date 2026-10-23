# Theory Questions and Answers

## Q: What is the difference between unit testing, integration testing, regression testing and performance testing?


Unit testing - when we are testing the single functions or small unit of code 
independently to see if the method is working as expected. 


Integration testing - when two different modules are integrated and exchange 
data with each other. Integration testing is done to check if all the modules are 
working fine together as they are meant.


Regression testing - when the developer made any changes in existing code and that 
code can have effects on different places. regression tests are run to made sure that 
all the affected areas are still functional and working fine after the changes. 

Performance testing - To check how the application works under different workloads. We check 
the response time, how any resources are being used while performing some work. 

## Q: Describe the process of working with TDD.


Test driven development. This is reg, green and refactor process. 

Red -  write the tests for functionality and run the test to make it fail
Green - then we write enough logic so we can pass the test and 
Refactor -  improve the code without changing its behavior.  

## Q: Describe how BDD differs from TDD.

BDD tests focuses on how the application should behave and while the application matches
business perspective. BBD tests are written in plain language which can is understandable 


TDD how the single function or unit of code should be tested.


## Q:Imagine you were to build a web application similar to the Reading List, including both the frontend and the backend. 
    If you could choose freely,without any constraints, what types of tests would you want to use? Justify your choice.


Functional
    unit: test the methods separately. like add book. 
    integration: test the backend, front end and db communication works properly and are integrated. 
    E2E: test the whole work flows and features. 
    DB: test the data is saving and deleting as expected from the db. 
    API: test the endpoints and see the data is going to DB as expected. 

Non-functional
    usability: test how easy it is for customers to use the website functionality.
    performance: response time, loading time with different speed of net and component communication under 
                 normal usage and under heavy workload.   
    cross browser: website works properly on different browser. All the UI elements are displayed properly.