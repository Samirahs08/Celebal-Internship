# Week 4: Azure Cloud Fundamentals and Data Pipeline Implementation using ADF

## Objective

The objective of this assignment is to understand Azure cloud concepts and build an end-to-end data pipeline using Azure Storage Account and Azure Data Factory (ADF).

## Technologies Used

* Microsoft Azure
* Azure Resource Group
* Azure Storage Account
* Azure Blob Storage
* Azure Data Factory (ADF)
* Linked Services
* Datasets
* Get Metadata Activity
* Copy Data Activity
* IAM Roles

## Tasks Completed

### Task-1(Resource-Group)

Created a Resource Group (**samira-rg**) to organize and manage Azure resources used throughout the project.

### Task-2(Storage-Setup)

Created an Azure Storage Account, Blob Container, and uploaded the source CSV file (**Sample - Superstore.csv**).

### Task-3(ADF-Basics)

Created Azure Data Factory, configured Linked Services and Datasets, and validated the source file using the Get Metadata activity.

### Task-4(Pipeline-Development)

Built a data pipeline using the Copy Data activity and configured source and destination datasets.

### Task-5(Pipeline-Execution)

Executed the pipeline using Debug mode and verified successful execution.

### Task-6(IAM-Roles)

Configured IAM role assignments and provided Azure Data Factory access to Azure Blob Storage.

## Mini Project

### Problem Statement

Build a complete data pipeline that reads a CSV file from Azure Blob Storage and processes it using Azure Data Factory.

### Workflow

```text
Azure Blob Storage
        │
        ▼
   Get Metadata
        │
        ▼
    Copy Data
        │
        ▼
   output.csv
```

### Components Used

* Azure Blob Storage
* Azure Data Factory
* Linked Service
* Source Dataset
* Destination Dataset
* Get Metadata Activity
* Copy Data Activity

### Outcome

* Successfully connected Azure Data Factory to Azure Blob Storage.
* Validated file metadata using Get Metadata activity.
* Copied data from source CSV to destination file.
* Executed the pipeline successfully.
* Verified output file creation in Blob Storage.

## Folder Structure

```text
Week-4
│
├── Task-1(Resource-Group)
├── Task-2(Storage-Setup)
├── Task-3(ADF-Basics)
├── Task-4(Pipeline-Development)
├── Task-5(Pipeline-Execution)
├── Task-6(IAM-Roles)
└── Mini-Project
```

## Learning Outcomes

* Understanding Azure Resource Management
* Working with Azure Blob Storage
* Creating Linked Services and Datasets in ADF
* Building and executing data pipelines
* Validating files using Get Metadata
* Implementing Copy Data activity
* Managing access using IAM Roles
* Developing an end-to-end cloud-based data pipeline
