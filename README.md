# Day 2

**Deadline**: before Day 3 start

## 1. (team, mandatory, 15 pt) Project description

The goal: write a high-level description of your team capstone project.

Project: data processing pipeline - processing social media data (reddit)

Language - Python & Ksql

##### Azure components

Azure functions, Event Hub, Blob storage

##### High component level architecture

https://github.com/dmytrahaaa/cloud-platforms_azure/blob/hw_2/capstone_project_description/cloud_project_design.png

#### Components

##### Message producer

Entry point to the application. Reads Reddit comments from prepared .csv file and produces each record as a separate message to kafka topic '' using avro format

##### Language detector

Consumer for 'comments-stream' topic. Detect language of the message and Produces message with detected language to 'lang-stream' topic.

##### Statistics
Python script with executes ksql queries against ksql-cli server. Reads topics 'lang-stream'

##### Data set
Reddit comments .csv file with 5000 of messages.


## 2. (individual, mandatory, 15 pt) Function as a Service sample

The goal: to try in the wild real FaaS offering.

FaaS function implementation - faas_func directory

Result screens - screenshots directory
