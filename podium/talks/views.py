"""This module implements the views."""

from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse_lazy
from .forms import TalkSubmissionForm
from .models import Session

NOT_IMPLEMENTED_MSG = 'This view is not implemented. Please tell the Podium ' \
                      'maintainers to fix this.'


def submit_talk_view(request):
    form = TalkSubmissionForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = TalkSubmissionForm()
        return HttpResponseRedirect(reverse_lazy('talks-sessions'))
    return render(request, 'talks/submit.html', {
        'form': form,
    })


def talk_detail_view(request, talk_id):
    """Raise an exception for something we plan to implement later."""
    raise Http404(NOT_IMPLEMENTED_MSG)


def session_list_view(request):
    sessions = Session.objects.all()
    # sessions = [s.filter(status='A') for s in sessions]
    print(sessions)
    context = {'sessions': sessions}
    return render(request, 'talks/sessions.html', context)


def session_talk_list_view(request, id):
    """Get the view for a Session and its associated talks."""
    session = get_object_or_404(Session, id=id)
    # render() invokes a template.
    return render(request, 'talks/session-detail.html', {
        'session': session,
        'talks': session.talks_available.all(),
    })
