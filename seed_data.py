from students.models import Achievement, Category, Student
import os
import random
from datetime import date, timedelta

import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'student_management.settings')
django.setup()


def seed_data():
    print("Seeding categories...")
    categories = [
        ('Academic Excellence', 'Awards for high GPA and academic performance.'),
        ('Sports & Athletics', 'Achievements in inter-college or national sports.'),
        ('Cultural Arts', 'Recognition in music, dance, or drama.'),
        ('Technical Innovation', 'Hackathons, projects, and coding competitions.'),
        ('Social Service', 'Volunteer work and community engagement.')
    ]

    category_objs = []
    for name, desc in categories:
        cat, created = Category.objects.get_or_create(
            name=name, defaults={'description': desc})
        category_objs.append(cat)

    print("Seeding students...")
    student_data = [
        ('Rahul Sharma', 'rahul@example.com', 'REG001', 'B.Tech CS', '2022-26', 'Computer Science'),
        ('Priya Patel', 'priya@example.com', 'REG002', 'B.Tech IT', '2022-26', 'Information Technology'),
        ('Amit Singh', 'amit@example.com', 'REG003', 'B.E Mechanical', '2023-27', 'Mechanical'),
        ('Sneha Reddy', 'sneha@example.com', 'REG004', 'B.Com', '2023-26', 'Commerce'),
        ('Vikram Malhotra', 'vikram@example.com', 'REG005', 'B.Arch', '2021-26', 'Architecture'),
        ('Ananya Iyer', 'ananya@example.com', 'REG006', 'B.Tech EC', '2022-26', 'Electronics'),
        ('Arjun Das', 'arjun@example.com', 'REG007', 'B.Sc Physics', '2023-26', 'Science'),
        ('Kavita Nair', 'kavita@example.com', 'REG008', 'B.Tech CS', '2024-28', 'Computer Science'),
        ('Zaid Khan', 'zaid@example.com', 'REG009', 'BBA', '2023-26', 'Management'),
        ('Meera Joshi', 'meera@example.com', 'REG010', 'B.Tech AI', '2022-26', 'Artificial Intelligence'),
    ]

    student_objs = []
    for name, email, reg, course, batch, dept in student_data:
        student, created = Student.objects.get_or_create(
            register_number=reg,
            defaults={
                'name': name,
                'email': email,
                'course': course,
                'batch': batch,
                'department': dept,
                'status': 'Active'
            }
        )
        student_objs.append(student)

    print("Seeding achievements...")
    titles = [
        "Gold Medal in Semester", "1st Place in Inter-College Football",
        "Best Project Award", "NASA Space Apps Finalist",
        "Volunteered at NGO", "Classical Dance Winner",
        "Hackathon Runner Up", "Robotics Workshop Lead",
        "Scholarship Recipient", "Outstanding Leadership Award"
    ]

    for i in range(12):
        student = random.choice(student_objs)
        category = random.choice(category_objs)
        title = random.choice(titles)

        Achievement.objects.create(
            student=student,
            title=title,
            description=f"Automated description for {title}. Demonstrated excellence in the field.",
            category=category,
            date=date.today() - timedelta(days=random.randint(10, 300)),
            status=random.choice(['Approved', 'Pending', 'Rejected'])
        )

    print("Data seeding completed successfully!")


if __name__ == '__main__':
    seed_data()
