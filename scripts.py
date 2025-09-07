from datacenter.models import Commendation, Schoolkid, Mark, Lesson, Chastisement
import random


def fix_marks(schoolkid):
    try:
        child = Schoolkid.objects.get(full_name__contains=schoolkid_name)
    except (Schoolkid.DoesNotExist, Schoolkid.MultipleObjectsReturned):
        return

    bad_marks = Mark.objects.filter(schoolkid=child, points__in=[2, 3])
    updated_count = bad_marks.update(points=5)
    return updated_count


def remove_chastisements(schoolkid_name):
    try:
        child = Schoolkid.objects.get(full_name__contains=schoolkid_name)
    except (Schoolkid.DoesNotExist, Schoolkid.MultipleObjectsReturned):
        return

    chastisements = Chastisement.objects.filter(schoolkid=child)
    deleted_count = chastisements.delete()[0]
    return deleted_count


def create_commendation(schoolkid_name, subject_title):
    try:
        child = Schoolkid.objects.get(full_name__contains=schoolkid_name)
    except Schoolkid.DoesNotExist:
        print(f"Ученик '{schoolkid_name}' не найден")
        return
    except Schoolkid.MultipleObjectsReturned:
        print(f"Найдено несколько учеников с именем '{schoolkid_name}'")
        return

    lessons = Lesson.objects.filter(
        year_of_study=child.year_of_study,
        group_letter=child.group_letter,
        subject__title__contains=subject_title
    ).order_by('-date')

    if not lessons:
        print(f"Уроки по предмету '{subject_title}' не найдены")
        return

    last_lesson = lessons.first()

    praises = ["Молодец!", "Отлично!", "Супер!", "Великолепно!", "Талантливо!"]

    commendation = Commendation.objects.create(
        text=random.choice(praises),
        created=last_lesson.date,
        schoolkid=child,
        subject=last_lesson.subject,
        teacher=last_lesson.teacher
    )

    return commendation