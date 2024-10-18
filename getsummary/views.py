from django.shortcuts import render
import pandas as pd
from .forms import UploadFileForm
from django.http import HttpResponseBadRequest, HttpResponse
from django.core.mail import send_mail
import json


def get_summery(file):
    """
    Get summary of the file.

    """

    # Read the file
    if file.name.endswith('.xlsx'):
        df = pd.read_excel(file, engine='openpyxl')
    elif file.name.endswith('.csv'):
        df = pd.read_csv(file)
    else:
        raise ValueError("Unsupported file type. Please upload a .xlsx or .csv file.")


    # Check if the file contains the required columns
    required_columns = {'Cust State','Cust Pin'}
    if not required_columns.issubset(df.columns):
        raise ValueError(f"Missing required columns. The file must contain {required_columns} columns.")
    
    # Get summary
    summary = df.groupby(['Cust State', 'Cust Pin']).size().reset_index(name='DPD') # Group by state and pin and count the number of DPD
    summary = summary[summary['DPD'] > 1]  # Filter rows with DPD > 1
    summary_final = summary.sort_values(['Cust State', 'DPD'], ascending=[True, True]) # Sort by state and DPD
    summary = summary_final
    return summary

def send_email(summery):
    """
    Send email with the summary of the file.

    """
    #converting summary to string for email body
    summery_str = summery.to_string(index=False) 
    send_mail('Python Assignment - Siddharam Talawar', summery_str, 'from@example.com', ['to@example.com'], fail_silently=False)


def handle_file_upload(request):
    
    """
    Handle file upload and return the summary of the file.

    """

    if request.method =='POST':
        # print('file received')
        try:
            form = UploadFileForm(request.POST, request.FILES)
            if form.is_valid():
                file = request.FILES["file"]
                # print('file  received')
                summary = get_summery(file)  #calling get_summery function

                # summary_str = summary.to_string(index=False) 
                # summary_str = summary.to_html( )
                # check if user wants the summary in email
                if request.POST.get('send_mail') == 'send_mail':
                    print('send mail function is called')
                    #-------------send mail function is commented out------------------
                    # send_email(summary)
                
                #converting data frame to dictionary so that it be styled in html
                #we can also use excel writer to convert data frame to excel file and download it, 
                datatable = summary.to_dict(orient="split", index=False)
                context = {'datatable': datatable}
                

                
            return render(request, 'summary.html', context)
            # return HttpResponse(summary_str)
        
        except ValueError as e:
                return HttpResponseBadRequest(str(e))
    else:
        #for get request return empty form
        form = UploadFileForm
        context = {'form':form}
        return render(request, 'upload_file.html', context)