# Scorched!
An Analysis of U.S. Wildfires from 1992-2015

### By: k.E.G.d. (Katlin, Enzo, Graham, Danieli)

![image](https://user-images.githubusercontent.com/92705556/164362996-733acdf8-498c-4ec8-83fc-886dc000c433.png)


## Project Overview
### Purpose
**Why Study Wildfires?**  *Wildfires affect us all!*
- Wildfires have the potential to harm property, livelihoods, and human health. 
- Multiple studies have found that climate change has already led to an increase in wildfire season length, wildfire frequency, and burned area.

- Colorado Stats *(from Colorado Division of Fire Prevention and Control: https://dfpc.colorado.gov/wildfire-information-center/historical-wildfire-information)*
    - 4 of the 5 largest CO wildfires have occured since 2018
    - 20 of the top 20 largest CO wildfires have occured in the last 20 years
    
  ![image](https://user-images.githubusercontent.com/92705556/164361745-b2a8f5df-9c5e-4cca-8481-0344584ea7f7.png)


### Source Data 
- **U.S. Wildfire data (plus other attributes)** (*https://www.kaggle.com/datasets/capcloudcoder/us-wildfire-data-plus-other-attributes*) 

### Questions to Investigate
-   Has the number, size, and cause of wildfires changed over time?
-   Has the timing and distribution of wildfires changed over time?
-   What temperature, wind, and humidity conditions are most likely to result in large wildfires?

### Technologies, Languages, Tools, and Algorithms Used
- Data Storage
   - GitHub
- Data Preprocessing
    - Python / Pandas
    - Visual Studio Code (VSCode)
- Data Analysis
    - Python / Pandas
    - Visual Studio Code (VSCode)
    - RStudio
- Database Management
    - Python / Pandas
    - Visual Studio Code (VSCode)
    - PgAdmin (PostgreSQL)
    - Quick DBD for ERD development
- Dashboard
    - HTML / Javascript
    - Google Slides
    - Tableau
    - VSCode

### Communication Plan
Beginning on March 26, 2022, the group held weekly meetings via Zoom in addition to more frequent communication via the following platforms. Each group member actively participated in meetings, contributed to group discussions, sought to help other group members who were stuck or struggling, and played to their personal coding strengths to make the final product the best it could be.

*Communication Platforms utilized for group discussions*
- GitHub
- Google Drive
- Slack
- Zoom

## Project Visualizations
### Dashboards
- Tableau: coming soon
- HTML App: coming soon

### Google Slides Presentation
- *https://docs.google.com/presentation/d/1k6_nFs06r_e-iALVW8RSOxMYcdh0ALGk/edit?usp=sharing&ouid=108250606024172523210&rtpof=true&sd=true*

## Data Exploration & Analysis Process
### Data Exploration
The "U.S. Wildfire data (plus other attributes)" dataset was downloaded from *kaggle* and explored using both Google Colab and Pandas. 
- *Entire Dataset:* 43 columns; 55,367 rows 
  
**Data Preprocessing**

Based on the original dataset, it was determined that the data needed to be cleaned of columns and rows dominated by large numbers of empty cells and zeros. In addition, some of the columns required reclassification based on data type and/or binning to reduce number of unique values. In the end, the data was reduced to 13,138 rows and 18 columns.  

**Cleaning DF** *Example of Data that needed to be cleaned/removed (putout_time is a string, '-1.000' values in weather columns, multiple '0' values)*

![image](https://user-images.githubusercontent.com/92705556/166401401-c87669e4-9566-478c-9c48-6acccc5d442f.png)

**Final Cleaned DF** *Columns kept: 'fire_id', 'fire_size', 'fire_cause', 'latitude', 'longitude', 'state', 'discovery_month', 'Temp_pre_30', 'Temp_pre_15', 'Temp_pre_7', 'Wind_pre_30', 'Wind_pre_15', 'Wind_pre_7', 'Hum_pre_30', 'Hum_pre_15', 'Hum_pre_7', 'year', 'putout_time'*

![image](https://user-images.githubusercontent.com/92705556/166401152-29aa583b-8636-4aa1-8222-330468401cd4.png)


### Database
To create our Database, we chose to use PgAdmin.  Within our database, we have four tables that are all connected through a common field: 'fire_id'. All relevant data within the four tables can be queried and joined for subsequent analysis. QuickDBD was used to create the Entity Relationship Diagram (ERD).

![image](https://user-images.githubusercontent.com/92705556/166401232-ca7e9e18-e3d7-4309-aa73-6b5c6f1bf58b.png)


## Data Analysis & Machine Learning



### Machine Learning
Because our initial dataset did not have paired inputs and known binary outcomes, we elected to use Unsupervised Machine Learning rather than Supervised Machine Learning for our analysis. Unsupervised Machine Learning allows for clustering of similar datapoints to see patterns in data groupings.   

## Conclusions
comming soon
