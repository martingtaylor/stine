# STINE - Some Times Itunes is Not Enough

## Contents
* Brief Overview of the projet
* ERD and Detailed discussion on the data stored
* Risk Assessment
* Application design and description
* CD/CI Intergation - Using Jenkins to install from GITHUB and executing the application

## Brief
The following is a brief outling of the STINE application. STINE is intend to be a simple to use database, that
allowes audiophile to record basic information on their audio collection. The project indentified key data elements
of interest, and based of these requirements design a simple/easy to use GUI and underlying database structure.


## ERD Description of the Project
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

## Risk Assessment
![RISK Assessment](https://github.com/martingtaylor/stine/blob/main/STINE%20Risk%20Assessment.PNG)

## Application design description
* Main Album Table
* Media Type
* Category
* Composer
* Label
* HTML Framework

## Application Deployment Structure

## Database design considerations

## CD / CI Integration

