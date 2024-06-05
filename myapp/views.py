# core/views.py
import pandas as pd
from .forms import UploadFileForm, QueryForm
from .models import UploadedFile, CompanyData
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required



@login_required
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.save()
            handle_uploaded_file(uploaded_file.file.path)
            return redirect('query_builder')
    else:
        form = UploadFileForm()
    return render(request, 'core/upload.html', {'form': form})


def handle_uploaded_file(file_path):
    chunk_size = 10000
    for chunk in pd.read_csv(file_path, chunksize=chunk_size):
        for index, row in chunk.iterrows():
            name = row.get('name', '')  # Get the value of 'name' column, provide a default value if missing
            city = row.get('city', '')  # Get the value of 'city' column, provide a default value if missing
            state = row.get('state', '')  # Get the value of 'state' column, provide a default value if missing
            country = row.get('country', '')  # Get the value of 'country' column, provide a default value if missing
            industry = row.get('industry', '')  # Get the value of 'industry' column, provide a default value if missing
            description = row.get('description', '')  # Get the value of 'description' column, provide a default value if missing
            founded = row.get('founded', None)  # Get the value of 'founded' column, None if missing
            size_range = row.get('size_range', '')  # Get the value of 'size_range' column, provide a default value if missing
            website = row.get('website', '')  # Get the value of 'website' column, provide a default value if missing
            employees = row.get('employees', None)  # Get the value of 'employees' column, None if missing

            if name and city and state and country and industry and description and founded is not None:
                # Create CompanyData instance only if all required fields are present
                CompanyData.objects.create(
                    name=name,
                    website=website,
                    city=city,
                    state=state,
                    country=country,
                    industry=industry,
                    description=description,
                    founded=founded,
                    size_range=size_range,
                    employees=employees
                )

@login_required
def query_builder(request):
    if request.method == 'POST':
        form = QueryForm(request.POST)
        if form.is_valid():
            filters = {}
            if form.cleaned_data['city']:
                filters['city__icontains'] = form.cleaned_data['city']
            if form.cleaned_data['state']:
                filters['state__icontains'] = form.cleaned_data['state']
            if form.cleaned_data['country']:
                filters['country__icontains'] = form.cleaned_data['country']
            if form.cleaned_data['industry']:
                filters['industry__icontains'] = form.cleaned_data['industry']
            if form.cleaned_data['employees_from']:
                filters['employees__gte'] = form.cleaned_data['employees_from']
            if form.cleaned_data['employees_to']:
                filters['employees__lte'] = form.cleaned_data['employees_to']
            count = CompanyData.objects.filter(**filters).count()
            return render(request, 'core/query_result.html', {'count': count})
    else:
        form = QueryForm()
    return render(request, 'core/query_builder.html', {'form': form})

@login_required
def user_list(request):
    users = User.objects.all()
    return render(request, 'core/user_list.html', {'users': users})


    