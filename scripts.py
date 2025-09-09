from datacenter.models import Commendation, Schoolkid, Mark, Lesson, Chastisement
import random

COMMENDATIONS = [
    "Молодец!",
    "Отлично!",
    "Супер!",
    "Великолепно!",
    "Талантливо!"
]

def find_schoolkid(schoolkid_name):
    try:
        return Schoolkid.objects.get(full_name__contains=schoolkid_name)
    except Schoolkid.DoesNotExist:
        print(f"Ученик '{schoolkid_name}' не найден")
        return
    except Schoolkid.MultipleObjectsReturned:
        print(f"Найдено несколько учеников с именем '{schoolkid_name}'")
        return

def fix_marks(schoolkid):
    return Mark.objects.filter(schoolkid=schoolkid, points__in=[2, 3]).update(points=5)


def remove_chastisements(schoolkid):
    child_chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
    child_chastisements.delete()


def create_commendation(schoolkid, subject_title):
    lessons = Lesson.objects.filter(
        year_of_study=schoolkid.year_of_study,
        group_letter=schoolkid.group_letter,
        subject__title__contains=subject_title
    ).order_by('-date')

    if not lessons:
        print(f"Уроки по предмету '{subject_title}' не найдены")
        return

    last_lesson = lessons.first()

    commendation = Commendation.objects.create(
        text=random.choice(COMMENDATIONS),
        created=last_lesson.date,
        schoolkid=schoolkid,
        subject=last_lesson.subject,
        teacher=last_lesson.teacher
    )

    return commendation