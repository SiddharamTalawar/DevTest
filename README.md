This is the Python Development internship for Medius Technologies Private Limited 

Live link : https://dev-test-8iu825fv5-siddhus-projects.vercel.app/upload-file

Demo vedio : https://drive.google.com/file/d/1FetT1tS3ahsGueM6EiTHmSvcFJckhCl9/view?usp=sharing

Description :  this is a Django-based web page that prompts users for uploading an excel/csv file and Prepare a summary report for the uploaded data. (check the sample image below)
1) Django framework is used to build the backend of this webpage and HTMl and CSS is build Frontend.
2) when user opens the webpage it will show a page that is little bit similar to Medius AI company's home page.
3) there users can upload a excel/csv file and choose weather to recive a summary report in email by ticking a checkbar.
4) when user uploades the file they will lead to a new page which shows summery in HTMl table format.

Approach : 

1)file uploaded by the user is evaluvated in Backend, weather it is excel/csv format or does it contains required columns, if it dosen't then Value error is raised.

2)then using Python Pandas framework we create a dataframe from the file and manipalte it using group by operation on selected colums(state and pin) to get desired summary.

3)this summary is then sorted based on colums(state and DPD) to get result similar to the one given in samples.(the results whose DPD is 1 is filterd out as the sample output given satrrted from 2)

4)if user has cheked the send mail functon then he will recive summary in the email.

5)in the future we can also add functionality to download summary in excel format using excel writer to convert data frame to excel file.

![image1](https://github.com/user-attachments/assets/e2cff269-2651-460e-8a80-8bf7f353313c)

![image2](https://github.com/user-attachments/assets/b4d08110-de84-44ee-92f4-ca96d3333dbe)
