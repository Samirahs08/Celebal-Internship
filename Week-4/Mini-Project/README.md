# Mini Project: Azure Data Pipeline using Azure Data Factory

## Objective

Build an end-to-end data pipeline that reads a CSV file from Azure Blob Storage, validates its metadata, and copies the data to a destination file using Azure Data Factory.

## Components Used

* Azure Blob Storage
* Azure Data Factory
* Linked Service (samira_BlobStorage)
* Source Dataset (DS_Source_CSV)
* Destination Dataset (DS_Destination_CSV)
* Get Metadata Activity
* Copy Data Activity

## Workflow

### Source

CSV file (**Sample - Superstore.csv**) stored in Azure Blob Storage.

### Metadata Validation

Used the **Get Metadata** activity to validate:

* File Exists
* File Size
* Last Modified Date

### Data Movement

Used the **Copy Data** activity to transfer data from the source dataset to the destination dataset.

### Destination

Created a new output file (**output.csv**) in Azure Blob Storage.

## Expected Output Achieved

* Pipeline executed successfully.
* Metadata validated successfully.
* Data copied from source to destination.
* Output file created in Blob Storage.

## Screenshots

### Source CSV File

<img width="1920" height="1080" alt="Screenshot (38)" src="https://github.com/user-attachments/assets/98d68415-d120-4d51-87cc-9be6d5407b4b" />


### Metadata Configuration

<img width="1393" height="1080" alt="Screenshot (47)" src="https://github.com/user-attachments/assets/892d78a7-56b1-4e5a-a94c-d8f30ac24e31" />


### Metadata Validation Success

<img width="1920" height="1080" alt="Screenshot (48)" src="https://github.com/user-attachments/assets/b4f52a59-2f5e-48d1-9d43-850d905175f2" />


### Copy Data Pipeline Success

<img width="1920" height="1080" alt="Screenshot (51)" src="https://github.com/user-attachments/assets/6bfb6f95-1aa1-46ec-999e-42e4492de347" />


