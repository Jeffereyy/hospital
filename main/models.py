from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=20)
    specialization = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name} {self.specialization}"

class Schedule(models.Model):
    doctor_name = models.ForeignKey(Doctor, on_delete=models.PROTECT, related_name="schedule_doctor_name")
    date_time = models.DateTimeField()
    vacant = models.BooleanField(default=True)
    patient_name = models.CharField(blank=True, max_length=20)

    if vacant:
        vacan_str = "vacant"
    else:
        vacan_str = "booked"

    def __str__(self):
        # date_time = str(self.date_time)
        return f"{self.doctor_name} - {self.date_time} - {self.vacan_str}"