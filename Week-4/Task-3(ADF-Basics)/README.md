# Task 3: ADF Basics

## Objective

Create Azure Data Factory resources and establish connections to Azure Blob Storage using Linked Services and Datasets. Validate the source file using the Get Metadata activity.

## Steps Performed

1. Created an Azure Data Factory instance named **samira-adf**.
2. Explored the ADF interface:

   * Author
   * Monitor
   * Manage
3. Created a Linked Service named **samira_BlobStorage** to connect ADF with Azure Blob Storage.
4. Created the source dataset **DS_Source_CSV** for the uploaded CSV file.
5. Configured the **Get Metadata** activity to retrieve:

   * Exists
   * Size
   * Last Modified
6. Validated the metadata configuration successfully.

## Components Used

* Azure Data Factory
* Azure Blob Storage
* Linked Service
* Dataset
* Get Metadata Activity

## Purpose

Linked Services establish connections to external data sources, Datasets represent the data to be processed, and Get Metadata is used to validate file properties before processing.

## Outcome

Successfully connected Azure Data Factory to Blob Storage, created datasets, and validated the source file using the Get Metadata activity.

## Screenshots


### Source Dataset
<img width="1398" height="1080" alt="Screenshot (46)" src="https://github.com/user-attachments/assets/ca46e94e-9992-4bf4-ad02-5a0f3e8b34aa" />


### Get Metadata Activity

<img width="1393" height="1080" alt="Screenshot (47)" src="https://github.com/user-attachments/assets/112012f7-ea16-406b-94f5-ea64bad3c7a8" />

