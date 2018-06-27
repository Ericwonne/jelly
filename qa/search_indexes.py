from haystack import indexes
from qa.models import Question,Answer
import datetime


class QuestionIndex(indexes.SearchIndex,indexes.Indexable):
    text=indexes.CharField(document=True,use_template=True)
    asker=indexes.CharField(model_attr='asker')
    title=indexes.CharField(model_attr='title')
    categories=indexes.CharField(model_attr='categories')
    pubtime=indexes.DateTimeField(model_attr='pubtime')
    glances=indexes.IntegerField(model_attr='glances')

    def get_model(self):
        return Question

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(pubtime__lte=datetime.datetime.now())

class AnswerIndex(indexes.SearchIndex,indexes.Indexable):
    text=indexes.CharField(document=True,use_template=True)
    pubtime=indexes.DateTimeField(model_attr='pubtime')
    if_read=indexes.IntegerField(model_attr='if_read')
    answerer=indexes.CharField(model_attr='answerer')
    question=indexes.CharField(model_attr='question')
    glances=indexes.IntegerField(model_attr='glances')


    def get_model(self):
        return Answer

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(pubtime__lte=datetime.datetime.now())
