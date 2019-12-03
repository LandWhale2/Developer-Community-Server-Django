from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.views.generic import ListView, DetailView
from polls.models import Question, Choice

# Create your views here.



class IndexView(ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]#get_queryset은 pub_data 컬럼 기준으로 최신 5개 질문을 불러와 last_question에 저장


# detailview 는 객체 하나에 대한 상세한 정보를 나타내는 뷰
class DetailsView(DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultView(DetailView):
    model = Question
    template_name = 'polls/results.html'


#투표기능은 논리연산만 처리하기 때문에 템플릿을 필요로 하지않음 , 논리연산만 처리한다음에 다음 페이지로 이동하기위해 redirect 함
def vote(request, pk):
    question = get_object_or_404(Question, pk=pk)#404 함수는 특정 객체를 테이블로 부터 조회해 반환한다
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])#choice 셋 함수로 해당 객체 관련 choice 객체들을 불러온뒤 get 함수로 객체중 사용자가 선택한 choice 객체와 일치하는것 찾아서 반환
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question' : question,
            'error_message': "잘못 선택하였습니다. ",
        })
    else:
        selected_choice.votes += 1#레코드값 1증가시킨뒤save()
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))#reverse <<뷰 함수에서 url 스트링 추출하는법