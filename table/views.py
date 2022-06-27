from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .form import EmpForm
from .models import MyProject

''' To view a form'''


def form_request(request):
    if request.method == 'POST':
        # print("post_data", request.POST)
        project = EmpForm(request.POST, request.FILES)
        # Check the form data are valid or not
        if project.is_valid():
            data = ['Your registration is completed successfully.<br />']
            project.save()
            # Return the form values as response
            return HttpResponseRedirect('/table')

    else:
        project = EmpForm()
        return render(request, "form.html", {'form': project})


# def image(request):
#     if request.method == 'POST':
#         project= EmpForm(request.POST, request.FILES)

''' To list view '''


def list_view(request):
    projects = MyProject.objects.all().order_by('-id')
    return render(request, 'temp.html', {'projects': projects})  # bracket value mension for views


''' To update the form '''


def edit_post(request, id):
    context = {}
    project = get_object_or_404(MyProject, id=id)
    if request.method == 'POST':
        projects = EmpForm(request.POST, request.FILES, instance=project)
        if projects.is_valid():
            projects.save()
            return HttpResponseRedirect("/table/")

    context["projects"] = EmpForm(instance=project)
    return render(request, "edit.html", context)


def delete_view(request, id):
    """

    :param request:
    :param id:
    :return:

    To Delete post.
    """
    context = {}

    project = get_object_or_404(MyProject, id=id)

    if request.method == "POST":
        project.delete()
        return HttpResponseRedirect("/table/")

    return render(request, "delete.html", context)
