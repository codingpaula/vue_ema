from django.db import models
from django.core.validators import MaxValueValidator

from vue_ema.users.models import User

# Create your models here.
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class Topic(TimeStampedModel):
    topic_name = models.CharField(max_length=30)
    topic_owner = models.ForeignKey(User, on_delete= models.CASCADE)
    # TODO select better colors
    BLACK = '000000'
    GREY = '484A47'
    BROWN = '690500'
    YELLOW = 'F7EF81'
    YELLOWGREEN = 'D6D84F'
    LIGHTGREEN = '87A330'
    DARKGREEN = '243010'
    GREEN = '9BC53D'
    OLIVE = '656839'
    GREENBLUE = '7FC6A4'
    LIGHTBLUE = '4F7CAC'
    BLUE = '508991'
    DARKBLUE = '145C9E'
    RED = '800E13'
    DARKRED = '38040E'
    ORANGE = 'F9A03F'
    VIOLET = '963484'
    PINK = 'F45B69'
    PURPLE = '2E294E'
    TURQUOISE = '004346'
    COLOR_OPTIONS = [
        (BLACK, 'black'),
        (GREY, 'grey'),
        (BROWN, 'brown'),
        (YELLOW, 'yellow'),
        (YELLOWGREEN, 'yellowgreen'),
        (LIGHTGREEN, 'light green'),
        (DARKGREEN, 'dark green'),
        (GREEN, 'green'),
        (OLIVE, 'olive'),
        (GREENBLUE, 'greenblue'),
        (LIGHTBLUE, 'light blue'),
        (BLUE, 'blue'),
        (DARKBLUE, 'dark blue'),
        (RED, 'red'),
        (DARKRED, 'dark red'),
        (ORANGE, 'orange'),
        (VIOLET, 'violet'),
        (PINK, 'pink'),
        (PURPLE, 'purple'),
        (TURQUOISE, 'turquoise')
    ]
    color = models.CharField(max_length=6, choices=COLOR_OPTIONS, default=BLACK)

    def __str__(self):
        return self.topic_name


class Task(TimeStampedModel):
    task_name = models.CharField(max_length=50)
    task_description = models.TextField(max_length=3000, blank=True)
    importance = models.PositiveIntegerField(
        validators=[MaxValueValidator(101)],
        default=50
    )
    due_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    # TODO default duration
    duration = models.TimeField(auto_now=False, auto_now_add=False)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.task_name
