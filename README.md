# STINE - Some Times Itunes is Not Enough

## Contents
* Brief Overview of the projet
* ERD and Detailed discussion on the data stored
* Application design and description
* CD/CI Intergation - Using Jenkins to install from GITHUB and executing the application
* Project Tracking
* Risk Assessment
* Testing
* Conclusions


## Brief
The following is a brief outling of the STINE application. STINE is intend to be a simple to use database, that
allowes audiophile to record basic information on their audio collection. The project indentified key data elements
of interest, and based of these requirements design a simple/easy to use GUI and underlying database structure.

## Techincal Elements
Whilst executing the project:
* User stories where created and managed on the JIRA platform
* The User Interface will be a WEB front end.
* The Application will be designed and deployed as a WEB/Cloud bassed system.
* Relational Databases are utilised to store data: SQLITE for Dev, GCP based MySQL for Prod.
* Documentation had been either created before a task, or appended after the task.
* Programming best practices have been followed when using PYTHON, FLASH, HTML, JINGA2, etc
* GITHUB has been used as a code repository: https://github.com/martingtaylor/stine

## ERD and Description of the Project
Following formal meetings with potiental users of STINE, a number of key data elements where identified as useful 
to a collector of audio media, these included:
* Name/title of Album
* Composer
* Artist
* Performers
* Type (Vynal/CD)
* Label
* Date Recorded
* Category (Classical, Jazz, Rock, Blues, etc)
* Compliation
* Number of Tracks
* Number of disks
* Duration
* Digital/Analog

Following normalisation, the data elements where grouped in a number of seperate tables:
* ALBUM - the central table contain either base data or links to other tables.
* COMPOSERS - A table containing the names of individual composers. 
* MEDIA_TYPES - A list of the basic media types: C.D., Vinyl, Digit. This table is considered non changing.
* LABELS - A list of media publishers.
* CATEGORIES - A list of musical type, such as Jazz, Classical, Country, etc.

All these tables form a Many-to-One relationship with the central Ablum table:
|Table      |Relationship                                      |
|-----------|--------------------------------------------------|
|COMPOSERS  |One composers relates to none, one or many Albums |
|MEDIA_TYPES|One Media Type relates to none, one or many Albums|
|LABELS     |One Label relates to none, one or many Albums     |
|CATEGORIES |One category relates to none, one or many Albums  |

As can be seen, the creates a simple star structure with the Albums table in the centre.

The following ERD diagram shows the originally intended structure:
![STINE ERD1](https://github.com/martingtaylor/stine/blob/main/STINE%20ERD.png)

### Revision History:
It should be noted that due to time constraits a number of non-key data items have been dropped from the final implementation.
These include:
|Drop Field          |
|--------------------|
|Artist              |
|Conductor           | 
|Data Recorded       |
|Digital Analog      |
|Compilation Flag    |
|Run Time            |

All of the above fields are fields within the Albums tables and can ommited without affecting the overal design or function.
All these fields can be easily be added to the application, time permitting.

Removing the unimplemented fields gives a revised ERD diagram:
![STINE ERD2](https://github.com/martingtaylor/stine/blob/main/stine2.png)

## Application design description
### Overview
The techincal brief defined a number of tools/techniques/frameworks to employ:
* Cloud based production system: GCP
* Databases: SQLITE for Dev, MySQL for Prod
* WEB Interface
* Development Language: PYTHON
* Interface: WEB using HTML

### Frameworks
To achieve a reliable WEB based, database application using PYTHON, the following frameworks where selected for reliablity and robustness:
|Frameworks|Description|
|----------|-----------|
|SQLAchemny|A PYTHON base interface to backend database layers|
|FLASK     |WEB Services framework for PYTHON|
|WTForms   |WEB Forms Management software|
|JINGA2    |WEB/PYTHON interaction framework|

### Application Design
It was desided to keep the application user exprienance as simple as possible, using the same working methodology to all interfaces. The number of interfaces should be mininal, with easy context switching using a standard menu available on each interface screen.

The application included a seperate interface for each data table defined in the ERD. This includes:
* The main Album
* The music category
* The Composer
* The Pusblisher Labels

NOTE: the Media Type table is created is not alterable by design, and is populated when the database is deployed.

In addition to the interfaces, a simple menu system is included to context switch to each of the screens. The menu is imbedded with the main.html page, which includes a JINGA2 block, inwhich all other html pages are embedded. This approah makes the menu available to all interfaces.

The following directory structuer was used to host the application:

![DIR](https://github.com/martingtaylor/stine/blob/main/STINE_DIR_STRUCTURE.PNG)


## CD / CI Integration
### Development Cycle:
The application was developed and deployed using the following CI methodology:
1. A public GITHUB repository was created for the STINE account containing this README.md
2. The repository was cloned to the development PC.
3. Microsoft Visual Studio Code 1.56 was connected to the STINE GIT repository.
4. During the development cycle, regular commits where made to the main branch repo.

### Jenkins Deployment:
When Jenkins "Build" is invoked:

![JENKINSBuild](images/STINE_JENKINS_BUILD.PNG)

1. Query the user to select on the choice of MYSQL or SQLITE database types and whether to recreate the database.
2. On execution - download the latest STINE GIT main branch and deploy to a Jenkins Workspace.
3. Set the Database connection string (based on the choice made above) and store to an environmental variable.

**NOTE:** It should be noted that 3 lines in the build relating to the installation (requirements, pymysql, gunicorn) have been
commented out. This was due to these items crashing the build process. These items where installed on the command line using sudo
to get around this problem, and I will investigate this issue later.

4. Check the **CREATEDB** environmental variable, and if set to true, run the **CREATE.PY** program to drop and recreate the database on the selected database.
5. Invoke the **GUNICORN** WEB Host and execute the application.


## Project Tracking
The JIRA Project Management tool was used to track and manage the application during the development, testing deployment cycle:
![JIRA](https://github.com/martingtaylor/stine/blob/main/STINE_JIRA.PNG)
The JIRA configuration allows:
* Management of the "To-Do list" - user stories, summarising "Who Wants", "What they Want" and "What they except"
* The "In progress" - containing items currently being worked on, or blocked items.
* The "Done List" - Items that have been completed and tested, or approved.


## Risk Assessment
An initial Risk Assessment was completed on project commencement:
![RISK Assessment](https://github.com/martingtaylor/stine/blob/main/STINE%20Risk%20Assessment.PNG)


Revision History: Since then the assessment has been revised on a number of occassions:
|Date      |Item|Title                      |Description|New Likihood|
|----------|----|---------------------------|-----------|------------|
|03/05/2021|4   |Legal Constraints          |As the system was for private and non profit use only and does not contain actual audio media data, this can be dismissed.|Dissmed|
|19/05/2021|2   |Lack of technical Knowledge|Due to lack of techincal knowledge, was unable to default selection boxs to stored values.                                |Very Probable|
|19/05/2021|5   |System failes User Test    |Due to select fields not default, user testing will fail                                                                  |Very Probable|


## Testing

## Conclusions

