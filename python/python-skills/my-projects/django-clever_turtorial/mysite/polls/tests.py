from django.test import TestCase
import datetime
from django.utils import timezone
# Create your tests here.
from .models import Question
from django.urls import reverse

def create_question(question_text,days):
    """
    Create a question with the given `question_text` and published the
    given number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    """
    time=timezone.now()+datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text,pub_date=time)



class QuestionDetailviewTest(TestCase):
    def testfuturequsetion(self):
        """
        The detail view of a question with a pub_date in the future
        returns a 404 not found.
        """
        future_question=create_question(question_text='future question',days=5)
        url=reverse('polls:detail',args=(future_question.id,))
        response=self.client.get(url)
        self.assertEqual(response.status_code,404)

    def test_past_question(self):
        """
        The detail view of a question with a pub_date in the past
        displays the question's text.
        """
        past_question = create_question(question_text='Past Question.', days=-5)
        url = reverse('polls:detail', args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)




class QuestionIndexViewTests(TestCase):
    def test_with_no_question(self):
        """
        If no questions exist, an appropriate message is displayed.
        """
        response=self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"No polls are available")
        self.assertQuerysetEqual(response.context['latest_question_list'],[])

    def test_with_past_questions(self):
        """
        Questions with a pub_date in the past are displayed on the
        index page.
        """
        question=create_question(question_text='past question',days=-30)
        response=self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'],['<Question: past question>'])

    def test_with_future_questions(self):
        """
        Questions with a pub_date in the future aren't displayed on
        the index page.
        """
        question=create_question(question_text='future question',days=30)
        response=self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'],[])

    def test_with_past_questions_and_future_question(self):
        """
        Even if both past and future questions exist, only past questions
        are displayed.
        """
        question1=create_question(question_text='future question',days=30)
        question2=create_question(question_text='past question',days=-30)
        response=self.client.get(reverse('polls:index'))        
        self.assertQuerysetEqual(response.context['latest_question_list'],['<Question: past question>'])

    def test_with_two_past_question(self):
        """
        The questions index page may display multiple questions.
        """
        question1=create_question(question_text='past question1',days=-30)
        question2=create_question(question_text='past question2',days=-5)
        response=self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'],['<Question: past question2>','<Question: past question1>'])                




class QuestionModelTest(TestCase):
    def test_was_published_recently_with_future_question(self):
        time=timezone.now()+datetime.timedelta(days=30)
        future_question=Question(pub_date=time)
    #check krega agr future question bana tu bananai dega (true) ya eror dega (false) agr ban nay diya tu hamaray code mai bug hai  
        self.assertIs(future_question.was_published_recently(),False)

    def test_was_published_recently_with_old_question(self):
        time=timezone.now()-datetime.timedelta(days=30)
        old_question=Question(pub_date=time)
        #check krega agr old question bana tu bananai dega (true) ya eror dega (false) agr ban nay diya tu hamaray code mai bug hai  

        """
        was_published_recently() returns False for questions whose pub_date
        is older than 1 day.
        """
        self.assertIs(old_question.was_published_recently(),False)

    def test_was_published_recently_with_recent_question(self):
        time=timezone.now()-datetime.timedelta(hours=23,minutes=59,seconds=59)
        recent_question=Question(pub_date=time)
        """ 
        was_published_recently() returns True for questions whose pub_date
        is within the last day.
        """
        self.assertIs(recent_question.was_published_recently(),True)

